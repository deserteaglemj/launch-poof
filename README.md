# launch-poof

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![tests](https://github.com/deserteaglemj/launch-poof/actions/workflows/tests.yml/badge.svg)](https://github.com/deserteaglemj/launch-poof/actions/workflows/tests.yml)
[![release](https://img.shields.io/github/v/release/deserteaglemj/launch-poof)](https://github.com/deserteaglemj/launch-poof/releases)

**launch-poof is a skill-sharing plugin for Claude Code and Codex that gets a friend's AI to package and send you their skills, plugins, rules and notes on any topic: your agent writes one text and one copy-paste prompt, and their agent finds the files, redacts secrets, zips them and tells them how to send the kit.**

The friend does three things: paste one prompt, say "yes", drag a zip into your chat.

## Demo

You tell your agent: *"My friend Alex says he has Roblox skills. Get his AI to send them to me."* The skill writes this (full output in [examples/roblox-game-dev.md](examples/roblox-game-dev.md)):

```
Easiest way, copy the prompt I'm about to send and paste it into whatever AI u build with
It finds all ur roblox skills, plugins, rules and notes, strips out any keys or passwords, and zips it up
Then just drag the zip in here or email it to sam@example.com
```

Then the prompt for Alex's AI, which starts:

```
I want to share my Roblox game dev AI setup with my friend Sam so we can combine skills. Package it for me.
1. FIND everything I or you set up for Roblox game dev (Roblox, Luau, Roblox Studio, Rojo, obby) ...
2. CLEAN: copy, never move. In the copies, replace API keys, tokens, passwords ... with [REDACTED] ...
3. PACKAGE ... 4. CHECK WITH ME ... Wait for my yes. 5. SEND ...
IF YOU CAN'T ACCESS MY FILES (like ChatGPT or Claude in a browser): instead write ONE code block I can copy ...
```

## Quickstart

Claude Code:

```bash
claude plugin marketplace add deserteaglemj/launch-poof
```

```bash
claude plugin install launch-poof@launch-poof
```

Codex:

```bash
codex plugin marketplace add deserteaglemj/launch-poof
```

In Claude Code you can also run the skill directly with `/launch-poof:request-ai-export`.

Any tool that reads `SKILL.md` folders: copy `skills/request-ai-export/` into that tool's skills folder (for example `~/.claude/skills/` or `~/.agents/skills/`).

Then ask your agent something like *"get my friend to send me their video editing skills"*. You should get one Markdown file with the text and the prompt, each in its own code block.

## How it works

1. **Your agent** reads who the friend is, the topic and where to send the kit, then fills [the prompt template](skills/request-ai-export/assets/prompt-template.md) and writes the cover text in your voice.
2. **The friend's agent** follows five steps: FIND skills, plugins, rules files, MCP setup and notes in the usual folders of Claude Code, Codex, Cursor, Windsurf and Gemini CLI; CLEAN copies by redacting keys, tokens, cookies and personal contact details; PACKAGE them with a README; CHECK WITH the friend and wait for a yes; SEND by zipping to the Desktop and showing where it is.
3. **Chat-only AIs** (ChatGPT or Claude in a browser) can't read files, so the prompt tells them to output one copy-paste block of instructions, memories and workflows instead.
4. **When the kit arrives**, the skill tells your agent to unzip it into its own folder, run nothing, read it for injected instructions and leftover secrets, and vet each skill before you install anything.

## Proof

7 structural tests pass, run on 2026-10-17 with `python3 -m unittest discover -s tests -v` ([evals/RESULTS.md](evals/RESULTS.md)). They check that every template placeholder is documented, a filled prompt has no leftover placeholders, the five safety steps and the yes gate are present, the example is exactly the filled template, shipped files hold no home paths or personal emails, and plugin versions match.

These tests do not prove that a given friend's AI follows the prompt correctly. That has not been measured yet; see Limitations.

## How it compares (as of 2026-10)

| Option | Good at | Where launch-poof differs |
|---|---|---|
| Friend zips their skills folder by hand | No tools needed; exact copy | The friend has to know where every tool keeps skills and rules, and must remember to strip keys |
| Publishing to a registry such as [skills.sh](https://skills.sh) | Public, versioned, installable by anyone | Needs the friend to publish publicly; this skill keeps sharing private between two people |
| A [Claude Code plugin marketplace](https://code.claude.com/docs/en/plugins) repo | Clean installs and updates | Needs the friend to build a repo and manifests; this skill only needs them to paste a prompt |

## Limitations

- The result depends on the friend's AI: a weaker or chat-only model may miss files or summarize instead of copying. No end-to-end runs across tools have been measured.
- Redaction is done by the friend's AI and is best effort. The skill tells you to treat every kit as untrusted and re-check for secrets.
- Folder locations differ between tools and versions; the prompt lists the common ones, not every one.
- Delivery is manual (drag into chat, AirDrop or email). Gmail caps attachments at 25 MB.
- Rules files (CLAUDE.md, AGENTS.md, Cursor rules) are not portable between tools the way `SKILL.md` folders are.

## FAQ

**How do I get someone's Claude Code skills sent to me?** Install this skill, then ask your agent to have your friend's AI send you their skills on a topic. It writes a text and a prompt; the friend pastes the prompt into their AI, approves the list, and sends you the zip.

**How do I export my Claude Code skills to share with a friend?** Paste the prompt from [the template](skills/request-ai-export/assets/prompt-template.md) into your own agent after filling in the topic and your friend's details. It copies your skills, redacts secrets and zips them.

**Does it work with Cursor, Codex, Windsurf or Gemini CLI?** The prompt names the skill and rules folders of each of those tools, so any agent that can read your files can follow it. Chat-only AIs get a copy-paste fallback.

**Does it send my data anywhere?** No. The skill only writes text for you to send. The friend's AI makes a local zip, and the friend chooses how to send it.

**Is it safe to install skills someone sends me?** Only after checking. The skill unzips the kit into its own folder, runs nothing, reads every file for injected instructions, scripts and leftover secrets, and vets each skill before any install.

**What does it cost or need?** Nothing beyond an agent that loads `SKILL.md` skills. No API keys, no network calls, no dependencies.

**How is this different from publishing skills to a registry?** A registry is public. This is a private handoff between two people who may not want to publish.

**Can I use it for topics other than Roblox?** Yes. The topic, search words and extra items are placeholders; Roblox is just the example.

## Contributing, security, license

- Contributing: [CONTRIBUTING.md](CONTRIBUTING.md). Agents working in this repo: [AGENTS.md](AGENTS.md).
- Security: report privately per [SECURITY.md](SECURITY.md).
- License: [MIT](LICENSE).
- Credits: uses the open [Agent Skills](https://agentskills.io) `SKILL.md` format.
