Status: draft, not posted or submitted. Every step needs the owner's approval.

Needs: Showcase flair on r/ClaudeAI, account in good standing, re-read rules the day you post. Reword for r/ClaudeCode the next day.

**Title:** I made a skill that gets a friend's AI to package and send you their skills

A friend told me he had a bunch of Roblox dev skills for his AI. Getting them over meant him digging through ~/.claude/skills, Cursor rules, MCP configs and notes, then remembering to strip API keys. So I made a plugin for it.

You ask your agent for a friend's setup on a topic. It writes a short text and one prompt. The friend pastes the prompt into whatever AI they use; it finds their skills, plugins, rules and notes on that topic, replaces secrets with [REDACTED], shows them the list, waits for a yes, and zips it. Browser-only AIs give one copy-paste block instead.

When the zip arrives, the skill unzips it into its own folder, runs nothing from it and vets each skill before you install anything.

Limitation: I've tested the files (7 structural tests), not how well every AI follows the prompt. If you try it, I'd like to hear where it misses files.

Repo (MIT): https://github.com/deserteaglemj/launch-poof
