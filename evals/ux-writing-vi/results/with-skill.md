# Results with the skill

Run: 2026-11-27. Model: sonnet, one fresh subagent per case, told to read `skills/ux-writing-vi/SKILL.md` first and follow it. Mode A cases ran in a fresh git copy of the fixture repo; the verdict is from the diff plus the final reply. Baseline results: [baseline.md](baseline.md).

**Summary:** 20 / 20 cases pass every criterion (baseline: 12 / 20). B-01, B-08 and B-10 passed before the final Mode B wording change and were not re-run after it, so treat those three as provisional. The gaps closed are exactly the ones found in the baseline: a persistent voice file, domain register, the `Trước → Sau` shape, next steps on errors, flagging weak neighbouring strings, and no app self-reference.

| Case | Baseline | With skill | Output / notes |
|---|---|---|---|
| A-01 | FAIL | PASS | `docs/ux-voice.md` created (bạn, thân thiện, "món"/"đơn", *xóa*) and announced in one line; no questions. "Đặt lại". Weak neighbours listed. |
| A-02 | PASS | PASS | "Chưa thanh toán được vì cổng thanh toán không phản hồi. Thẻ chưa bị trừ tiền. Thử lại." Written from intent; no "của bạn". |
| A-03 | PASS | PASS | "Xác nhận" → "Đặt món" (food-domain verb). Voice file created. |
| A-04 | PASS | PASS | "Giao trong 30–45 phút." Kept hardcoded, as the file is. |
| A-05 | FAIL | PASS | "Quý khách đã dùng hết hạn mức chuyển tiền hôm nay. Vui lòng thử lại vào ngày mai." Adds a next step; voice file records *quý khách*, *xoá*. |
| A-06 | PASS | PASS | `badge_one` = `badge_other` = "{{count}} món trong giỏ". Domain word "món". |
| A-07 | FAIL | PASS | Only `cart.checkout` added; lists `auth.loginError`, `cart.remove`, `order.placed`, Checkout strings with an offer to review. |
| A-08 | PASS | PASS | "Xoá thẻ" / "Xoá thẻ?" following the repo; voice file: *quý khách*, trang trọng, *xoá*. Reply suggested "Hủy" (mixed style) → see Refactor. |
| B-01 | FAIL | PASS | `Trước → Sau`: "Chưa tải được ảnh lên. Ảnh vượt quá 5 MB. Chọn ảnh nhỏ hơn rồi thử lại." Reason in Vietnamese. |
| B-02 | PASS | PASS | "Xóa ảnh này?" + consequence + [Xóa ảnh] [Hủy]. |
| B-03 | PASS | PASS | No *vui lòng* left; input error made specific ("Email cần có ký tự @"). |
| B-04 | PASS | PASS | "OK" → "Lưu địa chỉ". |
| B-05 | PASS | PASS | "Chưa có đơn hàng nào / Đơn bạn đặt sẽ hiện ở đây… [Xem sản phẩm]". Format drifted ("Đổi X thành:") and it offered to create a voice file → see Refactor. |
| B-06 | PASS | PASS | Benefit first; [Bật thông báo] [Để sau]; no "Chúng tôi". |
| B-07 | PASS | PASS | NFC output; "Xóa tài khoản?"; error rewritten with a next step. |
| B-08 | PASS | PASS | "Lưu". |
| B-09 | FAIL | PASS | All six strings extracted; `Trước → Sau` with reasons; sentence case, "Submit" → "Đăng nhập", descriptive link, error without "Lỗi:"/"!". |
| B-10 | FAIL | PASS | `Trước → Sau`; "của chúng tôi" removed; empty state with action; specific buttons; benefit-first permission ask. |
| B-11 | FAIL | PASS | Formal, no pronoun, no *nhé*: "Mã OTP đã hết hạn. Chọn "Gửi lại mã" để nhận mã mới." Keeps "OTP". |
| B-12 | PASS | PASS | Flags *bạn*/*quý khách*/*mình*, unifies on *bạn*, drops "mình" self-reference. |

## Refactor (loopholes found in the GREEN run)

1. **Voice file noise in reviews.** B-01, B-05, B-08 and B-10 mentioned or offered to create `docs/ux-voice.md` in a review. Fix: Mode B step 2 now says not to create, offer or discuss the voice file in a review.
2. **Format drift on a single string.** B-05 used "Đổi X thành:". Fix: Mode B step 3 says the shape applies even for a single string.
3. **Tone-mark style applied to one word only.** A-08 wrote "Xoá" but suggested "Hủy". Fix: SKILL.md and `dinh-dang.md` say the style applies to every *oa/oe/uy* word (*xoá → huỷ, hoà, khoẻ*).

Reruns after the fix: see the end of this file.

### Reruns after the fix

| Case | Result | Notes |
|---|---|---|
| A-08 (adds `card.deleteCancel`) | PASS | "Xoá thẻ" / "Xoá thẻ?" / "**Huỷ**": style now applied to every word. |
| B-05 (rerun 1, after the first fix) | still noisy | Explained why it didn't create the voice file; used "Replace … with:". The rule was tightened to "Never mention `docs/ux-voice.md` in a review" and "start with the rewrites". |
| B-05 (rerun 2) | PASS | Opens with `"Không có dữ liệu." → "Chưa có đơn hàng nào" + … — lý do`; no voice-file mention. |

