import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "skills" / "ui-ux-workflow" / "scripts" / "check_tokens.py"
spec = importlib.util.spec_from_file_location("check_tokens", MODULE)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class TokenTests(unittest.TestCase):
    def setUp(self):
        self.base = json.loads((checker.TOKEN_DIR / "base.tokens.json").read_text(encoding="utf-8-sig"))
        self.alias = json.loads((checker.TOKEN_DIR / "alias.tokens.json").read_text(encoding="utf-8-sig"))

    def test_bundled_aliases_resolve(self):
        result = checker.audit(self.base, self.alias)
        self.assertTrue(result["ok"], result["errors"])
        self.assertGreater(result["base_count"], result["alias_count"])

    def test_missing_target_is_reported(self):
        del self.base["Color"]["neutral"]["900"]
        result = checker.audit(self.base, self.alias)
        self.assertFalse(result["ok"])
        self.assertTrue(any("target không có" in e for e in result["errors"]))

    def test_different_resolved_color_is_reported(self):
        token = self.alias["color"]["text"]["heading"]["900"]
        token["$value"] = copy.deepcopy(self.base["Color"]["neutral"]["800"]["$value"])
        result = checker.audit(self.base, self.alias)
        self.assertFalse(result["ok"])
        self.assertTrue(any("resolve khác" in e for e in result["errors"]))

    def test_invalid_color_channels_are_reported(self):
        self.base["Color"]["Primary"]["500"]["$value"]["components"][0] = 2
        self.assertFalse(checker.audit(self.base, self.alias)["ok"])

    def test_alias_type_mismatch_is_reported(self):
        self.alias["color"]["text"]["heading"]["900"]["$type"] = "number"
        result = checker.audit(self.base, self.alias)
        self.assertFalse(result["ok"])
        self.assertTrue(any("kiểu khác" in e for e in result["errors"]))


if __name__ == "__main__":
    unittest.main()
