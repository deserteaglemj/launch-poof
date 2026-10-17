# Example: asking a friend for their Roblox game dev setup

Made by running the skill with the sample values in `tests/test_skill.py` (friend: Alex, recipient: Sam). The test suite checks that the prompt below is exactly the filled template.

## Text to send Alex (separate bubbles)

```
Easiest way, copy the prompt I'm about to send and paste it into whatever AI u build with
```

```
It finds all ur roblox skills, plugins, rules and notes, strips out any keys or passwords, and zips it up
```

```
Then just drag the zip in here or email it to sam@example.com
```

```
If ur AI can't touch files it'll give u one big block instead, just paste that here
```

## Prompt for Alex's AI

```
I want to share my Roblox game dev AI setup with my friend Sam so we can combine skills. Package it for me. Keep it quick: do the work yourself and only stop where this says to.

1. FIND everything I or you set up for Roblox game dev (Roblox, Luau, Roblox Studio, Rojo, obby):
- Skills: folders with a SKILL.md in ~/.claude/skills, ~/.agents/skills, ~/.codex/skills, ~/.cursor/skills, ~/.windsurf/skills, ~/.gemini/skills, and the same folders inside my Roblox game dev project folders
- Plugins: Roblox game dev-related ones in ~/.claude/plugins or any other AI tool's plugin folder (include their skills, agents, commands and hooks)
- Rules: CLAUDE.md, AGENTS.md, GEMINI.md, .cursor/rules, .cursorrules, .windsurfrules, .github/copilot-instructions.md in my Roblox game dev projects, plus only the Roblox game dev parts of my global ones
- MCP setup: names and launch commands of Roblox game dev-related MCP servers, no keys
- Reusable prompts, checklists, templates, scripts, notes and lessons learned about Roblox game dev with AI
- Roblox Studio plugins or reusable Luau modules I wrote myself
Skip full project source code, node_modules, .git, caches, and any file over 5 MB.

2. CLEAN: copy, never move. In the copies, replace API keys, tokens, passwords, session cookies, webhook URLs and personal emails or phone numbers with [REDACTED]. Never include .env files, *.key, *.pem or credential files.

3. PACKAGE: put the copies in one folder named roblox-ai-kit-<my first name>-<today's date>, each skill as its own folder. Add a README.md with one line per item: what it is, which AI tool it's for, where it came from, and any setup Sam needs.

4. CHECK WITH ME: show me the README list and what you redacted, then ask "Good to send?" Wait for my yes.

5. SEND: after my yes, zip the folder to my Desktop and open its location (Mac: open -R <zip path>, Windows: explorer /select,<zip path>). Then tell me: "Drag this zip into your text thread with Sam, or attach it to an email to sam@example.com." If you have an email tool connected, offer to send it there for me. If the zip is over 25 MB, tell me and suggest AirDrop or a Google Drive link instead.

IF YOU CAN'T ACCESS MY FILES (like ChatGPT or Claude in a browser): instead write ONE code block I can copy, starting with "ROBLOX AI KIT FROM <my name>". Put in it my custom instructions, your saved memories about my Roblox game dev work, any project or GPT instructions and knowledge files you can see, and your best write-up of the Roblox game dev workflows, prompts and lessons we've used, using the README format above. No secrets. If it's too long for one message, split it into numbered parts. Then tell me: "Copy this and paste it to Sam."
```
