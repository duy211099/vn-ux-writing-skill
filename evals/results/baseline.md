# Baseline results (without the skill)

Run: 2026-11-27. Model: sonnet, one fresh subagent per case, no skill loaded. Mode A cases ran in a fresh git copy of the fixture repo; the verdict is from the diff plus the final reply.

**Summary:** 12 / 20 cases pass every criterion. The base model already avoids the obvious anti-patterns ("Đã xảy ra lỗi", "Bạn có chắc chắn…không?", "OK" buttons, "Nhấp vào đây"). Where it fails is consistency and the workflow: no persistent voice, register that doesn't follow the domain, an output format that varies from run to run, missing next steps, not flagging weak strings, and ending with a question instead of deciding.

| Case | Result | Failed criteria / notes |
|---|---|---|
| A-01 | FAIL | No `docs/ux-voice.md`; no voice decision recorded or announced. String "Đặt lại" OK. |
| A-02 | PASS | "Hết thời gian thanh toán. Thẻ của bạn chưa bị trừ tiền. Hãy thử lại." Calls it "my own translation"; "Thẻ của bạn" is the *của bạn* tic. |
| A-03 | PASS | "Thanh toán {total}". |
| A-04 | PASS | "Dự kiến giao hàng trong 30–45 phút." |
| A-05 | FAIL | "Quý khách đã đạt hạn mức chuyển tiền trong ngày": register right, but **no next step**. |
| A-06 | PASS | Only `badge_other`, `{{count}}` kept. Chose "sản phẩm" in a food app ("món" fits better); not a criterion. |
| A-07 | FAIL | Stayed in scope, but **didn't mention the weak `vi.json` strings** ("Đã xảy ra lỗi…", "Bạn có chắc chắn…"). It only mentioned the hardcoded Checkout text. |
| A-08 | PASS | Followed *Xoá*; "Xoá thẻ" / "Xoá thẻ này?". |
| B-01 | FAIL | Content good, but **not in `Trước → Sau` format**; the first rewrite keeps "Vui lòng". Reply in English to a Vietnamese string review. |
| B-02 | PASS | "Xóa ảnh này?" / "Hủy" / "Xóa ảnh". |
| B-03 | PASS | No *vui lòng* left. Ends by asking for more context. |
| B-04 | PASS | "Lưu địa chỉ". |
| B-05 | PASS | "Bạn chưa có đơn hàng nào" + "Mua sắm ngay". Ends with a question; the generic CTA ignores that it's a food app. |
| B-06 | PASS | Benefit first, "Bật thông báo" / "Để sau". Uses "**Chúng tôi** chỉ nhắn…" (self-reference). |
| B-07 | PASS | NFC output; "Bạn muốn xóa tài khoản?". Second string keeps "Vui lòng thử lại." |
| B-08 | PASS | "Lưu". |
| B-09 | FAIL | Content strong (sentence case, Submit→Đăng nhập, link text, error), but **not in `Trước → Sau` format** (a table of the final copy). |
| B-10 | FAIL | Content strong, but **not in `Trước → Sau` format**. |
| B-11 | FAIL | Banking app, yet the default is "**Bạn vui lòng** lấy mã mới": **not the formal register**. Ends by asking which pronoun to use. |
| B-12 | PASS | Flags the mix. Picks "mình"/"bạn" and keeps *mình* self-reference, which goes against the skill's default of no self-reference. |

## Patterns to target in the skill (with quotes)

1. **No persistent voice.** Every run re-decides the pronoun; nothing is written down (A-01). Several runs end with "Pick one register… and keep it" or "Cho mình biết app của bạn…" (B-05, B-11, B-12), which pushes the decision onto a novice.
2. **Domain register not applied by default.** Banking → "Bạn vui lòng…" (B-11).
3. **Output shape varies.** Prose, tables or bullet lists; never a consistent `Trước → Sau — lý do` (B-01, B-09, B-10). Replies are often in English.
4. **Errors without a next step** when the source string has none (A-05).
5. **Doesn't flag weak neighbouring strings** in locale files (A-07).
6. **Residual tics:** "của bạn" (A-02 "Thẻ của bạn"), leftover "Vui lòng thử lại" (B-01, B-07), app self-reference "Chúng tôi"/"Mình" (B-06, B-12), generic CTAs that ignore the domain ("Mua sắm ngay" in a food app, "sản phẩm" for dishes).
7. Frames Vietnamese as "my own translation" of the English (A-02) instead of writing copy from intent.
