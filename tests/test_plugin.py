import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST_DIR = ROOT / ".claude-plugin"


def load(name):
    return json.loads((MANIFEST_DIR / name).read_text(encoding="utf-8"))


class PluginManifestTests(unittest.TestCase):
    def test_plugin_json(self):
        data = load("plugin.json")
        self.assertEqual(data["name"], "viet-writing")
        self.assertTrue(data.get("description"))
        self.assertTrue(data.get("version"))

    def test_marketplace_json(self):
        data = load("marketplace.json")
        self.assertTrue(data.get("name"))
        self.assertTrue(data["owner"]["name"])
        self.assertEqual(len(data["plugins"]), 1)
        plugin = data["plugins"][0]
        self.assertEqual(plugin["name"], "viet-writing")
        self.assertEqual(plugin["source"], "./")


if __name__ == "__main__":
    unittest.main()
