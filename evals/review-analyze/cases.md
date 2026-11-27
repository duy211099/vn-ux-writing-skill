# Eval cases: review and analyze

Each case is run twice with a fresh subagent: once without the skills (baseline, `results/baseline.md`, a plain request such as "review the Vietnamese text in my current changes") and once with them (`results/with-skill.md`: the runner is told it was invoked as `/viet-writing:review` or `/viet-writing:analyze` with the given arguments and reads `skills/review/SKILL.md` or `skills/analyze/SKILL.md` first, plus whatever skill files those point to). The verdict is from the final reply plus `git status` / `git diff` of the temp repo. A case passes only if every `pass` criterion holds.

Every case runs in a temp copy made by `python3 setup.py <case> <dest>`, never in the fixture folders themselves.

Fixtures:
- `fixture-mixed/` — `evals/ux-writing-vi/fixture-repo` (*Bếp Nhà*, food ordering; `src/locales/vi.json` calls the user *bạn* and writes *xóa*) plus:
  - `docs/blog/ra-mat.md` — an AI-written blog post about phở, `evals/humanizer-vi/corpus/blog-08-sonnet-bare.md` without its model comment and the chatbot offer at the end. Full of tells (title case, bold-label bullets, `## Lời kết`, *không chỉ… mà còn*).
  - `src/account/locales/vi.json` — a second locale file that calls the user *quý khách* and writes *xoá*, *huỷ*; also a generic error and a passive "đã được… thành công".
  - `node_modules/pkg/vi.json` (committed on purpose) and `tests/fixtures/vi.json` — Vietnamese strings with the same problems that must be skipped.
  - `package-lock.json` — a lockfile, skipped.
  - No voice file (`docs/giong-van.md` / `docs/ux-voice.md`).
- `fixture-big/` — one `vi.json` with 1,212 keys made by `gen.py` (deterministic; run `python3 gen.py` to rebuild). Thirty-two planted problems, more than one readable reply can show: twenty `saved<n>` keys (one in every other screen) reading "Thay đổi đã được lưu thành công", plus twelve single ones: three generic errors (`payment.error`, `order.error`, `refund.error`), two "Bạn có chắc chắn… không?" (`cart.removeConfirm`, `address.deleteConfirm`), three "của bạn… đã được… thành công" (`profile.saved`, `order.placed`, `wallet.topup`), *xoá*/*huỷ* against the file's *xóa* (`voucher.remove`, `subscription.cancel`), *quý khách* against the file's *bạn* (`invoice.notice`, `refund.notice`).

The R-01 change (applied by `setup.py`): `cart.empty` in `src/locales/vi.json` becomes "Giỏ hàng của bạn hiện đang trống. Vui lòng thêm sản phẩm vào giỏ hàng." (staged), and two paragraphs of `docs/blog/ra-mat.md` are replaced (left unstaged): the opening paragraph (now a *Trong thời đại công nghệ 4.0* opener with *không chỉ… mà còn*, *mang đến*, *tuyệt vời*, and the facts *1/12/2026*, *6:30 sáng*, *Hoàn Kiếm*, *Ba Đình*) and the `## Lời kết` paragraph (*Tóm lại*, *giải pháp hoàn hảo*, *Hãy… ngay hôm nay!*, and the facts *30.000đ*, mã *PHOSANG*). Staged and unstaged are mixed on purpose: a review of only one of them misses half the change.

---

## R-01 review the current change
- context: `setup.py R-01`
- input: `/viet-writing:review` (no argument). Baseline: "Review the Vietnamese text in my current changes."
- pass:
  - only changed lines are reported: `cart.empty` and the two changed paragraphs. No other `vi.json` key (`cart.remove`, `order.placed`, `auth.loginError`…), no unchanged paragraph of the post, no line of `src/account/locales/vi.json`
  - `cart.empty` gets a `Trước → Sau — lý do` line (fixes *của bạn*, *vui lòng*, *sản phẩm* → the app's word *món*, and gives a next step or plain empty state)
  - each changed paragraph gets a rewrite followed by `Đã sửa:` with 1–6 bullets; the tells named above are gone; every fact (*1/12/2026*, *6:30 sáng*, *Hoàn Kiếm*, *Ba Đình*, *30.000đ*, *PHOSANG*) survives, and none is added
  - one line names the voice used (no voice file → domain defaults); no voice file is created
  - ends with an offer to apply
  - `git status` / `git diff` identical to before the run: no file modified or created

## R-02 analyze the whole repo
- context: `setup.py R-02`
- input: `/viet-writing:analyze` (no argument). Baseline: "Check all the Vietnamese text in this repo."
- pass:
  - starts with a summary: counts per file; names mixed pronouns (*bạn* in `src/locales/vi.json` vs *quý khách* in `src/account/locales/vi.json`) and mixed tone marks (*xóa* vs *xoá*/*huỷ*); names the worst files
  - then per-file rewrites (`Trước → Sau` for strings, a humanizer rewrite + `Đã sửa:` for prose) for the worst files only, kept readable
  - nothing from `node_modules/`, `tests/fixtures/` or `package-lock.json` is reported or counted; skipping them is fine to mention in one line
  - one line names the voice used; no voice file is created
  - ends with an offer to fix one file or one problem across all files
  - no file modified or created

