# Eval cases

Each case is run twice with a fresh subagent: once without the skill (baseline, `results/baseline.md`) and once with it (`results/with-skill.md`). Mode A cases run inside a fresh copy of the named fixture repo. A case passes only if every `pass` criterion holds.

Fixtures:
- `fixture-repo/` — *Bếp Nhà*, a consumer food-ordering app (React + react-i18next). `vi.json` contains several weak, literally translated strings. No `docs/ux-voice.md`.
- `fixture-repo-formal/` — *An Khang Bank*, a banking app. Its existing `vi.json` uses *quý khách* and the old tone-mark style (*xoá*).
- `inputs/` — files for Mode B cases.

---

## A-01 First run creates the voice file
- mode: A
- context: fixture-repo; task "Add a 'Reorder' button to past orders. Add the key `order.reorder` to en.json and vi.json."
- input: the task above
- pass:
  - `docs/ux-voice.md` is created
  - the voice file records the user pronoun (*bạn*) and how the app refers to itself
  - the user is told what was chosen in about one line, and how to change it
  - no questions are asked before doing the task

## A-02 English-source error key
- mode: A
- context: fixture-repo; task "When the payment gateway times out, show an error. Add `order.paymentTimeout` to en.json ('Payment timed out. Your card was not charged. Try again.') and vi.json."
- input: the task above
- pass:
  - the vi value says what failed, that the card wasn't charged, and what to do next
  - it doesn't open with "Đã xảy ra lỗi", "Lỗi:" or "Có lỗi xảy ra"
  - it has no stacked *vui lòng*; at most one, and none is better
  - it reads as natural Vietnamese, not English word order

## A-03 Payment confirm button
- mode: A
- context: fixture-repo; task "In src/Checkout.jsx, the pay button text 'Xác nhận' is unclear. Improve it."
- input: `src/Checkout.jsx`
- pass:
  - the button is `[verb] [object]`, e.g. "Thanh toán {total}" or "Đặt món"
  - it isn't "OK", "Đồng ý" or "Xác nhận"
  - only the button string changes in that file, unless other changes are only suggested

## A-04 Hardcoded Vietnamese, no locale file involved
- mode: A
- context: fixture-repo; task "Add a line under the total in src/Checkout.jsx telling users delivery takes 30–45 minutes."
- input: `src/Checkout.jsx`
- pass:
  - the new string is natural Vietnamese and consistent with the voice (*bạn* or no pronoun)
  - it uses a correct en dash or "đến" for the range; no "mins"
  - Claude doesn't move the text into i18n files unasked

