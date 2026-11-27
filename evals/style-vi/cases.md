# Eval cases: style-vi

Each case is run twice with a fresh subagent: once without the skill (baseline, `results/baseline.md`) and once with it (`results/with-skill.md`, the runner reads `skills/style-vi/SKILL.md` first). Every case runs in a fresh git copy of `evals/ux-writing-vi/fixture-repo/` (*Bếp Nhà*, a food-ordering app whose `vi.json` calls the user *bạn* and writes *xóa*). The verdict is from the diff plus the final reply. A case passes only if every `pass` criterion holds.

Seeds (copied into the fixture copy before the run, then committed so the diff shows only the agent's changes):
- `seeds/giong-van.md` — a filled voice file for Bếp Nhà in the new format (user *bạn*, prose voice: Bếp Nhà, xen kẽ, trò chuyện).
- `seeds/ux-voice.md` — the same choices in the old `ux-writing-vi` format, without a `## Văn bản dài` section.

---

## S-01 No voice file: create one
- context: fixture-repo, no seed
- input: "Mình sắp viết blog cho app này. Thiết lập giọng văn cho dự án trước đi."
- pass:
  - `docs/giong-van.md` is created, and no other voice file
  - it records *bạn* (or no pronoun) for the user and *xóa* tone marks, matching the existing strings
  - the `## Văn bản dài` section is filled, not left as `[ví dụ: …]` placeholders, with a food-app default (self-reference by product name or another sensible choice; not *chúng tôi* + formal)
  - the reply states the choice in about one line and how to change it
  - no questions are asked first; no menu of options

## S-02 Only the old file exists
- context: fixture-repo + `seeds/ux-voice.md` at `docs/ux-voice.md`
- input: "Thiết lập giọng văn cho bài viết dài (blog) của dự án."
- pass:
  - `docs/ux-voice.md` is used: the prose settings are added to it
  - `docs/ux-voice.md` is not moved, renamed or deleted, and `docs/giong-van.md` is not created
  - existing UI choices in the file are kept
  - no questions are asked first

## S-03 Change the user pronoun
- context: fixture-repo + `seeds/giong-van.md` at `docs/giong-van.md`
- input: "Đổi cách xưng hô sang quý khách nhé."
- pass:
  - `docs/giong-van.md` now calls the user *quý khách* (register and particles adjusted is fine)
  - the reply lists the strings that now disagree: `cart.empty`, `cart.remove`, `order.placed` in `src/locales/vi.json` (all use *bạn*)
  - `vi.json` and every other file except the voice file are unchanged
  - it offers to update the listed strings rather than doing it

## S-04 What is our voice?
- context: fixture-repo + `seeds/giong-van.md` at `docs/giong-van.md`
- input: "Giọng văn của app là gì?"
- pass:
  - the answer summarises the voice file in a few lines (about 6 or fewer): user pronoun, self-reference, tone, prose voice
  - it names `docs/giong-van.md` as the place to change it
  - no files change
