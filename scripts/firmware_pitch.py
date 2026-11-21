"""Apply one sourced firmware/pitch audit, then render comparisons locally.

No network, commits, workflows, or automatic unknown-filled model records.
The existing firmware_lifecycle ledger and historical audit evidence are retained.
"""
import copy
import datetime as dt
import json
from pathlib import Path
import re
import subprocess
import sys

import firmware_lifecycle as lifecycle

ROOT = Path(__file__).resolve().parents[1]
FORMAT = "firmware-pitch-v1"
FIRMWARE_PAGE = "FIRMWARE-UPDATES.md"
PITCH_PAGE = "PITCH-SHIFTING.md"
PITCH_LABELS = {
    "documented_polyphonic": "Documented polyphonic",
    "documented_monophonic": "Documented monophonic",
    "pitch_present_polyphony_unverified": "Pitch present; polyphony unverified",
    "no_pitch_documented": "No pitch algorithm documented in checked sources",
    "unverified": "Unverified",
    "not_applicable": "Not applicable",
}
BLOCK = re.compile(r"<!-- firmware-pitch:([^\n]+) begins -->\n.*?<!-- firmware-pitch:\1 ends -->\n*", re.S)


def clean(value):
    return str(value if value not in (None, "") else "Not verified").replace("|", "&#124;").replace("\n", " ")


def links(urls, label="source"):
    return " ".join(f"[{label} {n}]({url})" for n, url in enumerate(dict.fromkeys(urls), 1))


def inventory(state):
    return {brand + "::" + model for brand, models in state["inventory_by_brand"].items() for model in models}


def without_generated_blocks(text):
    """Comparison extraction uses per-key ledger data instead of shared prose."""
    return BLOCK.sub("", text)


def date_span(record):
    start = lifecycle.bounds(record["first_release"]["date"])
    end = lifecycle.bounds(record["firmware"]["date"])
    if start is None or end is None:
        return None
    low, high = (end[0] - start[1]).days, (end[1] - start[0]).days
    label = f"{low / 365.2425:.2f} years" if low == high else f"{low / 365.2425:.2f}–{high / 365.2425:.2f} years"
    if high < 0:
        label += " (firmware predates hardware release)"
    elif low < 0:
        label += " (date ranges overlap; order unresolved)"
    return {"minimum_days": low, "maximum_days": high, "label": label}


def model_link(state, record):
    key = record["model_key"]
    if key in inventory(state):
        result = state["comparison_model_sources"][key]["link"]
        assert not record.get("model_link") or record["model_link"] == result, "Canonical link mismatch"
    else:
        assert record.get("scope") in {"supplemental", "archival"}, "Unknown model needs explicit supplemental/archival scope"
        result = record["model_link"]
    path, separator, anchor = result.partition("#")
    assert separator and anchor and ".." not in Path(path).parts
    assert (path.startswith("brand/") and path.endswith(".md")) or path in {"single-guitar.md", "single-bass.md", "single-vocal.md"}
    assert (ROOT / path).is_file(), result
    return result


def validate_record(record, state, require_pitch=True):
    key = record["model_key"]
    assert isinstance(key, str) and "::" in key and not any(x in key for x in ("\n", "--", "<", ">"))
    checked = dt.date.fromisoformat(record["checked_date"])
    assert record["firmware"]["status"] in lifecycle.STATUSES
    assert record.get("sources"), "Each model needs an actual checked source trail"
    source_urls = set()
    for source in record["sources"]:
        assert source["url"].startswith(("https://", "http://"))
        assert source.get("evidence"), "Source evidence summary required"
        source_urls.add(source["url"])
    for field in ("first_release", "firmware"):
        item = record[field]
        value = item["date"]
        expected = {4: "year", 7: "month", 10: "day"}.get(len(value)) if value else "unknown"
        assert item["precision"] == expected, (key, field, "date precision mismatch")
        assert set(item["source_urls"]) <= source_urls, (key, field, "unregistered source")
        if value:
            assert lifecycle.bounds(value)[0] <= checked, (key, field, "future release")
            assert item["source_urls"], "Dates require sources"
    if record["firmware"]["status"] == "verified_latest":
        assert record["firmware"]["version"] and record["firmware"]["source_urls"]
    pitch = record.get("pitch")
    assert pitch is not None or not require_pitch, "Pitch evidence required for a combined audit"
    if pitch is not None:
        assert pitch["status"] in PITCH_LABELS
        for field in ("algorithms", "preset", "dsp"):
            assert isinstance(pitch[field], str) and pitch[field].strip(), (key, field)
        assert isinstance(pitch.get("notes", []), list)
        assert set(pitch["source_urls"]) <= source_urls
        if pitch["status"] != "unverified":
            assert pitch["source_urls"], "A pitch classification requires evidence"
        for measurement in pitch.get("measurements", []):
            assert measurement["basis"] in {"manufacturer", "owner_measurement", "independent_measurement"}
            assert measurement["denominator"] and measurement["configuration"] and measurement["algorithm"]
            assert set(measurement["source_urls"]) <= source_urls and measurement["source_urls"]
            assert isinstance(measurement["value"], (int, float)) and not isinstance(measurement["value"], bool)
            assert measurement["unit"] in {"percent", "blocks", "slots"}
            if measurement["unit"] == "percent":
                assert 0 <= measurement["value"] <= 100
    model_link(state, record)
    record["duration"] = date_span(record)
    return record


