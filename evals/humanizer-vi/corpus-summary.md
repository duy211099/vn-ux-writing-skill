# AI-Vietnamese corpus: tell frequencies

Built 2026-11-27 for `humanizer-vi`. The table below sets the order of `references/dau-hieu-ai.md`. Raw samples are in `corpus/` and are the eval inputs for Task 6.

## Sources and samples

**Claude only.** OpenAI was tried through the `codex` CLI (v0.172, model `gpt-6.2-sol`) and failed with `401 Unauthorized: Missing bearer or basic authentication` (`codex login status`: "Not logged in"), so the corpus has no OpenAI samples. No other model provider was available.

There are two routes, with about the same amount of text from each:

| Source | How it was run | Samples | Words |
|---|---|---|---|
| **Subagent** (`sonnet`, `haiku`, `opus`) | Fresh Claude Code subagents. They carry the Claude Code system prompt, and each got four plain requests in one message. | 24 (8 per model) | ~8,200 |
| **Bare** (`sonnet-bare`, `haiku-bare`, `opus-bare`) | `claude -p --model <m> --system-prompt "You are a helpful assistant." --tools ""`, run from an empty temp dir with no settings, one request per call. This is closest to a plain chat app. | 16 (Sonnet 8, Haiku 4, Opus 4) | ~8,100 |

| Genre | Subagent | Bare | Total |
|---|---|---|---|
| `blog` | 01–06 | 07–10 | 10 |
| `gioi-thieu-san-pham` | 01–06 | 07–10 | 10 |
| `facebook` | 01–06 | 07–10 | 10 |
| `email` | 01–06 | 07–10 | 10 |

Files are named `<genre>-<nn>-<source>.md`. Each starts with a one-line comment giving the model, the route and the exact prompt. Every topic is different, and all files are NFC. The prompts were plain user requests (*"Viết bài blog về món phở Hà Nội cho trang ẩm thực."*) with no mention of style or AI.

Bare replies are kept verbatim, including the chatbot framing around them ("Dưới đây là…", offers to revise), because users paste exactly that. Three of the six subagent replies added a note to the user after the pieces. I removed those notes, since four pieces arrived in one reply. Their leftovers count is therefore slightly low.

## Results

I read every sample. "Occ." counts each occurrence. "Samples" is how many of the 40 samples contain the tell at least once. Rows are sorted by total occurrences.

| # | Tell | Occ. | Samples /40 | Subagent occ. (/24) | Bare occ. (/16) | Status |
|---|---|---|---|---|---|---|
| 1 | Formatting by rule: bold label on every item, emoji at the start of every line or heading, emoji + ALL-CAPS headline, Title Case headings, bold phrases inside prose | 64 | 19 | 15 (7) | 49 (12) | starting list |
| 2 | Inflation | 34 | 13 | 5 (5) | 29 (8) | starting list |
| 3 | Staged closers: *Lời kết/Kết luận* + moral, start-small pep line, "Tag ngay…/bình luận nhé" bait, *Một lần nữa, …*, *ngay hôm nay* | 28 | 21 | 9 (9) | 19 (12) | starting list; new forms |
| 4 | Forced triads and anaphora | 27 | 13 | 9 (4) | 18 (9) | starting list |
| 5 | Chatbot leftovers: framing line, multiple versions, offer to revise, notes to the user | 26 | 16 | 2 (2) | 24 (14) | starting list |
| 6 | Contrast staging: *không cần X, chỉ cần Y*, *X, không phải Y*, *không chỉ… mà còn* | 21 | 10 | 11 (6) | 10 (4) | starting list; new form |
| 7 | Translated syntax: *sự bất tiện/sự thông cảm*, *rất vui mừng thông báo rằng*, *Nếu có bất kỳ thắc mắc nào*, *được thiết kế để*, *của bạn* that could be dropped, *Điều này* opener | 18 | 9 | 9 (4) | 9 (5) | starting list |
| 8 | Staged openers: rhetorical question, *Dưới đây là…*, "Có những X…" aphorism, "many people think X", *Lời đầu tiên* | 17 | 14 | 7 (6) | 10 (8) | starting list; new forms |
| 9 | Markdown `**` in Facebook posts and emails | 14 | 14 | 7 (7) | 7 (7) | **new** |
| 10 | Stock verb *mang đến / mang lại* | 7 | 5 | 0 | 7 (5) | **new** |
| 11 | Problem → "we'll handle it" pivot (*giải quyết đúng việc đó*, *Hãy để chúng tôi lo*) | 5 | 5 | 3 (3) | 2 (2) | **new** |
| 12 | Vague authority: *Nghiên cứu cho thấy…*, *Nhiều người thành đạt chia sẻ…*, *Người sành phở thường nói* | 4 | 2 | 0 | 4 (2) | **new** |
| 13 | Same-rhythm sentences | 3 | 3 | 2 (2) | 1 (1) | starting list |
| 14 | Sino-Vietnamese / verb stacking (*tiến hành*, *nhằm nâng cao*, *quá trình… hoàn tất*) | 3 | 1 | 0 | 3 (1) | starting list |
| — | Linking-word padding (*Bên cạnh đó, Ngoài ra, Đồng thời, Hơn thế nữa, Không những vậy*) | 0 | 0 | 0 | 0 | starting list, **not seen as padding** |

