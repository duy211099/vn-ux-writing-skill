# Baseline results (without the skill)

Run: 2026-11-27. Model: sonnet, one fresh subagent per case (H-05 is three runs), no skill loaded and the Skill tool off. Pasted-mode runners read the user's message from a file in an empty temp dir. File-mode cases ran in a temp git repo (H-10, H-11) or a plain dir (H-13); the verdict is from the file on disk, `git diff` and the final reply. H-14 was given `ux-writing-vi` and the English `humanizer` as the available skills, since `humanizer-vi` did not exist yet.

**Summary:** 6 / 14 cases pass every criterion. The base model is already good at spotting the loud tells (rhetorical openers, *chưa từng có*, *Không chỉ… mà còn*, chatbot framing), keeps most numbers, and refuses the injected instruction. It fails at everything around the rewrite: it rewrites human text it should leave alone, flattens the formal register, edits placeholders and front matter, invents small facts, and writes the user a long report.

| Case | Result | Failed criteria / notes |
|---|---|---|
| H-01 | FAIL | Opens with a paragraph of explanation, not the rewrite. Keeps *"Dưới đây là những thứ mà việc đọc… mang lại"*, *"Có nghiên cứu cho thấy"* and a `## Kết` moral. **Invents a first-person fact:** *"Mình đọc sách đều khoảng 20 phút mỗi ngày."* |
| H-02 | FAIL | **Placeholders changed:** `[Tùy chọn]` → `[Nếu có]`, `[xx dB]` → `[xx] dB`, `[Tên thương hiệu]` → `[Thương hiệu]`, `[số] lớp` → *"Bốn lớp lọc"* (an invented number). Drops *chính hãng 100%*. Emoji headings, caps headline and *siêu êm* are gone. Ends with its own offer to fill in details. |
| H-03 | FAIL | `**Hội sách…**`, `**Ưu đãi**` left in a Facebook post. Date shortened to *28–29/11* (year lost). Changes *"đầu năm"* to *"cuối năm"* on its own judgement. Four-point checklist and an offer after the post. |
| H-04 | FAIL | **Register flattened:** *Kính gửi Quý khách hàng* → *Chào anh/chị*, every *Quý khách* → *anh/chị* ("nghe như công văn"). Keeps *sự bất tiện* and `**Tiêu đề:**`. |
| H-05a (wiki-pho, formal) | FAIL | Rewrote the whole paragraph to remove *được cho là* hedges it judged "quá dè dặt". |
| H-05b (user-sanga, personal) | PASS | "Đoạn này giọng ổn rồi… Mình chỉ đề xuất sửa một chỗ" (*bị ấn tượng mạnh bởi* → *rất ấn tượng với*). |
| H-05c (talk-komsomolets, casual) | FAIL | Smoothed the comment: fixed *Tại nạn*, cut *"Kết luận:"*, reworded both paragraphs, while saying "Đoạn này không cần sửa giọng". |
| H-05 overall | FAIL | 1 of 3 runs passes. |
| H-06 | PASS | Every fact kept, quote word for word. But opens with a diagnosis, keeps `**` labels in a Facebook post, adds *"Trong 3 tiếng"* and *"tự nặn một chiếc cốc"* (from the rhetorical question), asks the user to check the date, offers another version. |
| H-07 | PASS | Read `docs/giong-van.md` unprompted (the README pointed at the project) and wrote with *mình*, no *chúng tôi*. Invented *"Những người đặt nhiều nhất là"* and *"chỉ cần báo trước khi đặt"*; six-point note after the text. |
| H-08 | PASS | No poem; "Mình coi đó là chữ lẫn vào lúc dán". Facts kept. Offers to write the poem separately. |
| H-09 | PASS | *deploy*, *commit*, *API*, *pull request* kept. Drops the name *CI/CD*. Six bullets of explanation plus advice to add an anecdote. |
| H-10 | FAIL | **Front matter changed** (`title:` rewritten). Code, inline code and link targets intact; *90 giây*, *214 test* kept; `## Tóm lại` heading kept. Reply is a seven-bullet report, not one line + `Đã sửa:`. |
| H-11 | PASS | File written back as NFC; tells gone; placeholders kept. Removed the chatbot "Gợi ý" block. |
| H-12 | FAIL | **Added diacritics** to the whole text and rewrote it ("Thêm dấu câu và dấu tiếng Việt"), and **changed a fact**: *"còn sống hay đã chết trận"* → *"còn sống lẫn đã mất"*. |
| H-13 | FAIL | **Overwrote the file outside a git repo without asking** ("ghi đè trực tiếp lên file, nên bản cũ không còn"). Also switched *Kính gửi* to *Chào*. |
| H-14 | PASS | `SKILLS READ: ux-writing-vi`; rewrote `auth.loginError` as a UI error with a next step. |

## Patterns to target in the skill (with quotes)

1. **Human text gets rewritten anyway** (H-05a, H-05c, H-12). The runner says the text is fine, then edits it: *"Đoạn này không cần sửa giọng… Chỉ có vài chỗ nhỏ đáng chỉnh"*. Hedges in an encyclopaedia, *Kết luận:* in a talk comment, a typo and missing diacritics were all "fixed". The skill needs a hard "no tells → return unchanged" rule, and to say that informal spelling, typos and *không dấu* are the writer's register.
2. **Formal register flattened** (H-04, H-13): *Quý khách* → *anh/chị*, *Kính gửi* → *Chào*, justified as "nghe như công văn". Register is the writer's choice, not a tell.
3. **Placeholders and front matter edited** (H-02, H-10). `[Tùy chọn]` → `[Nếu có]`, `[số] lớp` → *Bốn lớp*, `title:` rewritten. Needs a byte-for-byte rule.
4. **Small invented facts** (H-01, H-02, H-06, H-07): *"Mình đọc… 20 phút mỗi ngày"*, *"Bốn lớp lọc"*, *"Trong 3 tiếng"*, *"Những người đặt nhiều nhất là"*. And small lost ones: the year in *28–29/11/2026*, *100%* in *chính hãng 100%*, the name *CI/CD*.
5. **Output shape varies and is long.** Diagnosis before the text, 4–7 bold-labelled bullets, "check this before posting" lists, and an offer to do more in nearly every reply. The user asked for clean text.
6. **Markdown left in channels that don't render it** (H-03, H-04, H-06): `**` in Facebook posts and emails.
7. **Leftover tells after the rewrite** (H-01, H-10): *Dưới đây là*, *Có nghiên cứu cho thấy*, a `Kết`/`Tóm lại` section with a moral.
8. **File mode outside git** (H-13): overwrites and only then mentions that the old version is gone.