def measurement_text(item):
    value = str(item["value"]) + ("%" if item["unit"] == "percent" else " " + item["unit"])
    return (value + " of " + clean(item["denominator"]) + "; " + clean(item["basis"].replace("_", " "))
            + "; algorithm: " + clean(item["algorithm"]) + "; firmware: " + clean(item.get("firmware"))
            + "; configuration: " + clean(item["configuration"]) + ". " + links(item["source_urls"]))


def audit_rows(record, root_links=False):
    r, f = record["first_release"], record["firmware"]
    duration = record["duration"]["label"] if record.get("duration") else "Not calculable from verified dates"
    prefix = "" if root_links else "../"
    rows = [
        ("Firmware / first hardware release", lifecycle.release_text(record) + ". " + clean(r.get("note")) + " " + links(r["source_urls"], "launch")),
        ("Firmware / latest verification", lifecycle.firmware_text(record) + ". " + clean(f.get("note")) + " " + links(f["source_urls"], "firmware")),
        ("Firmware / release date", clean(f["date"]) + " (" + f["precision"] + " precision)"),
        ("Firmware / release-to-update duration", duration + "; observed release span, not continuous support or promised future updates."),
        ("Firmware / audit date", record["checked_date"] + f"; [firmware recap]({prefix}{FIRMWARE_PAGE})."),
    ]
    pitch = record.get("pitch")
    if pitch:
        rows += [
            ("Pitch / note handling", PITCH_LABELS[pitch["status"]] + ". " + clean(pitch["algorithms"]) + " " + links(pitch["source_urls"], "pitch")),
            ("Pitch / preset recall", clean(pitch["preset"])),
            ("Pitch / DSP resources", clean(pitch["dsp"])),
        ]
        rows += [("Pitch / DSP observation " + str(i), measurement_text(item)) for i, item in enumerate(pitch.get("measurements", []), 1)]
        if pitch.get("notes"):
            rows.append(("Pitch / qualifications", " ".join(clean(x) for x in pitch["notes"])))
        rows.append(("Pitch / comparison", f"[Polyphony, presets and DSP recap]({prefix}{PITCH_PAGE})."))
    return rows


def comparison_facts(state, key):
    record = state.get("firmware_lifecycle", {}).get("models", {}).get(key)
    if not record or record.get("audit_format") != FORMAT:
        return []
    path = model_link(state, record).split("#", 1)[0]
    return [{"field": field, "value": value, "source": path, "context": "Per-model firmware and pitch audit: " + key}
            for field, value in audit_rows(record, root_links=True)]


def render_record(record):
    key = record["model_key"]
    text = f"<!-- firmware-pitch:{key} begins -->\n### Firmware and pitch audit — {clean(key.replace('::', ' '))}\n\n"
    text += "| Field | Sourced finding |\n|---|---|\n"
    text += "\n".join(f"| {field} | {clean(value)} |" for field, value in audit_rows(record)) + "\n\n"
    if record.get("notes"):
        text += "\n\n".join(clean(note) for note in record["notes"]) + "\n\n"
    text += "Sources checked:\n\n"
    text += "\n".join(f"- [{clean(s.get('title') or s['url'])}]({s['url']}) — {clean(s['evidence'])} ({clean(s.get('access', 'opened'))})." for s in record["sources"]) + "\n\n"
    return text + f"<!-- firmware-pitch:{key} ends -->\n\n"