### By source

| Source | Occurrences | Per 1,000 words | Samples with none |
|---|---|---|---|
| Subagent Haiku | 39 | — | 0 / 8 |
| Subagent Sonnet | 21 | — | 3 / 8 |
| Subagent Opus | 19 | — | 3 / 8 |
| **Subagent, all** | **79** | **≈ 9.6** | 6 / 24 |
| Bare Sonnet | 93 | — | 0 / 8 |
| Bare Haiku | 48 | — | 0 / 4 |
| Bare Opus | 51 | — | 0 / 4 |
| **Bare, all** | **192** | **≈ 23.7** | 0 / 16 |

The route matters more than the model. With the Claude Code system prompt, all three models write fairly plain Vietnamese. Bare, all three produce about 2.5 times as many tells per word. Every bare sample has tells, and the heaviest is 23 in one blog post (blog-09-haiku-bare). Formatting, inflation, chatbot framing and closers account for most of the gap.

### Do linking-word padding and Sino-Vietnamese stacking appear outside the subagents?

- **Sino-Vietnamese stacking: yes, but only once.** All three occurrences are in one bare formal email (email-07-sonnet-bare): *"Nhằm nâng cao chất lượng và đảm bảo hệ thống vận hành ổn định, an toàn, chúng tôi sẽ tiến hành bảo trì…"*. That email also has the related nominalizations *"hạn chế tối đa sự bất tiện"* and *"sự thông cảm"*, counted under translated syntax. The pattern seems tied to the formal *Quý khách* register.
- **Linking-word padding: the words appear, but not as padding.** *"🌟 Ngoài ra, còn có:"* (facebook-09-haiku-bare) introduces a genuinely new list of events. *"Đồng thời, nên kiểm tra kỹ các thành phần…"* (gioi-thieu-san-pham-09-haiku-bare) adds a separate instruction. Under the brief's rule, neither counts. No sample opens sentence after sentence with *Bên cạnh đó / Ngoài ra / Hơn thế nữa*.
- Other spec words also appear only in bare samples: *tối ưu* ("để đạt hiệu quả tối ưu"), *tuyệt vời* ("một không gian đọc sách tuyệt vời"), *cực* ("GIẢM GIÁ CỰC SỐC"), *trong thời đại…* (mid-sentence, not an opener), *Điều này* as a sentence opener, and *không chỉ… mà còn* once.

## Quotes per tell

**1. Formatting by rule**
- `### ✅ Điểm nổi bật` / `### 🔧 Công nghệ lọc` / `### 📱 Tiện ích thông minh` … an emoji on every heading (gioi-thieu-san-pham-07-sonnet-bare)
- `# Dịch Vụ Dọn Nhà Theo Giờ: Sạch Bóng Không Gian, Thảnh Thơi Cuộc Sống` (gioi-thieu-san-pham-10-opus-bare; Title Case)
- `- **Tưới nước:** …` / `- **Bón phân:** …` / `- **Sâu bệnh:** …` (blog-04-sonnet)

**2. Inflation**
- *"một không gian đọc sách tuyệt vời cùng hàng ngàn đầu sách với giá ưu đãi chưa từng có!"* (facebook-09-haiku-bare)
- *"tạo nên những hạt Robusta chất lượng bậc nhất… hương vị mộc mạc, mạnh mẽ của vùng đất đại ngàn"* (gioi-thieu-san-pham-08-sonnet-bare)
- *"ý kiến của anh/chị có ý nghĩa rất lớn với chúng tôi"* (email-05-haiku)

**3. Staged closers**
- *"Sau vài năm, bạn sẽ cảm ơn chính mình vì quyết định hôm nay."* (blog-07-sonnet-bare). All four bare blogs end with a `## Lời kết` or `## Kết luận` section.
- *"Một ngôi nhà sạch là khởi đầu cho một cuộc sống khỏe mạnh và hạnh phúc."* (gioi-thieu-san-pham-10-opus-bare)
- *"👇 Tag ngay người bạn muốn cùng "dậy sớm, sống khỏe" nhé!"* (facebook-10-opus-bare). All three bare promo posts end with "Tag…".

