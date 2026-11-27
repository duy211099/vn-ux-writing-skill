# AI-Vietnamese corpus: tell frequencies

Built 2026-11-27 for `humanizer-vi`. The table below sets the order of `references/dau-hieu-ai.md`. Raw samples are in `corpus/` and are the eval inputs for Task 6.

## Models and samples

**Claude only.** No other model API was available. The samples come from three Claude models, run as fresh Claude Code subagents: Sonnet, Haiku and Opus.

Each generator got a plain user request in Vietnamese, four requests per dispatch (one per genre), with no mention of style, AI tells or this project. Two dispatches per model gave 24 samples, 2 per genre per model:

| Genre | Sonnet | Haiku | Opus | Total |
|---|---|---|---|---|
| `blog` | 01, 04 | 02, 05 | 03, 06 | 6 |
| `gioi-thieu-san-pham` | 01, 04 | 02, 05 | 03, 06 | 6 |
| `facebook` | 01, 04 | 02, 05 | 03, 06 | 6 |
| `email` | 01, 04 | 02, 05 | 03, 06 | 6 |

Files are named `<genre>-<nn>-<model>.md`. Each starts with a one-line comment giving the model and the exact prompt. Same `nn` means same topic. All files are NFC.

Three of the six replies added a note to the user after the pieces (e.g. *"Ghi chú chung: các chỗ trong ngoặc vuông là thông tin chưa có…"*). I removed those notes, because they are not part of the requested text. Notes inside a piece were kept.

## Results

Counts come from reading every sample. "Occ." counts each occurrence. "Samples" is how many of the 24 samples contain the tell at least once. The order is by occurrences, with sample count breaking ties.

| # | Tell | Occ. | Samples | Status |
|---|---|---|---|---|
| 1 | Formatting by rule (bold label on every item, emoji at the start of each line, emoji + ALL-CAPS headline) | 15 | 7 | starting list |
| 2 | Contrast staging, mostly in a new form: *không cần X, chỉ cần Y* / *X, không phải Y* | 11 | 6 | starting list; new form |
| 3 | Staged closers (start-small pep line, *Một lần nữa, …*, empty *sẵn sàng hỗ trợ*) | 9 | 9 | starting list; new forms |
| 4 | Forced triads and anaphora | 9 | 4 | starting list |
| 5 | Translated syntax (*được thiết kế/được tạo ra để*, *của bạn* that could be dropped, *một cách*) | 8 | 3 | starting list |
| 6 | Staged openers (rhetorical question, "many people think…" setup, *Dưới đây là*) | 7 | 6 | starting list; new form |
| 7 | Markdown in channels that don't render it (`**bold**` in Facebook posts and emails) | 7 | 7 | **new** |
| 8 | Inflation | 5 | 5 | starting list |
| 9 | Problem → *giải quyết đúng việc đó* pivot | 3 | 3 | **new** |
| 10 | Same-rhythm sentences | 2 | 2 | starting list |
| 11 | Chatbot leftovers inside the text | 2 | 2 | starting list |
| — | Linking-word padding (*Bên cạnh đó, Ngoài ra, Đồng thời, Hơn thế nữa, Không những vậy*) | 0 | 0 | starting list, **not seen** |
| — | Sino-Vietnamese / verb stacking (*thực hiện việc, tiến hành, đóng vai trò quan trọng, góp phần nâng cao*) | 0 | 0 | starting list, **not seen** |

Seen, but in too few samples to count as tells (fewer than 3 occurrences, or normal for the genre): *Thứ nhất… Thứ năm* enumeration (1 sample), *Thay mặt [công ty], chúng tôi…* (2, normal for Vietnamese business email), and the en dash used only in titles (`Tên – khẩu hiệu`, 4). The corpus has no em dashes.

### Per model

| Model | Occurrences | Samples with none |
|---|---|---|
| Haiku | 39 (8 samples) | 0 |
| Sonnet | 20 (8 samples) | blog-01, facebook-01, gioi-thieu-san-pham-01 |
| Opus | 19 (8 samples) | gioi-thieu-san-pham-03, gioi-thieu-san-pham-06, facebook-06 |

Haiku is the most marked. Its product pages and the Facebook anniversary post use almost every pattern. Six of the 24 samples have no tells.

## Quotes per tell

**1. Formatting by rule**
- `- **Tưới nước:** mỗi ngày một lần…` / `- **Bón phân:** …` / `- **Sâu bệnh:** …` (blog-04-sonnet; four lists like this in one post)
- `✅ Truyện tranh, truyện cổ tích…` … `❌ Sách rách mất trang, ẩm mốc` … `📍 Mang tới:` (facebook-04-sonnet)
- `🌸 **MỪNG 20/10 – GIẢM 30% TOÀN BỘ DỊCH VỤ** 🌸` (facebook-03-opus)

