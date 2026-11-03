"""Regression checks for duplicate canonical brand sections."""
import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.dont_write_bytecode = True
import research_tools as research


class CanonicalSectionsTest(unittest.TestCase):
    def verify_fixture(self, body):
        with tempfile.TemporaryDirectory(prefix="instrumentfx-verifier-") as directory:
            root = Path(directory)
            (root / "brand").mkdir()
            (root / "brand/TEST.md").write_text(body)
            state = {"cursor": {"model": "Model", "task": "Continue"},
                     "inventory_by_brand": {"TEST": ["Model", "Model Lite"]},
                     "active_model_count": 2, "canonical_root_model_count": 2,
                     "legacy_only_model_count": 0, "excluded_models": [],
                     "root_brand_content": {"brand/TEST.md": ["Model", "Model Lite"]}}
            (root / "research-state.json").write_text(json.dumps(state))
            with patch.object(research, "ROOT", root), \
                 patch.object(research, "identity"), \
                 patch.object(research, "git", return_value=""), \
                 contextlib.redirect_stdout(io.StringIO()):
                research.verify()

    def test_distinct_models_and_repeated_subsections(self):
        self.verify_fixture("## Model\n\n### Sources\nEvidence\n\n## Model Lite\n\n### Sources\nOther evidence\n")

    def test_duplicate_model_is_rejected(self):
        body = "## Model\nFirst evidence\n## Model Lite\nOther model\n## Model\nDuplicate evidence\n"
        with self.assertRaisesRegex(AssertionError, "TEST.md.*duplicate.*Model"):
            self.verify_fixture(body)

    def test_duplicated_document_is_rejected(self):
        body = "## Model\nEvidence\n## Model Lite\nOther evidence\n"
        with self.assertRaisesRegex(AssertionError, "TEST.md.*duplicate"):
            self.verify_fixture(body + body)


if __name__ == "__main__":
    unittest.main()
