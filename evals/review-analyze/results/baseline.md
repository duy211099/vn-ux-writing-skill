# Baseline results (no skills)

Run: 2026-11-27. Model: sonnet, one fresh subagent per case, no skills, told not to read this repo. Each case ran in a temp copy made by `setup.py`; the verdict is from the final reply plus `git status` / `git diff` of the temp repo. Cases: [../cases.md](../cases.md). With the skills: [with-skill.md](with-skill.md).

Requests: R-01 and R-03 "Review the Vietnamese text in my current changes."; R-02 and R-04 "Check all the Vietnamese text in this repo."; R-05 "ok áp dụng" sent to the R-01 agent.

**Summary:** 0 / 6 runs pass (R-03 counted as two runs).

| Case | Result | What happened |
|---|---|---|
| R-01 | FAIL | Found both the staged `vi.json` change and the unstaged paragraphs. Reply in English with `##` headings and diff blocks. Prose handled as a critique: bullet lists of problems per paragraph plus a one-sentence "suggested rewrite" that cut most of each paragraph, no `Đã sửa:` list. Advised reverting the change and argued about whether the post should be an ad. Added a "Not in the diff" section about `cart.removeConfirm`. No voice line. Suggested a new `emptyAction` key. No explicit offer to apply. No file changed. |
| R-02 | FAIL | Named mixed *bạn*/*quý khách* and *xóa*/*xoá*/*huỷ*, skipped `node_modules`, but **reviewed `tests/fixtures/vi.json`** and counted it in the pronoun problem. No counts per file and no "worst files"; problems as a bulleted essay with no `Trước → Sau`. Blog got four small notes (Title Case, *muỗng*), no rewrite. Ended asking the author to choose: "First I need your choices on voice ("bạn" or "quý khách") and tone-mark style". No file changed. |
| R-03a (no git) | FAIL | Said in one sentence it was not a git repo, then **reviewed every file anyway** (about 40 lines: pronouns, tone marks, errors, a code bug in `App.jsx`, the blog). Included `tests/fixtures`. No mention of a whole-repo check as the alternative. |
| R-03b (no commits) | FAIL | Treated "nothing committed" as "every file is a change" and reviewed the whole repo in eight numbered sections, including `tests/fixtures/vi.json` and a missing `en.json`. No offer of anything else. |
| R-04 | FAIL | Content good: found all 12 planted keys, grouped them by problem, stayed readable. But no `Trước → Sau — lý do` lines (fixes given for some groups only), no voice line, no list of what was left out (it said the other 1,200 strings were fine as a pattern claim), and it suggested also editing `gen.py`. No file changed. |
| R-05 | FAIL | Applied its suggestions, but not exactly as proposed: the closing paragraph dropped `[link]` and became "…Đặt trên ứng dụng Bếp Nhà." Did not stage over the staged file (good). The reply was a four-item "Cần bạn quyết" list, including advice to run `git checkout -- docs/blog/ra-mat.md`. |

## Failure patterns the skills have to address

1. **No stop when there is nothing to diff.** Not a repo, or no commits: the agent reviews everything instead of saying so and pointing at the whole-repo command.
2. **Scope creep.** Unchanged strings ("Not in the diff") in a review; test fixtures in a whole-repo check; `gen.py` and code bugs.
3. **Critique instead of rewrite for prose.** Problems listed per paragraph, then a short "suggested" sentence that drops content; no fixed `Đã sửa:` shape.
4. **No fixed output shape.** English or Vietnamese at random, headings, diff blocks, tables; no `Trước → Sau — lý do`; no summary with counts and worst files.
5. **Asking instead of deciding.** "First I need your choices on voice", "Cần bạn quyết". No voice line.
6. **Applying is loose.** What was written differs from what was shown, and the reply is a new list of open questions.
