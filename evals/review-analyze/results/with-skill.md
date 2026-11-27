# Results with the skills

Run: 2026-11-27. Model: sonnet, one fresh subagent per case, told it was invoked as `/viet-writing:review` or `/viet-writing:analyze` (no arguments) and to read `skills/review/SKILL.md` or `skills/analyze/SKILL.md` first, plus the skill files they point to. Each case ran in a temp copy made by `setup.py`; the verdict is from the final reply plus `git status` / `git diff`. Baseline: [baseline.md](baseline.md).

**Summary:** 6 / 6 runs pass (baseline: 0 / 6). R-04 was re-run twice after the fixture got harder and after one refactor; see below.

## GREEN run

| Case | Result | Output / notes |
|---|---|---|
| R-01 | PASS | Voice line: "chưa có file giọng văn, dùng mặc định cho ứng dụng giao đồ ăn (gọi "bạn", dấu kiểu xóa)". `src/locales/vi.json`: one line, `cart.empty: "Giỏ hàng của bạn hiện đang trống. Vui lòng thêm sản phẩm vào giỏ hàng." → "Chưa có món nào trong giỏ. Chọn món để bắt đầu đặt." — …dùng "món" thay cho "sản phẩm"`. `docs/blog/ra-mat.md`: two rewrites, each with `Đã sửa:` (3 and 2 bullets): staged opener, *không chỉ… mà còn*, inflation, *Tóm lại*, *giải pháp hoàn hảo*, the *Hãy… ngay hôm nay!* closer. All six facts kept (1/12/2026, 6:30 sáng, Hoàn Kiếm, Ba Đình, 30.000đ, PHOSANG), none added. Nothing about unchanged keys or paragraphs. Last line "Áp dụng các thay đổi này vào file không?". `git status` unchanged; no voice file. Both the staged and the unstaged change were found. |
| R-02 | PASS | Voice line, then `Tổng quan` with four files and counts (`src/locales/vi.json — 8 chuỗi, 6 cần sửa`, `src/account/locales/vi.json — 7 chuỗi, 4 cần sửa`, `docs/blog/ra-mat.md — 11 đoạn, 5 có dấu hiệu văn AI`, `src/Checkout.jsx — 4 chuỗi, 2 cần sửa`), five repeated problems including "Lẫn xưng hô: "bạn" ở src/locales/vi.json, "quý khách" ở src/account/locales/vi.json" and "Lẫn kiểu dấu: "xóa" … "xoá/huỷ"", `Nặng nhất:` three files. Then 10 `Trước → Sau` lines over the two locale files and two blog rewrites with `Đã sửa:`. `Chưa rà chi tiết:` named `src/Checkout.jsx` and the remaining blog tells. `Bỏ qua: node_modules/, tests/fixtures/, package-lock.json.` Offer: "Mình sửa tiếp src/account/locales/vi.json, hay sửa lẫn xưng hô trên mọi file (đổi "quý khách" về "bạn")?" No file changed. |
| R-03a (no git) | PASS | One line: "Thư mục này chưa phải repo git nên không có thay đổi để so. Chạy /viet-writing:analyze để rà toàn bộ chữ tiếng Việt trong thư mục." Nothing else. |
| R-03b (no commits) | PASS | One line: "Repo chưa có commit nào nên chưa có gì để so. Chạy /viet-writing:analyze …". No `git init`/commit, files still untracked. |
| R-04 (12 planted) | PASS | Summary (`vi.json — 1.212 chuỗi, 12 cần sửa`, four repeated problems), all 12 planted keys as `Trước → Sau — lý do` lines, `Bỏ qua: gen.py và package.json`, offer one file or one problem. But `Chưa rà chi tiết: không có` because all 12 fit under the 15-line cap, so the left-out rule was not exercised. The fixture was made harder (below). |
| R-05 | PASS | Wrote exactly the proposed `cart.empty` value and the two proposed paragraphs; nothing else in either file; `vi.json` still staged with the new change unstaged on top (`MM`), no commit; JSON parses, both files NFC, trailing newline kept. Reply: "Đã áp dụng 1 chuỗi trong src/locales/vi.json và 2 đoạn trong docs/blog/ra-mat.md." |

