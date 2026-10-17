# Results

Structural tests for the request-ai-export skill, run 2026-10-17 on macOS with Python 3.9.6.

Reproduce:

```bash
python3 -m unittest discover -s tests -v
```

Result: 7 of 7 tests passed (exit code 0).

```
test_every_placeholder_is_documented (test_skill.SkillTests) ... ok
test_example_is_the_filled_template (test_skill.SkillTests) ... ok
test_fill_leaves_no_placeholders (test_skill.SkillTests) ... ok
test_frontmatter (test_skill.SkillTests) ... ok
test_no_private_data_or_em_dashes (test_skill.SkillTests) ... ok
test_prompt_keeps_safety_steps (test_skill.SkillTests) ... ok
test_versions_in_sync (test_skill.SkillTests) ... ok

Ran 7 tests in 0.002s
OK
```

`claude plugin validate --strict .` on the same date: "Validation passed".

## What these tests do not cover

They check the files, not behavior. No end-to-end runs of the prompt in a friend's AI (Claude Code, Codex, Cursor, ChatGPT) have been measured yet.
