"""Structural checks for the request-ai-export skill. Run: python3 -m unittest discover -s tests -v"""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skills" / "request-ai-export"
SKILL = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
TEMPLATE = (SKILL_DIR / "assets" / "prompt-template.md").read_text(encoding="utf-8")
EXAMPLE = ROOT / "examples" / "roblox-game-dev.md"

# Sample values used to build examples/roblox-game-dev.md from the template.
EXAMPLE_VALUES = {
    "TOPIC": "Roblox game dev",
    "SEARCH_WORDS": "Roblox, Luau, Roblox Studio, Rojo, obby",
    "RECIPIENT_NAME": "Sam",
    "EXTRA_ITEMS": "- Roblox Studio plugins or reusable Luau modules I wrote myself",
    "KIT_SLUG": "roblox-ai-kit",
    "KIT_TITLE": "ROBLOX AI KIT",
    "CHANNEL": "text thread",
    "EMAIL": "sam@example.com",
}


def fill(template, values):
    return re.sub(r"\{\{([A-Z_]+)\}\}", lambda m: values[m.group(1)], template)


def frontmatter(text):
    block = text.split("---")[1]
    return dict(line.split(": ", 1) for line in block.strip().splitlines())


class SkillTests(unittest.TestCase):
    def test_frontmatter(self):
        fm = frontmatter(SKILL)
        self.assertEqual(fm["name"], SKILL_DIR.name)
        self.assertLess(len(fm["description"]), 1024)

    def test_every_placeholder_is_documented(self):
        used = set(re.findall(r"\{\{([A-Z_]+)\}\}", TEMPLATE))
        self.assertEqual(used, set(EXAMPLE_VALUES))
        for name in used:
            self.assertIn("{{%s}}" % name, SKILL, name)

    def test_fill_leaves_no_placeholders(self):
        self.assertNotIn("{{", fill(TEMPLATE, EXAMPLE_VALUES))

    def test_prompt_keeps_safety_steps(self):
        for phrase in ["1. FIND", "2. CLEAN", "copy, never move", "[REDACTED]", "3. PACKAGE",
                       "4. CHECK WITH ME", "Wait for my yes", "5. SEND", "IF YOU CAN'T ACCESS MY FILES"]:
            self.assertIn(phrase, TEMPLATE, phrase)

    def test_example_is_the_filled_template(self):
        example = EXAMPLE.read_text(encoding="utf-8")
        self.assertIn(fill(TEMPLATE, EXAMPLE_VALUES).strip(), example)

    def test_no_private_data_or_em_dashes(self):
        for path in [*SKILL_DIR.rglob("*.md"), EXAMPLE, ROOT / "README.md"]:
            text = path.read_text(encoding="utf-8")
            self.assertNotIn(chr(0x2014), text, path)  # em dash
            self.assertNotRegex(text, r"/Users/\w|/home/\w", path)
            self.assertNotRegex(text, r"@(gmail|yahoo|outlook|icloud)\.com", path)

    def test_versions_in_sync(self):
        claude = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text())
        codex = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text())
        market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text())
        changelog = (ROOT / "CHANGELOG.md").read_text()
        self.assertEqual(claude["version"], codex["version"])
        self.assertEqual(claude["version"], market["plugins"][0]["version"])
        self.assertIn("## [%s]" % claude["version"], changelog)


if __name__ == "__main__":
    unittest.main()