def section_location(text, anchor):
    matches = list(re.finditer(r"^## (.+)\n", text, re.M))
    slug = lambda s: re.sub(r"[^\w\- ]", "", s.lower().replace("`", "")).replace(" ", "-")
    selected = [(m.end(), matches[i + 1].start() if i + 1 < len(matches) else len(text))
                for i, m in enumerate(matches) if slug(m[1]) == anchor]
    assert len(selected) == 1, ("Canonical section missing or ambiguous", anchor)
    return selected[0]


def update_brand(text, record, link):
    key = record["model_key"]
    start, end = section_location(text, link.split("#", 1)[1])
    body = text[start:end]
    matches = [m for m in BLOCK.finditer(body) if m[1] == key]
    assert len(matches) <= 1, "Duplicate generated audit block"
    if matches:
        match = matches[0]
        body = body[:match.start()] + render_record(record) + body[match.end():]
    else:
        # Historical firmware-only text is retained; the dated combined block supersedes it.
        body = "\n" + render_record(record) + body.lstrip("\n")
    return text[:start] + body + text[end:]


def recap_header(state, title):
    audit = state["firmware_lifecycle"]
    records = audit["models"]
    active = inventory(state)
    firmware_count = len(active & set(records))
    pitch_count = sum(key in active and "pitch" in record for key, record in records.items())
    supplementary = len(set(records) - active)
    return (f"# {title}\n\n[Repository](README.md) · [Guitar](all-guitar.md) · [Bass](all-bass.md) · [Vocal](all-vocal.md)"
            f" · [Firmware]({FIRMWARE_PAGE}) · [Pitch shifting]({PITCH_PAGE})\n\n"
            f"**Checked through {audit['checked_date']}. {firmware_count}/{len(active)} active models have firmware audits; "
            f"{pitch_count}/{len(active)} have pitch audits; {supplementary} supplemental/archival records are separate from active counts.** "
            "Each model is updated individually. Audited records can retain unresolved fields; this is not a claim that every specification is verified.\n\n")


def render_firmware_page(state):
    records = state["firmware_lifecycle"]["models"]
    text = recap_header(state, "Firmware updates — release-to-update duration")
    text += ("## Reading the ranking\n\nDuration is the device-firmware release date minus the first hardware release date, using the stated announcement or shipping basis. "
             "Editors, drivers, updater apps, manual revisions and web crawl dates are not device-firmware releases. Beta firmware is identified in the model evidence.\n\n"
             "Exact elapsed days are divided by 365.2425. Month/year precision produces minimum–maximum bounds. "
             "Rows sort by the largest lower bound, then upper bound; overlapping intervals do not establish a strict order. Negative or overlapping release dates remain visible. "
             "The span is an observation, not continuous support, update frequency or a promised lifetime. Unknown, unavailable and documented non-updatable are distinct.\n\n")
    def table(keys):
        result = "| Model / complete evidence | First release / basis | Device firmware | Firmware release | Elapsed span | Sources |\n|---|---|---|---|---|---|\n"
        for key in keys:
            rec = records[key]
            label = clean(key.replace("::", " ")) + (" (" + rec["scope"] + ")" if key not in inventory(state) else "")
            result += f"| [{label}]({model_link(state, rec)}) | {clean(lifecycle.release_text(rec))} | {clean(lifecycle.firmware_text(rec))} | {clean(rec['firmware']['date'])} | {clean(rec['duration']['label'] if rec.get('duration') else 'Not calculable')} | {links(rec['first_release']['source_urls'], 'launch')} {links(rec['firmware']['source_urls'], 'firmware')} |\n"
        return result if keys else "No qualifying records verified yet.\n"
    ranked = [k for k, r in records.items() if r.get("duration") and r["duration"]["minimum_days"] >= 0]
    ranked.sort(key=lambda k: (-records[k]["duration"]["minimum_days"], -records[k]["duration"]["maximum_days"], k.casefold()))
    latest = [k for k in ranked if records[k]["firmware"]["status"] == "verified_latest"]
    historical = [k for k in ranked if k not in latest]
    unresolved = sorted(set(records) - set(ranked), key=str.casefold)
    text += "## Latest firmware verified — longest span first\n\n" + table(latest)
    text += "\n## Dated firmware located — current latest status unresolved\n\n" + table(historical)
    text += "\n## Unresolved spans and overlapping or pre-launch dates\n\n" + table(unresolved)
    pending = sorted(inventory(state) - set(records), key=str.casefold)
    text += "\n## Remaining firmware checks\n\n" + ("; ".join(clean(k.replace("::", " ")) for k in pending) + ".\n" if pending else "Every active model has an audit record; unresolved fields above remain unresolved.\n")
    return text