**R-05 harness note.** The first attempt sent "ok áp dụng" to the R-01 runner through an agent message. It refused: "Lời "ok áp dụng" đến qua một phiên Claude khác, không phải do bạn gõ trực tiếp, nên mình không coi đó là xác nhận của bạn", and wrote nothing. That is the right behaviour for a relayed message (and a sign the no-write rule holds), but it is not the case. R-05 was then run in a fresh runner given the R-01 conversation as a script (its reply, then the user turn "ok áp dụng"), on the same temp repo. The result above is from that run. The baseline R-05 runner accepted the relayed message.

## Refactor

**Fixture made harder.** With 12 planted problems the answer fits under the detail cap, so nothing is left out. `fixture-big/gen.py` now also writes "Thay đổi đã được lưu thành công" into 20 `saved<n>` keys (32 problems in all).

| Run | Result | Notes |
|---|---|---|
| R-04, 32 planted | PASS (borderline) | Summary `32 cần sửa`, the 20 keys counted inside one repeated problem ("23 chuỗi") and shown as one line `saved3, saved7, saved11… (20 khóa): "Thay đổi đã được lưu thành công" → "Đã lưu thay đổi"`; all 12 single keys found. Loophole: `Chưa rà chi tiết: không có. Đã đếm cả 1.212 chuỗi bằng script, và các chuỗi còn lại không có lỗi.` A grep for known patterns cannot show that the rest has no problems. |

Fix in `skills/analyze/SKILL.md` §4: many keys with the same fix take one line (codifies the good grouping), and strings only scanned by a pattern script go under `Chưa rà chi tiết:` with their count, never as "không có lỗi"; matching red-flag row.

| Run | Result | Notes |
|---|---|---|
| R-04, after fix | PASS | Same summary (`32 cần sửa`, six repeated problems), 13 `Trước → Sau` lines with the 20 keys as one (`saved3, saved7, saved11… saved79 (20 khóa)`), all 12 single keys. Now: `Chưa rà chi tiết: 1.180 chuỗi còn lại trong vi.json (đã quét bằng mẫu lỗi, chưa đọc từng chuỗi)… Mình chưa kiểm tra thêm.` No file changed. Small slip: the offer says "đổi 23 chuỗi về dạng "Đã lưu thay đổi"", though only 20 of them are about saving; the detail lines above it are right. |

## Change to `humanizer-vi`

`skills/humanizer-vi/SKILL.md` said a call from `review` or `analyze` is embedded and returns "only the final text… No report, no `Đã sửa:`", which contradicts the commands' output (rewrite + `Đã sửa:`). The line now says such a call never writes a file and its result is shown in the pasted-text shape. The GREEN runs above used the changed line.

## Review fix round 1 (2026-11-27)

The review found that `review <branch>` diffed against the tip of the branch, so commits added to that branch after branching would show up reversed, as "added" text. `skills/review/SKILL.md` now diffs against `git merge-base <arg> HEAD`, with a red-flag row. New case R-06 (`main` moves on after `feature` branches). Wording fixes in the same round: `humanizer-vi` lists review/analyze as an explicit exception to embedded mode; `analyze` names `Bỏ qua vì quá lớn:` in its output parts and limits a "one problem everywhere" fix to files in scope; both commands say their voice line overrides `ux-writing-vi` Mode B's "never mention the voice file". Fresh runners, fresh temp repos.

| Case | Result | Output / notes |
|---|---|---|
| R-06 (`/viet-writing:review main`) | PASS | Voice line; `cart.empty` → "Chưa có món nào trong giỏ. Thêm món để đặt hàng." with reason; the opening paragraph rewritten (facts kept) with 3 `Đã sửa:` bullets; offer line. Nothing from `src/account/locales/vi.json`, nothing about `## Lời kết` (both differ from the tip of `main` but are not this branch's change). Repo clean, still on `feature`. |
| R-01 (re-run, no argument) | PASS | Same shape as the GREEN run: voice line, one `cart.empty` line, two paragraph rewrites with `Đã sửa:` (3 and 2 bullets), all six facts kept, offer line. Repo unchanged (`MM` state as set up). |
