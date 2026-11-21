"""Maintain sourced, per-model firmware lifecycles and a duration-ranked recap.

No network or workflows. Publishing is an ordinary, separately leased Git commit.
"""
import calendar
import datetime as dt
import difflib
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PAGE = "FIRMWARE-UPDATES.md"
CHECKED = "2026-11-21"
STATUSES = {"verified_latest", "latest_located", "no_public_firmware_found", "not_applicable", "unverified"}


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def identity():
    assert git("branch", "--show-current") == "main"
    assert git("remote", "get-url", "origin") in {
        "https://github.com/kokizzu/instrumentfx.git", "git@github.com:kokizzu/instrumentfx.git"}


def bounds(value):
    if value is None:
        return None
    assert re.fullmatch(r"\d{4}(?:-\d{2}(?:-\d{2})?)?", value), value
    nums = list(map(int, value.split("-")))
    if len(nums) == 1:
        return dt.date(nums[0], 1, 1), dt.date(nums[0], 12, 31)
    if len(nums) == 2:
        y, m = nums
        return dt.date(y, m, 1), dt.date(y, m, calendar.monthrange(y, m)[1])
    return (dt.date(*nums),) * 2


def span(record):
    start, end = bounds(record["first_release"]["date"]), bounds(record["firmware"]["date"])
    if start is None or end is None:
        return None
    low, high = (end[0] - start[1]).days, (end[1] - start[0]).days
    if high < 0:
        return {"minimum_days": low, "maximum_days": high, "label": "Firmware predates hardware release"}
    low = max(0, low)
    text = f"{low / 365.2425:.2f} years" if low == high else f"{low / 365.2425:.2f}–{high / 365.2425:.2f} years"
    return {"minimum_days": low, "maximum_days": high, "label": text}


def validate_record(record, inventory):
    assert record["model_key"] in inventory, record["model_key"]
    assert record["checked_date"] == CHECKED
    assert record["firmware"]["status"] in STATUSES
    assert record.get("sources"), "Every audit needs its checked source trail"
    source_urls = {s["url"] for s in record["sources"]}
    assert all(url.startswith(("https://", "http://")) for url in source_urls)
    for name in ("first_release", "firmware"):
        item = record[name]
        date = item["date"]
        expected = {4: "year", 7: "month", 10: "day"}.get(len(date)) if date else "unknown"
        assert item["precision"] == expected, (name, date, item["precision"])
        if date:
            assert bounds(date)[0] <= dt.date.fromisoformat(CHECKED), "Future release"
            assert item["source_urls"], "A date requires a source"
        assert set(item["source_urls"]) <= source_urls
    if record["firmware"]["status"] == "verified_latest":
        assert record["firmware"]["version"] and record["firmware"]["source_urls"]
    record["duration"] = span(record)
    return record


def clean(value):
    return str(value or "Not verified").replace("|", "\\|").replace("\n", " ")


def links(urls, label="source"):
    return " ".join(f"[{label} {i}]({url})" for i, url in enumerate(dict.fromkeys(urls), 1))


def release_text(record):
    r = record["first_release"]
    kind = r.get("kind", "unknown").replace("_", " ")
    return clean(r["date"]) + (f" ({clean(kind)})" if r["date"] else "")


def firmware_text(record):
    f = record["firmware"]
    labels = {"verified_latest": "Latest verified", "latest_located": "Located; latest status unverified", "no_public_firmware_found": "No public firmware located", "not_applicable": "Not applicable", "unverified": "Unverified"}
    return f"{clean(f['version'])} — {labels[f['status']]}"


def render_record(record):
    r, f = record["first_release"], record["firmware"]
    duration = record["duration"]["label"] if record["duration"] else "Not calculable from verified dates"
    rows = [
        ("Hardware first release / date basis", release_text(record) + ". " + clean(r.get("note", "")) + " " + links(r["source_urls"])),
        ("Device firmware / current verification", firmware_text(record) + ". " + clean(f.get("note", "")) + " " + links(f["source_urls"])),
        ("Firmware release date / precision", clean(f["date"]) + " (" + f["precision"] + " precision)"),
        ("Firmware release-to-update span", duration + "; calculated from the stated hardware-date basis, not a promise of continuous or future support."),
        ("Firmware audit checked", CHECKED + "; see the [duration-sorted firmware comparison](../" + PAGE + ")."),
    ]
    text = "### Firmware lifecycle\n\n| Field | Verified evidence |\n|---|---|\n"
    text += "\n".join("| " + field + " | " + value + " |" for field, value in rows) + "\n\n"
    if record.get("notes"):
        text += "\n\n".join(clean(n) for n in record["notes"]) + "\n\n"
    text += "Firmware sources checked:\n\n" + "\n".join(
        f"- [{clean(s.get('title') or s['url'])}]({s['url']}) — {clean(s['evidence'])} ({clean(s.get('access', 'opened'))})."
        for s in record["sources"]) + "\n\n"
    return "<!-- firmware-lifecycle begins -->\n" + text + "<!-- firmware-lifecycle ends -->\n\n"