## A-05 Repo already uses *quý khách*
- mode: A
- context: fixture-repo-formal; task "Add `transfer.limitExceeded` for when a transfer is over the daily limit, to en.json ('You've reached today's transfer limit') and vi.json."
- input: the task above
- pass:
  - the vi value uses *quý khách* (or no pronoun), never *bạn*
  - the register is formal, with no *nhé*/*nha*
  - it says what the user can do next (e.g. try tomorrow, or change the limit)

## A-06 Placeholders and plurals
- mode: A
- context: fixture-repo; task "Add a cart badge string: '{{count}} items in your cart', as en.json keys `cart.badge_one` ('{{count}} item in your cart') and `cart.badge_other`, plus vi.json."
- input: the task above
- pass:
  - `{{count}}` appears unchanged in the vi value(s)
  - there are no invented plural word forms; one Vietnamese form is fine (both keys may share it)
  - it uses the voice pronoun, or no pronoun

## A-07 Stay in scope
- mode: A
- context: fixture-repo; task "Add `cart.checkout` button text to both locale files."
- input: the task above (vi.json already has weak strings such as "Đã xảy ra lỗi. Vui lòng thử lại sau.")
- pass:
  - only `cart.checkout` is added; existing values are left alone
  - the weak existing strings are mentioned briefly, with an offer to review them

## A-08 Follow the repo's tone-mark style
- mode: A
- context: fixture-repo-formal; task "Add a 'Delete card' button: key `card.delete` in both locale files, and a confirm-dialog title `card.deleteTitle`."
- input: the task above
- pass:
  - the vi values use *xoá* (old style, as the repo does), not *xóa*
  - the dialog title names the action, and the button names the action

---

## B-01 Vague error
- mode: B
- input: "Review this error: 'Đã xảy ra lỗi. Vui lòng thử lại sau.' It shows when uploading a profile photo fails because the file is over 5 MB."
- pass:
  - the rewrite names the cause (the file is too large, limit 5 MB) and the fix (choose a smaller photo)
  - it is shown as `Trước → Sau` with a one-line reason in Vietnamese

## B-02 "Are you sure…?" calque
- mode: B
- input: "Improve this dialog: title 'Bạn có chắc chắn muốn xóa ảnh này không?', buttons 'Có' / 'Không'."
- pass:
  - the title names the action briefly (e.g. "Xóa ảnh này?") and may say what happens next
  - the buttons name the action ("Xóa" / "Hủy"), not "Có"/"Không"

## B-03 Stacked *vui lòng*
- mode: B
- input: "Review: 'Vui lòng nhập email. Vui lòng kiểm tra lại email của bạn. Vui lòng liên hệ hỗ trợ nếu cần.'"
- pass:
  - at most one *vui lòng* remains, and none is better
  - the message is shorter than the input

## B-04 Generic button
- mode: B
- input: "Button under a form that saves shipping address says 'OK'. Better?"
- pass:
  - the suggestion is a verb plus an object, e.g. "Lưu địa chỉ"
  - there is a one-line reason

## B-05 Dead-end empty state
- mode: B
- input: "Empty state on the Orders tab: 'Không có dữ liệu.'"
- pass:
  - the rewrite says what will appear here and gives a next step (e.g. a button "Xem thực đơn")
  - it doesn't use the word "dữ liệu"

## B-06 Permission without benefit
- mode: B
- input: "Push-permission prompt: 'Ứng dụng muốn gửi thông báo cho bạn. Cho phép?'"
- pass:
  - the benefit comes first (e.g. know when the order arrives), then the ask
  - the buttons are specific ("Bật thông báo" / "Để sau")

## B-07 NFD input
- mode: B
- input: the contents of `inputs/b07-nfd.txt` (decomposed Unicode), "Rewrite these two strings."
- pass:
  - the output strings are NFC (check with `unicodedata.normalize('NFC', s) == s`)
  - the first string isn't an "Bạn có chắc chắn…không?" calque

## B-08 Tight space
- mode: B
- input: "Translate/write the Vietnamese for a toolbar button. English is 'Save'. Space fits about 10 characters."
- pass:
  - the output is at most 3 words and fits the space (e.g. "Lưu")
  - it isn't abbreviated (no "L.")

## B-09 Screenshot
- mode: B
- input: image `inputs/b09-login.png`, "Review the copy on this screen."
- pass:
  - all six strings are extracted (title, two placeholders, error, button, link)
  - title-case "Đăng Nhập Vào Tài Khoản Của Bạn" is fixed to sentence case and shortened
  - "Submit" becomes "Đăng nhập"
  - "Nhấp vào đây" is replaced with descriptive link text
  - the error drops the "Lỗi:" prefix and "!" and says what to do
  - each change is `Trước → Sau` with a one-line reason

## B-10 URL
- mode: B
- input: URL of `inputs/b10-onboarding.html`, served locally (`python3 -m http.server` in `evals/inputs`), "Review the copy on this page."
- pass:
  - "ứng dụng của chúng tôi" self-reference is removed or reduced
  - the empty state gives a next step
  - "Tiếp tục"/"Đồng ý" become specific actions
  - the notification ask leads with the benefit
  - the output is in `Trước → Sau` format

## B-11 Banking domain, no voice file
- mode: B
- input: "I'm building a banking app. Write the message for when an OTP code expires."
- pass:
  - the register is formal: *quý khách* or no pronoun; no *nhé*
  - it keeps "OTP" (no invented translation)
  - it says what to do (e.g. "Gửi lại mã")

## B-12 Mixed pronouns
- mode: B
- input: "Review these strings from one app: 'Chào bạn!', 'Quý khách vui lòng xác nhận đơn hàng', 'Mình đã nhận được yêu cầu của bạn nhé'."
- pass:
  - the inconsistent pronouns (*bạn* / *quý khách* / *mình*) are flagged explicitly
  - all three rewrites use one consistent choice
