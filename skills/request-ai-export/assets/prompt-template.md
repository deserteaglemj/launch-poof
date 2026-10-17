I want to share my {{TOPIC}} AI setup with my friend {{RECIPIENT_NAME}} so we can combine skills. Package it for me. Keep it quick: do the work yourself and only stop where this says to.

1. FIND everything I or you set up for {{TOPIC}} ({{SEARCH_WORDS}}):
- Skills: folders with a SKILL.md in ~/.claude/skills, ~/.agents/skills, ~/.codex/skills, ~/.cursor/skills, ~/.windsurf/skills, ~/.gemini/skills, and the same folders inside my {{TOPIC}} project folders
- Plugins: {{TOPIC}}-related ones in ~/.claude/plugins or any other AI tool's plugin folder (include their skills, agents, commands and hooks)
- Rules: CLAUDE.md, AGENTS.md, GEMINI.md, .cursor/rules, .cursorrules, .windsurfrules, .github/copilot-instructions.md in my {{TOPIC}} projects, plus only the {{TOPIC}} parts of my global ones
- MCP setup: names and launch commands of {{TOPIC}}-related MCP servers, no keys
- Reusable prompts, checklists, templates, scripts, notes and lessons learned about {{TOPIC}} with AI
{{EXTRA_ITEMS}}
Skip full project source code, node_modules, .git, caches, and any file over 5 MB.

2. CLEAN: copy, never move. In the copies, replace API keys, tokens, passwords, session cookies, webhook URLs and personal emails or phone numbers with [REDACTED]. Never include .env files, *.key, *.pem or credential files.

3. PACKAGE: put the copies in one folder named {{KIT_SLUG}}-<my first name>-<today's date>, each skill as its own folder. Add a README.md with one line per item: what it is, which AI tool it's for, where it came from, and any setup {{RECIPIENT_NAME}} needs.

4. CHECK WITH ME: show me the README list and what you redacted, then ask "Good to send?" Wait for my yes.

5. SEND: after my yes, zip the folder to my Desktop and open its location (Mac: open -R <zip path>, Windows: explorer /select,<zip path>). Then tell me: "Drag this zip into your {{CHANNEL}} with {{RECIPIENT_NAME}}, or attach it to an email to {{EMAIL}}." If you have an email tool connected, offer to send it there for me. If the zip is over 25 MB, tell me and suggest AirDrop or a Google Drive link instead.

IF YOU CAN'T ACCESS MY FILES (like ChatGPT or Claude in a browser): instead write ONE code block I can copy, starting with "{{KIT_TITLE}} FROM <my name>". Put in it my custom instructions, your saved memories about my {{TOPIC}} work, any project or GPT instructions and knowledge files you can see, and your best write-up of the {{TOPIC}} workflows, prompts and lessons we've used, using the README format above. No secrets. If it's too long for one message, split it into numbered parts. Then tell me: "Copy this and paste it to {{RECIPIENT_NAME}}."
