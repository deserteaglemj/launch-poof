# launch-poof launch plan

Status: draft, not posted or submitted. Every step needs the owner's approval.

## Readiness gate

- Audit score on 2026-10-17: 94.4/100. Only required failure: `hygiene-history` (the first commit's author email). Non-required failure: `no-placeholders`, which flags the skill's intentional template fields.
- Open: rewrite the first commit's author email to the noreply address (owner step 1 below), push, make public, enable Pages, upload the social preview, create the v0.1.0 release.
- Unproven until after launch: CI on GitHub (runs on first push), Pages rendering, search and AI indexing (days).
- Honest gap to mention everywhere: no end-to-end runs of the prompt in other people's AIs have been measured yet.

## Sequence (times Central, CDT; ET in brackets)

| Day | Date | Channel | Time | Owner action | Needs |
|---|---|---|---|---|---|
| 0 | Mon 2026-10-19 | GitHub | any | Run owner steps 1 to 6 below | gh signed in |
| 0 | Mon 2026-10-19 | Claude plugin directory | after Pages is live | Submit from claude.ai/directory/manage | Public repo |
| 1 | Tue 2026-10-20 | Show HN | 8:00 AM (9:00 AM ET) | Post by hand from the outline, stay 2 hours to reply | HN account |
| 1 | Tue 2026-10-20 | X, LinkedIn, Bluesky | 11:00 AM (12:00 PM ET) | Post drafts, link the repo | Social preview image |
| 2 | Wed 2026-10-21 | r/ClaudeAI | 9:00 AM (10:00 AM ET) | Post draft, reply to comments | Check rules that day |
| 3 | Thu 2026-10-22 | r/ClaudeCode | 9:00 AM (10:00 AM ET) | Post reworded draft | Check rules that day |
| 4 | Fri 2026-10-23 | Dev.to | any | Publish article | Dev.to account |
| 5 to 7 | 2026-10-24 to 26 | Discord or Slack | any | Share in allowed showcase channels | Membership |
| 14+ | 2026-11-02 onward | awesome-claude-code, newsletters | any | Submit if age and star rules are met | Repo 14+ days old |

## Channels

### Show HN
Fits: a free open-source tool people can try in two commands. Write the final text by hand (HN asks for that); outline in [posts/show-hn.md](posts/show-hn.md).

### Reddit
r/ClaudeAI (Showcase flair, may remove very new accounts), then r/ClaudeCode a day later with different wording. r/SideProject only if the first two go well. Re-read each sidebar the day you post. Draft: [posts/reddit.md](posts/reddit.md).

### X, Bluesky, LinkedIn
Same facts, platform length. Drafts: [posts/x.md](posts/x.md), [posts/bluesky.md](posts/bluesky.md), [posts/linkedin.md](posts/linkedin.md).

### Dev.to
Short article on why sharing agent setups is hard and how the prompt handles it. Draft: [posts/devto.md](posts/devto.md).

### Discord and Slack
Only in channels that allow sharing projects (for example a showcase channel in Claude developer communities). Draft: [posts/discord.md](posts/discord.md).

### Plugin and skill directories
Claude plugin directory first (review takes days). Codex: no confirmed official directory; users install with `codex plugin marketplace add`. skills.sh and claude-plugins.dev: check each site's submission route before submitting. Draft listing text: [posts/directories.md](posts/directories.md).

### Awesome lists
awesome-claude-code takes web-form submissions only and its bot closes resources under 14 days old or under 100 stars, so wait until day 14 and check stars.

### Newsletters
Day 14+, only with real traction to report (stars, installs, feedback). No draft yet.

### Skipped
- Product Hunt: a single small skill with no UI is a weak fit, and a launch there needs a full day present. Revisit if the plugin grows.
- r/programming and r/opensource: strict self-promotion rules; a prompt-only tool is unlikely to fit.

## Owner approval commands (in order)

See the session report for the exact list; it is repeated here so the plan stands alone.

```bash
git bundle create ../launch-poof-before-rewrite.bundle --all
```

```bash
git rebase -r --root --exec 'git commit --amend --no-edit --reset-author'
```

```bash
gh repo create deserteaglemj/launch-poof --public --source . --push
```

```bash
gh repo edit deserteaglemj/launch-poof --description "Skill-sharing plugin for Claude Code and Codex: get a friend's AI to package and send you their skills, plugins, rules and notes on any topic. One text, one prompt, one zip, secrets redacted." --homepage "https://deserteaglemj.github.io/launch-poof/" --add-topic claude-code --add-topic claude-code-plugin --add-topic codex --add-topic agent-skills --add-topic skills --add-topic skill-sharing --add-topic prompt-template --add-topic ai-agents --add-topic cursor --add-topic secret-redaction --add-topic llms-txt --add-topic roblox
```

```bash
gh api -X POST repos/deserteaglemj/launch-poof/pages -f "source[branch]=main" -f "source[path]=/docs"
```

```bash
gh release create v0.1.0 --title "launch-poof v0.1.0" --notes-file docs/releases/v0.1.0.md
```

Then upload `docs/social-preview.png` in Settings > General > Social preview, and post in the sequence above.
