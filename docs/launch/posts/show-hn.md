Status: draft, not posted or submitted. Every step needs the owner's approval.

# Show HN outline (write the final text by hand)

Title idea: Show HN: launch-poof, get a friend's AI to package and send you their agent skills

Facts to use:
- I built it after a friend said he had Roblox dev skills for his AI and I had no easy way to get them.
- Your agent writes a short text and one prompt. The friend pastes the prompt into their AI (Claude Code, Codex, Cursor, Windsurf, Gemini CLI).
- Their AI finds skills, plugins, rules files, MCP setup and notes on the topic, replaces secrets with [REDACTED], waits for one "yes", zips it and tells them where to drop it.
- Chat-only AIs (ChatGPT, claude.ai) output one copy-paste block instead.
- The receiving side treats the kit as untrusted: own folder, run nothing, vet before install.
- Proof: 7 structural tests pass in CI (evals/RESULTS.md). Limitation: no end-to-end runs in other people's AIs measured yet.
- MIT, no dependencies, no network calls.

Link: https://github.com/deserteaglemj/launch-poof
