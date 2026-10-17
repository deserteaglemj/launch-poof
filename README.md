# launch-poof

Get someone's AI setup into your hands with almost no work on their end. Ask your agent for an export from a friend, and it writes:

1. A short text for you to send them.
2. A prompt they paste into their own AI (Claude Code, Codex, Cursor, Windsurf, Gemini CLI, ChatGPT, claude.ai).

Their AI finds every skill, plugin, rules file, MCP setup, prompt and note on the topic, swaps secrets for `[REDACTED]`, builds a zip with a README, waits for their one "yes", and tells them where to drop it. Browser-only AIs give a single copy-paste block instead.

When the export comes back, the skill treats it as untrusted: it unzips it into its own folder, runs nothing from it, and has every skill vetted before anything gets installed.

## Install (Claude Code)

```bash
claude plugin marketplace add deserteaglemj/launch-poof
```

```bash
claude plugin install launch-poof@launch-poof
```

Then ask: "get Stxrmz to send me his Roblox skills", or run `/launch-poof:request-ai-export`.

## Other agents

`skills/request-ai-export/` is a standard SKILL.md folder. Copy it into `~/.agents/skills/`, `~/.codex/skills/` or `~/.cursor/skills/`.

## Customize

- Delivery email and voice rules live in `skills/request-ai-export/SKILL.md`.
- The prompt they paste is `skills/request-ai-export/assets/prompt-template.md`.

MIT license.