def render_page(state):
    audit = state["firmware_lifecycle"]
    records = audit["models"]
    ranked, dated, unresolved = [], [], []
    for key, record in records.items():
        duration = record["duration"]
        if duration and duration["maximum_days"] >= 0:
            (ranked if record["firmware"]["status"] == "verified_latest" else dated).append(key)
        else:
            unresolved.append(key)
    order = lambda key: (-records[key]["duration"]["minimum_days"], -records[key]["duration"]["maximum_days"], key.casefold())
    ranked.sort(key=order)
    dated.sort(key=order)
    unresolved.sort(key=str.casefold)
    text = "# Firmware updates — release-to-update duration\n\n[Repository](README.md) · [Guitar](all-guitar.md) · [Bass](all-bass.md) · [Vocal](all-vocal.md)\n\n"
    text += f"**Checked {CHECKED}. {len(records)} of {len(audit['scope'])} active models audited.** Each model is saved in a separate commit. Unknown dates remain unknown; this page does not certify installed firmware on a seller's unit.\n\n"
    text += "## Reading the ranking\n\n"
    text += "Duration means **latest located device-firmware release date minus the unit's first hardware release date**. Retail/shipping dates are preferred when documented; an announcement is explicitly identified when used instead. Software editors, drivers, updater apps, manual revisions and download-page crawl dates are not firmware releases. Public beta versions are identified separately when relevant.\n\n"
    text += "Exact dates use elapsed days ÷ 365.2425, rounded to two decimals. A month/year-only date produces an honest minimum–maximum interval. Rows sort by the **largest verified minimum duration**, then maximum duration; overlapping intervals do not establish a strict order. A pre-launch firmware date is kept visible rather than forced into a positive span. This measures an observed release span, not continuous support, update frequency or a promised support lifetime.\n\n"
    text += "Unknown, unavailable and non-updatable are different states. A failed download or search is not evidence of no firmware. Historical version claims remain qualified if current latest status cannot be established.\n\n"

    def table(keys):
        result = "| Model / complete evidence | First hardware release / basis | Device firmware | Firmware release | Elapsed span | Sources |\n|---|---|---|---|---|---|\n"
        for key in keys:
            record = records[key]
            f = record["firmware"]
            link = state["comparison_model_sources"][key]["link"]
            duration = record["duration"]["label"] if record["duration"] else "Not calculable"
            result += f"| [{clean(key.replace('::', ' '))}]({link}) | {release_text(record)} | {firmware_text(record)} | {clean(f['date'])} | {duration} | {links(record['first_release']['source_urls'], 'launch')} {links(f['source_urls'], 'firmware')} |\n"
        return result if keys else "No qualifying records verified yet.\n"

    text += "## Latest firmware verified — longest span first\n\n" + table(ranked)
    text += "\n## Dated firmware located — current latest status unresolved\n\n" + table(dated)
    text += "\n## Audited records without a calculable span\n\n" + table(unresolved)
    pending = sorted(set(audit["scope"]) - set(records), key=str.casefold)
    text += "\n## Remaining model checks\n\n"
    text += ("; ".join(clean(k.replace("::", " ")) for k in pending) + ".\n") if pending else "Every active model has an individual audit record. Unresolved dates and versions above remain unresolved, not assumed.\n"
    return text


