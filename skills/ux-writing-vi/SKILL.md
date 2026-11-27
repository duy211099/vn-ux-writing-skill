---
name: ux-writing-vi
description: Use when writing, editing or reviewing Vietnamese user interface text — buttons, labels, errors, empty states, dialogs, notifications, onboarding, form hints — including adding or changing keys in Vietnamese locale files (vi.json, vi.yml, vi.ts, *_vi.arb, values-vi/strings.xml, vi.lproj, vi.po), English-source strings in a repo that has a Vietnamese locale, hardcoded Vietnamese strings in components, or when someone shares Vietnamese copy, a screenshot or a URL of a Vietnamese screen and asks to improve it.
---

# Vietnamese UX writing

Write Vietnamese interface text that sounds native, stays consistent across the app, and helps the user act. The people using this skill are usually solo developers with no UX writing experience: **make the decisions for them**, state each one in a single line, and let them override. Never hand them a menu of tone or pronoun choices.

Framework adapted from the UX Writing Skill by Christopher Greer (MIT). Language rules paraphrased from the Microsoft Vietnamese Localization Style Guide.

## When to use

- **Mode A — while coding.** You are about to write or change any user-facing string in a repo that has a Vietnamese locale or Vietnamese UI text. This includes adding a key to `en.json` when a `vi.json` exists: write the Vietnamese value too.
- **Mode B — review on request.** The user pastes text, shares a screenshot or URL, or points at files and asks to check or improve the Vietnamese copy.

## Mode A: writing strings in a repo

1. **Read the voice file**: `docs/giong-van.md`, or `docs/ux-voice.md` if only that one exists (use it where it is; never move or rename it unasked). If neither exists, create `docs/giong-van.md` before writing any string. If the `style-vi` skill is available, use it to create the file, and its one-line notice is the notice: write it once, as the last line of your reply, never a second notice of your own. Otherwise:
   - Copy [templates/giong-van.md](templates/giong-van.md). Leave its `## Văn bản dài` section as the template's `[ví dụ: …]` placeholders; it is for prose, not UI strings.
   - Guess the domain from the project name, `package.json`, README and existing screens. Set pronoun and register from the domain table in [references/xung-ho-va-giong-dieu.md](references/xung-ho-va-giong-dieu.md).
   - If existing Vietnamese strings already use one pronoun (*quý khách*, *anh/chị*, *bạn*) or one tone-mark style (*xóa* vs *xoá*), record that instead of the default.
   - **Required** (when you created the file yourself): end your reply with a one-line notice to the user that says what you chose and that they change it by editing `docs/giong-van.md`. Write it as text for the user, not as a note to yourself or the caller. Example: `Đã tạo docs/giong-van.md: gọi người dùng là "bạn", giọng thân thiện (ứng dụng giao đồ ăn). Sửa file này nếu muốn đổi.` Don't ask first.