**2. Contrast staging.** The spec's forms *không chỉ… mà còn* and *không phải… mà là* do not occur at all. The same move shows up as a negation followed by a reassurance:
- *"Bạn không cần hiểu từng chữ, chỉ cần hiểu ý chính."* (blog-02-haiku)
- *"Không cần đắt, chỉ cần vừa chân, đế mềm và có độ bám."* (blog-03-opus; this post has four of these)
- *"Đó là lỗi của chúng tôi trong việc dự trù và thông báo, không phải lỗi của anh/chị."* (email-04-sonnet)

**3. Staged closers.** *Tóm lại*, *Có thể nói* and *Hy vọng bài viết…* do not occur. What does occur:
- *"Tối nay, sau bữa cơm, hãy xỏ giày và đi một vòng quanh khu nhà. Vậy là được rồi."* (blog-03-opus)
- *"Bạn bắt đầu từ hôm nay với 5 phút là đã đi trước những người còn đang chờ ngày rảnh."* (blog-02-haiku)
- *"Một lần nữa, chúng tôi xin lỗi anh/chị, và cảm ơn anh/chị đã kiên nhẫn chờ đợi."* (email-04-sonnet)

**4. Forced triads and anaphora**
- *"Làm việc nhanh hơn, ít sai hơn, về đúng giờ"* (gioi-thieu-san-pham-05-haiku, headline)
- *"đi chậm, ăn nhiều, và một chút tiếc nuối"* (blog-05-haiku, headline; the post never mentions any regret)
- *"Có những buổi mưa tầm tã, có những buổi nắng cháy da, có những hôm ai cũng mệt rã rời…"* (facebook-02-haiku)

**5. Translated syntax**
- *"Ví Xanh được thiết kế đơn giản, dễ dùng…"* (gioi-thieu-san-pham-02-haiku)
- *"theo dõi chi tiêu hằng ngày một cách nhanh gọn"* (gioi-thieu-san-pham-02-haiku)
- *"Dữ liệu của bạn được mã hóa và chỉ bạn mới truy cập được."* (gioi-thieu-san-pham-02-haiku)

**6. Staged openers.** *Hãy cùng tìm hiểu* and *Trong thời đại 4.0* do not occur. *Bạn có bao giờ…?* occurs twice. A new form, the "many people think X" setup, occurs three times:
- *"Bạn có bao giờ mất cả buổi chiều chỉ để gộp dữ liệu từ ba file khác nhau…?"* (gioi-thieu-san-pham-05-haiku)
- *"Nhiều người nghĩ muốn khỏe thì phải đăng ký phòng gym… Thật ra, chỉ cần đi bộ đều đặn…"* (blog-03-opus)
- *"Mình từng nghĩ muốn học tiếng Anh thì phải có vài tiếng rảnh mỗi tối…"* (blog-02-haiku)

**7. Markdown in channels that don't render it.** Facebook and most email clients show `**` as literal asterisks. 5 of 6 emails and 2 of 6 Facebook posts have them:
- `**Tiêu đề: Thông báo điều chỉnh giá gói dịch vụ từ [ngày/tháng]**` (email-01-sonnet)
- `**Chuyện gì đã xảy ra:** … **Tình trạng hiện tại:** … **Chúng tôi muốn bù đắp:**` (email-04-sonnet)
- `Chúng mình đang nhận **sách cũ** để gửi lên…` (facebook-04-sonnet)

**8. Inflation.** None of the spec's words occur (*vô cùng, cực kỳ, hoàn hảo, đột phá, tối ưu, vượt trội, hàng đầu, trải nghiệm tuyệt vời*). The one *hoàn hảo* in the corpus is negated (*"không cần một khoảng thời gian hoàn hảo"*), so I did not count it. What occurs is milder:
- *"ý kiến của anh/chị có ý nghĩa rất lớn với chúng tôi"* (email-05-haiku)
- *"Hôm nay là một cột mốc đáng nhớ của cả câu lạc bộ"* (facebook-02-haiku)
- *"Bắt đầu quản lý tài chính thông minh hơn ngay hôm nay."* (gioi-thieu-san-pham-02-haiku)