def render_pitch_page(state):
    records = state["firmware_lifecycle"]["models"]
    text = recap_header(state, "Pitch shifting — polyphony, presets and DSP resources")
    text += ("Polyphonic here concerns simultaneous input notes in the identified pitch algorithm. Stereo, two harmony voices, octave effects, synth polyphony and vocal pitch correction do not by themselves prove whole-chord transposition. "
             "Preset recall and the exact firmware/algorithm remain separate checks.\n\n"
             "DSP percentages require the measurement basis, processor/path denominator, firmware and effect-chain configuration. Published specifications and owner measurements remain labelled separately. "
             "A fixed block count is not a CPU percentage, and unpublished resource costs are not zero. Values across unlike processors or denominators are not directly comparable.\n\n")
    for status, label in PITCH_LABELS.items():
        keys = sorted((k for k, r in records.items() if r.get("pitch", {}).get("status") == status), key=str.casefold)
        text += f"## {label}\n\n"
        if not keys:
            text += "No records in this classification yet.\n\n"
            continue
        text += "| Model / complete evidence | Algorithm / note handling | Preset recall | DSP / resource constraints | Evidence |\n|---|---|---|---|---|\n"
        for key in keys:
            record, pitch = records[key], records[key]["pitch"]
            dsp = clean(pitch["dsp"])
            if pitch.get("measurements"):
                dsp += " " + " ".join(measurement_text(m) for m in pitch["measurements"])
            algorithm = clean(pitch["algorithms"])
            if pitch.get("notes"):
                algorithm += " " + " ".join(clean(x) for x in pitch["notes"])
            scope = " (" + record["scope"] + ")" if key not in inventory(state) else ""
            text += f"| [{clean(key.replace('::', ' '))}{scope}]({model_link(state, record)}) | {algorithm} | {clean(pitch['preset'])} | {clean(dsp)} | {links(pitch['source_urls'])}; checked {record['checked_date']} |\n"
        text += "\n"
    pending = sorted(inventory(state) - {k for k, r in records.items() if "pitch" in r}, key=str.casefold)
    text += "## Remaining pitch checks\n\n" + ("; ".join(clean(k.replace("::", " ")) for k in pending) + ".\n" if pending else "Every active model has a pitch audit; unresolved classifications remain explicit.\n")
    return text


def navigation(text):
    rows = {
        FIRMWARE_PAGE: "Device firmware, first hardware release dates and longest release-to-update spans; date precision and source gaps retained",
        PITCH_PAGE: "Pitch algorithms, polyphony, preset recall and documented DSP constraints; manufacturer claims and observations distinguished",
    }
    for page, description in rows.items():
        row = f"| **[{page}]({page})** | {description} |\n"
        pattern = re.compile(r"^\| \*\*\[" + re.escape(page) + r"\].*\n", re.M)
        if pattern.search(text):
            text = pattern.sub(lambda _: row, text)
        else:
            position = text.index("| **[MULTI-EFFECTS.md]")
            text = text[:position] + row + text[position:]
    return text