**4. Forced triads and anaphora**
- *"giải pháp linh hoạt, tiện lợi và tiết kiệm"* … *"sạch sẽ, gọn gàng, thơm tho"* (gioi-thieu-san-pham-10-opus-bare)
- *"là bữa sáng quen thuộc, là món ăn khuya sau một ngày dài, là thứ để nhớ về khi xa quê"* (blog-08-sonnet-bare)
- *"đi chậm, ăn nhiều, và một chút tiếc nuối"* (blog-05-haiku; the post never mentions any regret)

**5. Chatbot leftovers**
- *"Dưới đây là vài phiên bản để bạn chọn tùy phong cách nhé:"* followed by three versions (facebook-08-sonnet-bare)
- *"Nếu bạn cho mình biết thời gian cụ thể, tên dịch vụ và tên công ty, mình có thể điền sẵn…"* (email-07-sonnet-bare). 14 of the 16 bare replies end with an offer or a note like this.
- *"(Thông số trong ngoặc vuông cần thay bằng số liệu thật của sản phẩm trước khi đăng.)"* (gioi-thieu-san-pham-04-sonnet)

**6. Contrast staging**
- *"Bạn không cần hiểu từng chữ, chỉ cần hiểu ý chính."* (blog-02-haiku)
- *"Tiết kiệm không đòi hỏi bạn phải sống khắc khổ. Chỉ cần ghi chép chi tiêu…"* (blog-07-sonnet-bare)
- *"Có những món ăn không chỉ để no bụng, mà còn kể một câu chuyện về cả một vùng đất."* (blog-08-sonnet-bare; the corpus's only *không chỉ… mà còn*)

**7. Translated syntax**
- *"Chúng tôi chân thành xin lỗi về sự bất tiện này và rất mong nhận được sự thông cảm từ Quý khách."* (email-07-sonnet-bare)
- *"chúng tôi rất vui mừng thông báo rằng… anh/chị sẽ là một bổ sung giá trị cho đội ngũ"* (email-08-sonnet-bare)
- *"Ví Xanh được thiết kế đơn giản, dễ dùng…"* (gioi-thieu-san-pham-02-haiku)

**8. Staged openers**
- *"Bạn có bao giờ nghĩ rằng chỉ 20 phút mỗi ngày có thể thay đổi cách bạn suy nghĩ, làm việc và sống?"* (blog-09-haiku-bare)
- *"Có những nơi bạn đến một lần rồi thôi. Hội An thì khác…"* (blog-10-opus-bare)
- *"Nhiều người nghĩ muốn khỏe thì phải đăng ký phòng gym… Thật ra, chỉ cần đi bộ đều đặn…"* (blog-03-opus)

**9. Markdown in channels that don't render it.** Facebook and most email clients show `**` as literal asterisks. 9 of 10 emails and 5 of 10 Facebook posts have them.
- `**Tiêu đề:** Thông báo trúng tuyển vị trí Nhân viên Marketing` (email-08-sonnet-bare)
- `Chúng mình đang nhận **sách cũ** để gửi lên…` (facebook-04-sonnet)
- `quán chính thức ra mắt **MENU LẨU MÙA ĐÔNG MỚI**` (facebook-07-sonnet-bare)

**10. *mang đến / mang lại***
- *"Son môi [Tên thương hiệu] mang đến màu sắc rực rỡ"* (gioi-thieu-san-pham-09-haiku-bare)
- *"Dịch vụ dọn nhà theo giờ của chúng tôi mang đến giải pháp linh hoạt…"* (gioi-thieu-san-pham-10-opus-bare)
- *"Đọc sách là một trong những thói quen đơn giản nhất nhưng mang lại giá trị lâu dài nhất."* (blog-09-haiku-bare)

**11. Problem → "we'll handle it" pivot**
- *"Ví Xanh được tạo ra để giải quyết đúng việc đó."* (gioi-thieu-san-pham-02-haiku)
- *"Hãy để chúng tôi lo phần đó, còn bạn dành thời gian cho gia đình…"* (gioi-thieu-san-pham-10-opus-bare)
- *"Hãy để [Tên phòng gym] giúp bạn thay đổi điều đó!"* (facebook-10-opus-bare)

**12. Vague authority**
- *"Nghiên cứu cho thấy đọc sách có thể làm giảm mức căng thẳng hiệu quả…"* (blog-09-haiku-bare)
- *"Nhiều người thành đạt chia sẻ rằng thói quen đọc sách là một trong những yếu tố then chốt…"* (blog-09-haiku-bare)
- *"Người sành phở thường nói: "Phở ngon hay dở là ở nước dùng.""* (blog-08-sonnet-bare)

**13. Same rhythm**
- *"Thứ nhất, gắn việc học… Thứ hai, ưu tiên… Thứ ba, nghe và đọc… Thứ tư… Thứ năm…"*, each paragraph with the same shape (blog-02-haiku)
- Seven sections each built on "Đọc … giúp bạn …" (blog-09-haiku-bare)

**14. Sino-Vietnamese stacking**
- *"Nhằm nâng cao chất lượng và đảm bảo hệ thống vận hành ổn định, an toàn, chúng tôi sẽ tiến hành bảo trì định kỳ hệ thống"* (email-07-sonnet-bare)
- *"Dịch vụ sẽ được khôi phục ngay sau khi quá trình bảo trì hoàn tất."* (email-07-sonnet-bare)

## How I tagged

- I read each sample in full. Each occurrence went into a list of (tell, sample, quote), and the tables were computed from that list. Grep was used only to look for the spec's literal phrases and to check the zero counts.
- **Linking words:** a linker counts as padding only if it adds no real relation. *Vì vậy*, *Trong khi đó*, *Ngược lại*, *Dù vậy*, *Có điều*, and the *Ngoài ra* and *Đồng thời* above all add something real, so none of them count.
- **Contrast:** a plain "without" (*mà không phải gọi ai*) does not count. An honest caveat does not count (*"bạn không nên kỳ vọng im lặng tuyệt đối"*), and neither does a factual correction (*"thuộc thành phố Đà Nẵng chứ không còn thuộc tỉnh Quảng Nam"*). What counts is an expectation set up and knocked down for effect.
- **Triads:** concrete lists of real items do not count (*phòng ngủ, phòng khách, phòng làm việc*; *gia đình, bạn bè, đồng nghiệp*), nor do product spec lists or tasting notes. Evaluative or rhythmic triples and repeated frames do count.
- **Inflation:** *rất* is mostly ordinary (*rất hợp*, *rất ít công ty*). Spec numbers (*lọc 99,97%*) do not count. Claims larger than the content supports do count, including slogan subtitles.
- **Translated syntax:** *của bạn* counts only where it can be dropped without loss. *sự + noun* counts only in apology or thanks formulas (*sự bất tiện*, *sự chậm trễ*, *sự thông cảm*), not in ordinary nouns (*sự cố*, *sự kiện*) or literary uses (*chính sự giản dị ấy*). *Thay mặt [công ty]…* is a normal Vietnamese business opener and does not count.
- **Formatting:** bold section headings in a blog or product page are normal web formatting. The tell is a bold label on *every* item, an emoji on every line or heading, Title Case, or bold phrases inside running prose. In Facebook and email, `**` is counted under row 9 instead.
- **Closers:** a call to action that is the point of the genre (register, the hotline) does not count. A generic moral, pep line, engagement bait, urgency line, or repeated thank-you or apology does count.
- **Same rhythm:** counted only when the same frame opens three or more sentences or paragraphs in a row.
- **Chatbot leftovers:** each distinct framing line, note or offer counts once.
- Square-bracket placeholders (`[Tên quán]`, present in most samples) are not counted. The writer is meant to fill them, and the humanizer must leave them alone.
- The bare set was tagged after the subagent set. The *sự + noun* rule surfaced while tagging it, so I re-checked the subagent set and added one hit (email-04-sonnet, *"sự chậm trễ này"*).

## What this means for the catalogue

1. **Order by the combined table.** Formatting, inflation, closers, triads and chatbot framing lead. Contrast staging, translated syntax and openers follow. Linking-word padding and Sino-Vietnamese stacking go last, marked *yếu nếu đứng một mình*. Stacking appears only in formal *Quý khách* email, so the catalogue can name that register.
2. **Update the examples.** Inflation should describe claims larger than the content (*chưa từng có*, *bậc nhất*, *đại ngàn*), not just a word list. Closers should include *Lời kết* + moral, "Tag ngay…" and *ngay hôm nay*. Contrast should lead with *không cần X, chỉ cần Y*. Openers should include the "Có những X…" aphorism and *Dưới đây là*.
3. **Add four patterns.** Markdown in Facebook and email; *mang đến / mang lại*; the problem → "we'll handle it" pivot; vague authority (*Nghiên cứu cho thấy*). The last has only 4 hits in 2 samples and is the weakest of the four.
4. **Chatbot leftovers are common in pasted chat output** (14 of 16 bare replies). The skill should strip the framing and offers but never touch `[placeholders]`.

## Limits

- **Claude only.** Codex/OpenAI failed on auth, and no Gemini or local Vietnamese model was available. Linking-word padding is widely reported in Vietnamese AI text from other models, and neither Claude route produced it, so its rank here may not hold for other models.
- **Two routes, one family.** The bare route is the closer stand-in for what users paste. The subagent route undercounts tells by about 2.5× per word. Evals in Task 6 should draw mainly on the bare samples.
- 40 samples and one tagger, with no second rater. Treat rows 10–14 as roughly tied.
- No human-written controls yet. Triads and same rhythm, in particular, need a control comparison before they can be trusted.
