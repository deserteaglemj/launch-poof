Status: draft, not posted or submitted. Every step needs the owner's approval.

Needs: Dev.to account, cover image (social preview), tags: ai, claude, opensource, productivity.

# How I get friends' AI agent setups without making them do the work

A friend said he had Roblox dev skills for his AI. To send them, he'd have to find them across ~/.claude/skills, ~/.cursor, AGENTS.md files and MCP configs, and strip any keys. Most people won't.

## The idea

Make their AI do it. launch-poof is a plugin with one skill. You ask your agent for a friend's setup on a topic, and it writes:

1. a short text for you to send, and
2. a prompt for the friend's AI with five steps: FIND, CLEAN (copy, never move; replace secrets with [REDACTED]), PACKAGE (folder plus README), CHECK WITH ME (wait for a yes), SEND (zip to the Desktop and say where to drop it).

If their AI runs in a browser and can't read files, it writes one copy-paste block instead.

## Receiving safely

A kit from another person is untrusted. The skill unzips it into its own folder, runs nothing, reads every file for injected instructions, install scripts and leftover secrets, and vets each skill before install.

## What's proven

7 structural tests pass in CI (placeholders documented, prompt keeps its safety steps, example matches the template, no personal data in shipped files). Not proven: how well each AI follows the prompt. That's next.

Repo (MIT): https://github.com/deserteaglemj/launch-poof