**9. Problem → solution pivot**
- *"Ví Xanh được tạo ra để giải quyết đúng việc đó."* (gioi-thieu-san-pham-02-haiku)
- *"Khóa học này được thiết kế để giải quyết đúng những việc đó."* (gioi-thieu-san-pham-05-haiku)
- *"Phần mềm kế toán trên đám mây giải quyết khá gọn những chuyện như vậy."* (blog-06-opus)

**10. Same-rhythm sentences**
- *"Thứ nhất, gắn việc học… Thứ hai, ưu tiên… Thứ ba, nghe và đọc… Thứ tư, đừng đặt… Thứ năm, chấp nhận…"*. Each paragraph has the same shape: imperative, reason, payoff (blog-02-haiku).
- *"Cảm ơn tất cả các thành viên… Cảm ơn những người đã đi trước… Và cảm ơn cả những người mới…"* (facebook-02-haiku)

**11. Chatbot leftovers**
- *"(Thông số trong ngoặc vuông cần thay bằng số liệu thật của sản phẩm trước khi đăng.)"* (gioi-thieu-san-pham-04-sonnet)
- `[Nút: Tải ứng dụng miễn phí] [Nút: Xem bảng giá]` (gioi-thieu-san-pham-02-haiku)

## How I tagged

- I read each sample in full. Tells were counted by hand, then the tally was computed from a list of (tell, sample, quote) entries. I used grep only to look for the spec's literal phrases and to confirm that the zero counts really are zero.
- **Linking words:** a linker counts as padding only if it opens a sentence without adding a real relation. All linkers in the corpus did real work: *Vì vậy*, *Trong khi đó*, *Ngược lại*, *Dù vậy*, *Có điều*. So the count is 0, and that zero is a finding, not a gap.
- **Contrast:** a plain "without" (*mà không phải gọi ai*, *không cần mang máy theo*) does not count. A sentence counts when it sets up an expectation and knocks it down for effect (*không cần X, chỉ cần Y*). An honest caveat that gives information does not count, e.g. gioi-thieu-san-pham-04: *"bạn không nên kỳ vọng im lặng tuyệt đối"*.
- **Triads:** concrete lists of real items do not count (*đồ ăn, động vật, gia đình*; *rủ mẹ, chị gái, bạn thân*). Evaluative or rhythmic triples and repeated sentence frames do count. Conventional Tết wishes do not count.
- **Inflation:** *rất* appears 13 times, and most uses are ordinary (*rất hợp*, *rất ít công ty*). Only claims larger than the content supports count.
- **Translated syntax:** *của bạn* counts only where dropping it loses nothing (*khoản chi đầu tiên của bạn*). It does not count where it is needed (*gói của bạn vẫn giữ nguyên*) or idiomatic (*bạn của bạn*).
- **Formatting:** bold section headings in a blog or product page are normal web formatting and do not count. The tell is a bold label on *every* bullet, or an emoji on every line.
- **Closers:** a call to action that is the point of the genre (register, call the hotline) does not count. A generic pep line or a repeated thank-you or apology does.
- Square-bracket placeholders (`[Tên quán]`, 167 of them in 16 samples) are not counted as a tell. The writer is meant to fill them, and the humanizer must leave them alone.

## What this means for the catalogue

1. **Reorder the spec's list.** In this corpus, formatting, contrast staging, closers and triads lead. Linking-word padding and Sino-Vietnamese stacking did not occur once. Keep them in the catalogue, because they are documented tells of Vietnamese AI text in general, but list them last and mark them *yếu nếu đứng một mình* until another corpus shows them.
2. **Change the examples.** Contrast staging should lead with *không cần X, chỉ cần Y*. Staged closers should include the start-small pep line and *Một lần nữa, …*. Staged openers should add the "many people think X" setup. Inflation should be about claims larger than the content (*có ý nghĩa rất lớn*, *cột mốc đáng nhớ*), not a word list.
3. **Add two patterns.** Markdown in Facebook and email: strip `**`, or say it shows as literal asterisks. The problem → *giải quyết đúng việc đó* pivot in sales copy.

## Limits

- **Claude only, through a coding-agent harness.** The generators ran as Claude Code subagents, not in a plain chat app and not through the bare API. The harness system prompt may make the prose plainer than what a user gets from a chat app. The corpus also includes no GPT, Gemini or local Vietnamese models, which are often the source of *Bên cạnh đó*, *Ngoài ra* and *vô cùng*. The zero counts in this corpus may not hold for those models.
- 24 samples, one tagger, no second rater. The counts are small. Treat ranks 8–11 as roughly tied.
- Human-written controls are not part of this step. Same-rhythm and triads, in particular, need a control comparison before they can be trusted.
