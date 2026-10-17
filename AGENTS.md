# AGENTS.md

launch-poof is a Claude Code and Codex plugin with one skill, request-ai-export: it writes a text and a copy-paste prompt that gets a friend's AI to package and send their skills on a topic.

## Develop

No dependencies. Python 3.9+ standard library only. CI runs exactly:

```bash
python3 -m unittest discover -s tests -v
```

Before a release, also validate the plugin:

```bash
claude plugin validate --strict .
```

## Layout

- `skills/request-ai-export/SKILL.md`: the skill (frontmatter `name` must match the folder).
- `skills/request-ai-export/assets/prompt-template.md`: the prompt with double-brace placeholder fields; every placeholder must be documented in SKILL.md.
- `examples/roblox-game-dev.md`: the template filled with the sample values in `tests/test_skill.py`; regenerate it when the template changes.
- `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `.codex-plugin/plugin.json`: keep `version` identical in all three and in CHANGELOG.md.
- `docs/`: GitHub Pages landing page and launch material.

## Rules

- No em dashes, home paths or personal emails in shipped files (tests check this).
- Claims in README need evidence in `evals/RESULTS.md` or a linked source.
