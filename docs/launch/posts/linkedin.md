Status: draft, not posted or submitted. Every step needs the owner's approval.

Needs: social preview image attached.

Sharing what you've built with AI agents is harder than it should be. Skills, rules files, MCP setups and notes live in different folders for every tool, and they often hold API keys.

I built launch-poof, an open-source plugin for Claude Code and Codex. You ask your agent for a colleague's setup on a topic; it writes a short message and one prompt. They paste the prompt into their own AI, which finds the files, replaces secrets with [REDACTED], asks them to confirm, and zips the kit. On your side, the kit is treated as untrusted and vetted before anything gets installed.

It's early: the files are tested (7 structural tests), but how well each AI follows the prompt hasn't been measured yet. Feedback welcome.

https://github.com/deserteaglemj/launch-poof