def apply_record(path):
    lifecycle.identity()
    state_path = ROOT / "research-state.json"
    state = json.loads(state_path.read_text())
    record = validate_record(json.loads(Path(path).read_text()), state)
    record["audit_format"] = FORMAT
    key = record["model_key"]
    audit = state.setdefault("firmware_lifecycle", {"models": {}, "scope": sorted(inventory(state))})
    assert set(audit["scope"]) == inventory(state), "Inventory changed; review scope before applying"
    previous = audit["models"].get(key)
    if previous:
        history = copy.deepcopy(previous.get("prior_audits", []))
        retained = {k: copy.deepcopy(v) for k, v in previous.items() if k != "prior_audits"}
        replacement = {k: v for k, v in record.items() if k != "prior_audits"}
        if retained != replacement and retained not in history:
            history.append(retained)
        if history:
            record["prior_audits"] = history
    audit["models"][key] = record
    audit["format_version"] = FORMAT
    audit["checked_date"] = max(r["checked_date"] for r in audit["models"].values())
    audit["next_models"] = sorted(inventory(state) - set(audit["models"]), key=str.casefold)
    audit["pitch_next_models"] = sorted(inventory(state) - {k for k, r in audit["models"].items() if "pitch" in r}, key=str.casefold)
    audit["completed_model_count"] = len(inventory(state) & set(audit["models"]))
    audit["pitch_completed_model_count"] = len(inventory(state)) - len(audit["pitch_next_models"])
    audit["supplemental_model_count"] = len(set(audit["models"]) - inventory(state))
    audit["last_model"] = key
    audit["last_commit_parent"] = lifecycle.git("rev-parse", "HEAD")
    audit["status"] = "all_models_checked_with_explicit_gaps" if not audit["next_models"] and not audit["pitch_next_models"] else "in_progress"
    link = model_link(state, record)
    brand = ROOT / link.split("#", 1)[0]
    new_brand = update_brand(brand.read_text(), record, link)
    # Validate render locations before any writes; mutations are one model only.
    assert render_record(record).strip() in new_brand
    brand.write_text(new_brand)
    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")
    (ROOT / FIRMWARE_PAGE).write_text(render_firmware_page(state))
    (ROOT / PITCH_PAGE).write_text(render_pitch_page(state))
    (ROOT / "README.md").write_text(navigation((ROOT / "README.md").read_text()))
    import comparison_views as cv
    for name, content in cv.make_plan(persist=False)["outputs"].items():
        if not (ROOT / name).exists() or (ROOT / name).read_text() != content:
            (ROOT / name).write_text(content)
    subprocess.run(["git", "diff", "--check"], cwd=ROOT, check=True)
    print(json.dumps({"model": key, "firmware_models": audit["completed_model_count"], "pitch_models": audit["pitch_completed_model_count"], "supplemental_models": audit["supplemental_model_count"], "commit_created": False}))


def verify():
    lifecycle.identity()
    state = json.loads((ROOT / "research-state.json").read_text())
    audit = state["firmware_lifecycle"]
    assert set(audit["scope"]) == inventory(state)
    for key, record in audit["models"].items():
        assert key == record["model_key"]
        checked = validate_record(copy.deepcopy(record), state, require_pitch=record.get("audit_format") == FORMAT)
        expected = checked["duration"]
        if record.get("audit_format") == FORMAT:
            assert record["duration"] == expected, (key, "Stale duration")
            path, anchor = model_link(state, record).split("#", 1)
            text = (ROOT / path).read_text()
            start, end = section_location(text, anchor)
            matches = [m for m in BLOCK.finditer(text) if m[1] == key]
            assert len(matches) == 1 and start <= matches[0].start() < matches[0].end() <= end, (key, "Wrong audit owner")
            assert matches[0][0].strip() == render_record(record).strip(), (key, "Stale brand audit")
    assert audit["completed_model_count"] == len(inventory(state) & set(audit["models"]))
    assert set(audit["next_models"]) == inventory(state) - set(audit["models"])
    assert set(audit["pitch_next_models"]) == inventory(state) - {k for k, r in audit["models"].items() if "pitch" in r}
    assert audit["pitch_completed_model_count"] == len(inventory(state)) - len(audit["pitch_next_models"])
    assert audit["supplemental_model_count"] == len(set(audit["models"]) - inventory(state))
    assert (ROOT / FIRMWARE_PAGE).read_text() == render_firmware_page(state)
    assert (ROOT / PITCH_PAGE).read_text() == render_pitch_page(state)
    assert (ROOT / "README.md").read_text() == navigation((ROOT / "README.md").read_text())
    import comparison_views as cv
    plan = cv.make_plan(persist=False)
    for path, content in plan["outputs"].items():
        assert (ROOT / path).read_text() == content, (path, "Stale generated comparison")
    for key, row in plan["records"].items():
        actual = [f for f in row["facts"] if f["context"].startswith("Per-model firmware and pitch audit:")]
        assert actual == comparison_facts(state, key), (key, "Audit facts leaked between models")
    print(f"PASS: {len(audit['models'])} firmware records; {audit['pitch_completed_model_count']} active pitch records; dates, sources, recap ranking and exact-model extraction")


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "apply":
        apply_record(sys.argv[2])
    elif len(sys.argv) == 2 and sys.argv[1] == "verify":
        verify()
    else:
        raise SystemExit("Use apply <one-model-evidence.json> or verify")