Not re-run: B-01, B-08 and B-10 had the same voice-file noise. They're covered by the same rule, but untested after the change.

## Run 2026-11-27 (after plugin restructure)

Run: 2026-11-27, after the skill moved to `skills/ux-writing-vi/` and the voice file became `docs/giong-van.md`. Model: sonnet, one fresh subagent per case, told to read `skills/ux-writing-vi/SKILL.md` first and follow it. Mode A cases ran in a fresh git copy of the fixture; verdict from the diff plus the final reply. B-09 read the PNG; B-10 read the HTML file directly instead of a served URL.

**Summary:** 19 / 20 cases pass on the first run (previous run: 20 / 20). The one first-run miss is A-01 (criterion 3: the reply listed the voice choices but not how to change them). A-01 then passed on a rerun and on three further fresh-runner runs (see below), so the miss is not reproducible but is not proven to be noise either. No change to the skill. This run also covers B-01, B-08 and B-10 under the final Mode B wording, which the previous run had only provisionally.

**A-01 repeat runs (fresh runner, fresh fixture copy each):** run 1 miss (no "how to change"); rerun PASS ("... Sửa file này nếu muốn đổi"); x1 PASS (same line); x2 PASS (same line); x3 marginal PASS (voice file created and choices stated, "how to change" given as "the user can edit that file" addressed to the caller, not as the one-line notice). Pass rate on the three extra runs: 3 / 3 (one of them marginal); over all five runs: 4 / 5 clean plus one marginal. All five created `docs/giong-van.md` and none created `docs/ux-voice.md`; none asked questions. Other checks: A-05 created `docs/giong-van.md` (as did all Mode A cases that started without one); B-07's strings, as returned by the runner, are NFC (`unicodedata.normalize('NFC', s) == s` is True for all five).

| Case | Previous | Now | Output / notes |
|---|---|---|---|
| A-01 | PASS | FAIL first run, PASS on 4 later runs | `docs/giong-van.md` created (bạn, no self-reference, *xóa*), no `docs/ux-voice.md`; `order.reorder` = "Đặt lại đơn"; no questions. First run: notice lacked "how to change" in the reply; rerun gave the full line. |
| A-02 | PASS | PASS | "Chưa thanh toán được vì quá thời gian chờ. Thẻ chưa bị trừ tiền. Thử lại." No "của bạn", no *vui lòng*. |
| A-03 | PASS | PASS | "Xác nhận" → "Đặt món"; only that string changed in Checkout.jsx; voice file created. |
| A-04 | PASS | PASS | "Dự kiến giao trong 30–45 phút." hardcoded, en dash, not moved to i18n. |
| A-05 | PASS | PASS | "Quý khách đã đạt hạn mức chuyển tiền hôm nay. Thử lại vào ngày mai hoặc liên hệ ngân hàng để tăng hạn mức." Formal, next step. |
| A-06 | PASS | PASS | `badge_one` = `badge_other` = "{{count}} món trong giỏ hàng". |
| A-07 | PASS | PASS | Only `cart.checkout` added ("Thanh toán"); five weak strings listed with an offer to review. |
| A-08 | PASS | PASS | "Xoá thẻ" / "Xoá thẻ?"; voice file records *xoá, huỷ, hoà*, quý khách. |
| B-01 | PASS | PASS | `Trước → Sau`: "Ảnh quá lớn. Chọn ảnh dưới 5 MB rồi tải lên lại." Reason in Vietnamese; no voice-file mention. |
| B-02 | PASS | PASS | "Xóa ảnh này?" + consequence + [Xóa ảnh] [Hủy]. |
| B-03 | PASS | PASS | Rewrites carry no *vui lòng* (one only in an optional formal variant); split into specific messages. |
| B-04 | PASS | PASS | "OK" → "Lưu địa chỉ" with reason. |
| B-05 | PASS | PASS | "Chưa có đơn hàng nào" + "Đơn bạn đặt sẽ hiện ở đây…" + [Xem sản phẩm]; no "dữ liệu" in the rewrite. |
| B-06 | PASS | PASS | "Nhận thông báo khi đơn hàng có cập nhật." [Bật thông báo] [Để sau]. |
| B-07 | PASS | PASS | "Xóa tài khoản?" with consequence and [Xóa tài khoản] [Hủy]; error rewritten with a next step. NFC machine-checked on the reply strings. |
| B-08 | PASS | PASS | "Lưu". |
| B-09 | PASS | PASS | All six strings extracted; sentence-case title, "Submit" → "Đăng nhập", link text, error without "Lỗi:" / "!"; `Trước → Sau` with reasons. |
| B-10 | PASS | PASS | "chúng tôi" removed; empty state with action; specific buttons; benefit-first permission ask; `Trước → Sau`. |
| B-11 | PASS | PASS | "Mã OTP đã hết hạn. Nhấn "Gửi lại mã" để nhận mã mới." Formal, no pronoun, keeps OTP. |
| B-12 | PASS | PASS | Flags *quý khách* / *bạn* / *mình*, unifies on *bạn*, drops the "mình" self-reference. |

No Mode B reply mentioned the voice file. The Mode A runs read `docs/giong-van.md` first (all created it where none existed).
