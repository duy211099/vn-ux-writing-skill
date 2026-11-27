# Baseline results (no skill)

Run: 2026-11-27. Model: sonnet, one fresh subagent per case, no skills. Each case ran in a fresh git copy of `evals/ux-writing-vi/fixture-repo/` with the case's seed committed; the verdict is from the diff plus the final reply. Cases: [../cases.md](../cases.md). With the skill: [with-skill.md](with-skill.md).

**Summary:** 0 / 4 cases pass.

| Case | Result | What happened |
|---|---|---|
| S-01 | FAIL | Wrote a 50-line free-form `docs/giong-van.md` (brand persona "người bạn rành chuyện ăn uống", four voice traits, tables, an invented sample paragraph, items marked **[cần xác nhận]**) and an unasked `CLAUDE.md` pointing to it. Chose *mình*/*bạn*. Long reply ending with two numbered questions: "Xưng hô 'mình - bạn' có đúng không?" and who the blog is for. |
| S-02 | FAIL | Left `docs/ux-voice.md` untouched and created a second file, `docs/blog-voice.md` (title rules, sentence lengths in words, invented "canh chua cá lóc" example). Self-reference "Bếp Nhà hoặc chúng tôi". About 30-line reply with a "Cần bạn xác nhận" section. |
| S-03 | FAIL | Changed the pronoun in `docs/giong-van.md` but left the tone "Trung tính, thân thiện" and *nhé*. Rewrote `cart.empty` and `order.placed` in `vi.json` unasked; missed `cart.remove` ("Bạn có chắc…") because it searched only for "của bạn". |
| S-04 | FAIL | No files changed and the content was right, but the answer was about 22 lines: bold headings, nested bullets for every field down to the money format, plus "Bạn nên xem lại các mục này." |

## Failure patterns the skill has to address

1. **No fixed format.** Without the template, the voice file becomes a style-guide essay, and prose settings go into a new file (`blog-voice.md`) instead of the existing voice file.
2. **Extra files.** `CLAUDE.md` pointers, second voice files.
3. **Asking instead of deciding.** Questions about pronoun and audience at the end of the reply.
4. **A pronoun change treated as find-and-replace.** Strings were rewritten unasked, the search was too narrow, and related fields (register, particles) were left contradicting the new pronoun.
5. **Long answers** to a short question.