2. **Identify the element** (button, error, empty state, dialog…) and apply its pattern from [references/mau-noi-dung.md](references/mau-noi-dung.md).
3. **Write the Vietnamese from intent.** When the source is an English string, work out what the user needs to know and do, then write it as Vietnamese copy. Don't translate word by word, and don't call the result a translation. Check it against [references/loi-dich-may-moc.md](references/loi-dich-may-moc.md).
4. **Keep it consistent**: terms from [references/thuat-ngu.md](references/thuat-ngu.md) and from existing strings; the voice file's pronoun, particles and tone-mark style; formats from [references/dinh-dang.md](references/dinh-dang.md).
5. **Errors and limits always get a next step**, even when the English source has none. English "File too large" → `Tệp quá lớn. Chọn tệp dưới 20 MB.`
6. **Stay in scope.** Change only the strings the task needs. If you notice weak existing Vietnamese strings nearby (in the same locale file or component), list them in one or two lines at the end and offer a review. Don't rewrite them unasked.
7. **Don't explain obvious choices.** The user is coding. Mention a copy decision only when it's non-obvious (for example, you added a next step the English lacked).
8. **A request to change the pronoun or tone** (for example, switch to *quý khách*) is a voice change: update the voice file first (with `style-vi`'s Job 3 if it is available), then the strings.

## Mode B: reviewing copy

1. **Extract every string** from the text, screenshot, page (fetch the URL) or files: titles, labels, placeholders, buttons, links, errors, helper text.
2. If you are in the user's app repo, read `docs/giong-van.md` (or `docs/ux-voice.md` if only that exists) and follow it. If not, infer the domain from the content and apply the domain defaults. Say which voice you used in one line, describing the voice (pronoun, register), not the file. Don't end by asking which pronoun the user prefers. **Never mention the voice file in a review** — not to create it, offer it, or explain why you didn't. It belongs to Mode A.
3. **Start the answer with the rewrites in this exact shape**, one line per changed string, with the reason in Vietnamese — even for a single string, and before any other notes:

   ```
   Trước → Sau — lý do
   "Cài Đặt Thông Báo" → "Cài đặt thông báo" — Chỉ viết hoa chữ đầu.
   ```

   Group by screen or element if there are many. Skip strings that are already good, or list them as `Giữ nguyên: …`.
4. **Flag inconsistencies** across the strings: mixed pronouns, mixed terms, mixed tone-mark styles. Pick one and rewrite all of them to it.
5. In a repo, offer to apply the changes to the source files.

## Four standards

Every string should be:

- **Có mục đích:** it helps the user do something or understand where they are.
- **Ngắn gọn:** every word has a job. Cut "của bạn", "một cách", "thực hiện việc".
- **Tự nhiên:** it sounds like a polite person talking, not a translated document. Active voice; no "được… bởi".
- **Rõ ràng:** one meaning, specific, true. Name the thing, the number, the time.

## Patterns at a glance

| Element | Pattern | Example |
|---|---|---|
| Title | Noun phrase or verb + object, sentence case | Đổi mật khẩu |
| Button | `[Động từ] [đối tượng]`, 2–4 words | Thanh toán 245.000đ |
| Link | Describes the destination | Xem chính sách đổi trả |
| Input error | What to fix | Mật khẩu cần ít nhất 8 ký tự |
| System error | `[Điều gì không thành công]. [Vì sao]. [Cần làm gì].` | Chưa lưu được thay đổi. Mất kết nối mạng. Kiểm tra mạng rồi thử lại. |
| Success | `Đã [động từ] [đối tượng]` | Đã gửi hóa đơn |
| Confirm dialog | `[Động từ] [đối tượng]?` + consequence + `[Động từ]` / `Hủy` | Đăng xuất khỏi thiết bị này? [Đăng xuất] [Hủy] |
| Empty state | What's missing + what will appear + action in the domain's words | Chưa có địa chỉ nào. Lưu địa chỉ để đặt nhanh hơn. [Thêm địa chỉ] |
| Permission ask | Benefit first, then a specific button + `Để sau` | Quét mã QR để thanh toán nhanh. [Cho phép dùng camera] [Để sau] |
| Push notification | Title says what happened (≤ 40 chars), body gives detail | Món sắp đến / Tài xế còn khoảng 3 phút nữa. |
| Form | Visible label + example placeholder + format hint | Số điện thoại / 0912 345 678 |

Full patterns with do/don't examples: [references/mau-noi-dung.md](references/mau-noi-dung.md). Worked rewrites: [examples/truoc-va-sau.md](examples/truoc-va-sau.md).

## Top traps

1. **Generic errors.** "Đã xảy ra lỗi", "Lỗi:", "… thất bại". Say what failed, why, and what to do.
2. **"Bạn có chắc chắn muốn… không?"** with "Có/Không" buttons. Use `[Động từ] [đối tượng]?` and buttons that name the action.
3. **Stacked *vui lòng*.** At most one per screen, and in a friendly voice usually none: start with the verb.
4. **Translation tics.** "của bạn" / "của chúng tôi" everywhere, passive "đã được… thành công", "một cách + tính từ", title case.
5. **The app talking about itself.** "Chúng tôi…", "Mình đã…", "ứng dụng của chúng tôi". Drop the subject or use the app's name (*chúng tôi* is fine only for finance, legal or policy text — trừ văn bản tài chính, pháp lý, chính sách).

Also: use the domain's own words ("món" in a food app, not "sản phẩm"), no English left in the UI except accepted terms (OTP, email), and no abbreviations on buttons or labels.

## Mechanics

- **Placeholders are byte-for-byte.** Keep `{{count}}`, `{name}`, `%s`, `%1$d`, `<b>…</b>` exactly. Vietnamese has no plural forms: one sentence works for every count. For i18next, the `_other` key is enough for `vi`; if the project keeps `_one` too, give it the same text.
- **ICU and native plurals** (Flutter ARB, FormatJS `{count, plural, …}`, Android `<plurals>`, iOS `.stringsdict`): keep the `plural`/`select` structure and every placeholder, write Vietnamese inside each branch, and always keep `other` (for `vi` it can be the only branch besides `=0`).
- **Several `%s`/`%d` in one string:** if Vietnamese word order differs, switch to positional `%1$s`, `%2$s` instead of reordering unindexed ones, and say so.
- **Output NFC.** Normalize any Vietnamese you write or rewrite to Unicode NFC, even if the input was decomposed (NFD).
- **Tone marks** follow the repo (*xóa* or *xoá*); the default is *xóa*. The style applies to every word, not just the one you saw: a *xoá* repo also writes *huỷ*, *hoà*, *thuỷ*. Never mix the two.
- **Number, date and currency formats**: `1.526`, `4,5`, `14:30`, `27/11/2026`, `100.000đ` (banking: `100.000 VND`). See [references/dinh-dang.md](references/dinh-dang.md).
- **Accessibility**: descriptive link text, no abbreviations a screen reader will spell out, don't rely on colour alone. See [references/tiep-can.md](references/tiep-can.md).

## Reference map

| Load | When |
|---|---|
| [references/xung-ho-va-giong-dieu.md](references/xung-ho-va-giong-dieu.md) | Creating the voice file, choosing a pronoun or register, using particles (*nhé*, *vui lòng*, *hãy*) |
| [references/mau-noi-dung.md](references/mau-noi-dung.md) | Writing any element: the full pattern and examples |
| [references/loi-dich-may-moc.md](references/loi-dich-may-moc.md) | The source is English, or reviewing copy that sounds translated |
| [references/thuat-ngu.md](references/thuat-ngu.md) | Choosing between a Vietnamese word and a loanword; keeping terms consistent |
| [references/dinh-dang.md](references/dinh-dang.md) | Dates, times, numbers, money, punctuation, capitalization, Unicode |
| [references/tiep-can.md](references/tiep-can.md) | Alt text, link text, screen readers, form errors |
| [examples/truoc-va-sau.md](examples/truoc-va-sau.md) | Calibrating a rewrite or showing the user examples |
| [templates/giong-van.md](templates/giong-van.md) | Creating `docs/giong-van.md` (when `style-vi` is not available) |