def prepare(evidence_path):
    identity()
    assert not git("diff", "--name-only"), "Tracked local changes need review before another model"
    assert not git("diff", "--cached", "--name-only"), "Index is not clean"
    state = json.loads((ROOT / "research-state.json").read_text())
    inventory = {b + "::" + m for b, models in state["inventory_by_brand"].items() for m in models}
    record = validate_record(json.loads(Path(evidence_path).read_text()), inventory)
    key = record["model_key"]
    base = git("rev-parse", "HEAD")
    audit = state.setdefault("firmware_lifecycle", {"checked_date": CHECKED, "scope": sorted(inventory), "method": "Hardware first release to latest verified device firmware; date bounds, no assumed day, 365.2425 days per year; per-model commits.", "models": {}, "next_models": []})
    assert set(audit["scope"]) == inventory
    assert key not in audit["models"], "Model already audited; review before replacing evidence"
    audit["models"][key] = record
    audit["next_models"] = sorted(inventory - set(audit["models"]), key=str.casefold)
    audit["status"] = "all_models_checked_with_explicit_gaps" if not audit["next_models"] else "in_progress"
    audit["completed_model_count"] = len(audit["models"])
    audit["last_model"] = key
    audit["last_commit_parent"] = base
    link = state["comparison_model_sources"][key]["link"]
    path, anchor = link.split("#", 1)
    brand = (ROOT / path).read_text()
    headings = list(re.finditer(r"^## (.+)\n", brand, re.M))
    slug = lambda s: re.sub(r"[^\w\- ]", "", s.lower().replace("`", "")).replace(" ", "-")
    matching = [h for h in headings if slug(h[1]) == anchor]
    assert len(matching) == 1, (key, link)
    heading = matching[0]
    insertion = heading.end()
    (ROOT / path).write_text(brand[:insertion] + "\n" + render_record(record) + brand[insertion:].lstrip("\n"))
    (ROOT / "research-state.json").write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")
    (ROOT / PAGE).write_text(render_page(state))
    readme_path = ROOT / "README.md"
    readme = readme_path.read_text()
    if "[FIRMWARE-UPDATES.md]" not in readme:
        marker = "| **[MULTI-EFFECTS.md]"
        position = readme.index(marker)
        readme = readme[:position] + "| **[FIRMWARE-UPDATES.md](FIRMWARE-UPDATES.md)** | Device firmware, hardware release dates and longest release-to-update spans; date precision, source conflicts and missing evidence retained |\n" + readme[position:]
        readme_path.write_text(readme)
    # The existing generator propagates model-specific firmware facts to eligible instrument rows.
    import comparison_views as cv
    plan = cv.make_plan(persist=False)
    for name, content in plan["outputs"].items():
        if (ROOT / name).read_text() != content:
            (ROOT / name).write_text(content)
    subprocess.run(["git", "diff", "--check"], cwd=ROOT, check=True)
    # Re-use the repository's established gates; no workflows or network execution.
    log = ROOT.parent / "firmware-validation.log"
    with log.open("w") as out:
        subprocess.run(["make", "brand-sort-test", "research-verify", "comparison-verify"], cwd=ROOT, stdout=out, stderr=subprocess.STDOUT, check=True)
    files = git("diff", "--name-only").splitlines()
    files += [p for p in (PAGE, "scripts/firmware_lifecycle.py") if not git("ls-files", p)]
    changes = []
    for name in dict.fromkeys(files):
        tracked = bool(git("ls-files", name))
        old = subprocess.check_output(["git", "show", base + ":" + name], cwd=ROOT).decode() if tracked else ""
        new = (ROOT / name).read_text()
        old_lines, new_lines = old.splitlines(keepends=True), new.splitlines(keepends=True)
        # autojunk anchors on uncommon lines and keeps this delta small for the large ledger.
        ops = [[i, j, new_lines[a:b]] for tag, i, j, a, b in difflib.SequenceMatcher(None, old_lines, new_lines).get_opcodes() if tag != "equal"]
        changes.append({"path": name, "old_blob": git("rev-parse", base + ":" + name) if tracked else None, "new_blob": git("hash-object", name), "ops": ops})
    payload = {"repository": "kokizzu/instrumentfx", "branch": "main", "base_commit": base, "model_key": key, "message": "docs(firmware): audit " + key.replace("::", " ") + " release and update history", "files": changes, "evidence_path": str(Path(evidence_path).resolve()), "validated": True}
    target = ROOT.parent / "firmware-publish.json"
    target.write_text(json.dumps(payload, ensure_ascii=False))
    print(json.dumps({"payload": str(target), "model": key, "files": [x["path"] for x in changes], "completed": len(audit["models"])}))


def verify():
    identity()
    state = json.loads((ROOT / "research-state.json").read_text())
    audit = state["firmware_lifecycle"]
    inventory = {b + "::" + m for b, models in state["inventory_by_brand"].items() for m in models}
    assert set(audit["scope"]) == inventory
    for record in audit["models"].values():
        previous = record["duration"]
        validate_record(record, inventory)
        assert record["duration"] == previous
    assert (ROOT / PAGE).read_text() == render_page(state)
    assert audit["completed_model_count"] == len(audit["models"])
    assert set(audit["next_models"]) == inventory - set(audit["models"])
    print(f"PASS: {len(audit['models'])} model lifecycles, date bounds, ranking and remaining queue")


if __name__ == "__main__":
    if sys.argv[1] == "prepare":
        prepare(sys.argv[2])
    elif sys.argv[1] == "verify":
        verify()
    else:
        raise SystemExit("Use prepare <evidence.json> or verify")