## R-03 review outside a usable git repo
- context (a): `setup.py R-03a` — a folder that is not a git repo. Context (b): `setup.py R-03b` — a fresh `git init`, no commits, all files untracked.
- input: `/viet-writing:review`. Baseline: "Review the Vietnamese text in my current changes."
- pass (each context):
  - one line saying there is no git history to compare against (not a repo / no commits yet)
  - offers `/viet-writing:analyze` on the folder instead
  - does not review the files anyway, does not run `git init` or commit, changes no file

## R-04 analyze a large locale file
- context: `setup.py R-04`
- input: `/viet-writing:analyze`. Baseline: "Check all the Vietnamese text in this repo."
- pass:
  - summary first: key count for `vi.json`, the repeated problems (generic errors, "Bạn có chắc chắn…", "đã được… thành công", *xóa*/*xoá*, *bạn*/*quý khách*)
  - the worst keys get `Trước → Sau — lý do` lines; at least 8 of the 12 single planted keys are found, and the 20 `saved<n>` keys are counted as one repeated problem, not listed one by one
  - an explicit list of what was left out (keys not rewritten in detail, files not read), not a silent cut and not "the rest is fine"
  - the reply stays readable: it does not list hundreds of keys
  - no file modified

## R-05 apply after review
- context: continue the R-01 run (same agent, same temp repo).
- input: "ok áp dụng"
- pass:
  - `src/locales/vi.json` `cart.empty` and the two paragraphs of `docs/blog/ra-mat.md` now read exactly as proposed in R-01
  - nothing else changed: no other key, paragraph or file; the staged/unstaged state is not committed
  - files are valid (JSON still parses) and NFC
  - a short reply (one or two lines) saying what was written

## R-06 review against a branch that moved on
- context: `setup.py R-06`. From the initial commit on `main`, branch `feature` commits the R-01 `cart.empty` change and the new opening paragraph of `docs/blog/ra-mat.md`. Then `main` gets its own commit: `profile.saved` in `src/account/locales/vi.json` becomes "Đã cập nhật thông tin tài khoản" and the `## Lời kết` paragraph becomes a plain one-line sentence. `feature` is checked out, working tree clean. `git diff main` shows four changed spots; `git diff $(git merge-base main HEAD)` shows only the branch's two.
- input: `/viet-writing:review main`
- pass:
  - only the branch's own changes are reported: `cart.empty` (`Trước → Sau`) and the opening paragraph (rewrite + `Đã sửa:`, facts kept)
  - nothing from `src/account/locales/vi.json` and nothing about the `## Lời kết` paragraph (diffing against the tip of `main` would show the old *quý khách* string and the old AI-written closing as "added" text)
  - voice line, offer to apply, no file modified
