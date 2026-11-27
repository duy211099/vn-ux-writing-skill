# viet-writing

**Bộ skill viết tiếng Việt cho AI agent.** Plugin Claude Code giúp agent viết chữ giao diện nghe như người Việt viết, sửa văn bản dài cho hết giọng AI, và giữ một giọng văn chung cho cả dự án. Có thêm hai lệnh để bạn tự rà phần vừa sửa hoặc cả repo.

Dành cho lập trình viên làm sản phẩm một mình, không có người viết nội dung. Bạn không cần biết UX writing: skill tự chọn cách xưng hô và giọng văn hợp với ứng dụng, báo lại một dòng, rồi giữ nguyên cho cả dự án.

```
Trước → Sau — lý do
"Đã xảy ra lỗi. Vui lòng thử lại sau." → "Chưa tải được ảnh lên. Ảnh vượt quá 5 MB. Chọn ảnh nhỏ hơn rồi thử lại." — Nói rõ việc gì hỏng, vì sao, và làm gì tiếp.
"Bạn có chắc chắn muốn xóa ảnh này không?" [Có] [Không] → "Xóa ảnh này?" [Xóa] [Hủy] — Câu hỏi ngắn; nút ghi rõ hành động.
```

[English below](#english)

---

## Các skill

| Skill | Làm gì | Khi nào chạy |
|---|---|---|
| [`ux-writing-vi`](skills/ux-writing-vi/) | Viết và sửa chữ giao diện: nút, nhãn, lỗi, trạng thái trống, hộp thoại, thông báo đẩy. | Tự chạy khi agent đụng tới chuỗi hiển thị tiếng Việt. |
| [`humanizer-vi`](skills/humanizer-vi/) | Bỏ dấu hiệu "AI viết" trong bài blog, email, README, giới thiệu sản phẩm mà không đổi ý. | Tự chạy khi bạn nhờ sửa cho tự nhiên, hoặc sau khi agent viết một đoạn tiếng Việt dài. |
| [`style-vi`](skills/style-vi/) | Tạo và sửa file giọng văn `docs/giong-van.md` mà mọi skill khác cùng đọc. | Tự chạy khi bạn hỏi về giọng văn, xưng hô, hoặc khi skill khác cần file này. |
| [`review`](skills/review/) | Rà chữ tiếng Việt trong phần bạn vừa thay đổi. | Chỉ khi bạn gõ `/viet-writing:review`. |
| [`analyze`](skills/analyze/) | Rà toàn bộ chữ tiếng Việt trong repo, chú ý tính thống nhất. | Chỉ khi bạn gõ `/viet-writing:analyze`. |

## Cài đặt

### Cách 1: Plugin Claude Code (nên dùng)

Một lần cài có đủ năm skill, kể cả hai lệnh `review` và `analyze`. Trong Claude Code:

```
/plugin marketplace add duy211099/vn-ux-writing-skill
/plugin install viet-writing@viet-writing
```

Hoặc từ terminal:

```bash
claude plugin install viet-writing --marketplace duy211099/vn-ux-writing-skill
```

Đã clone repo về máy thì thêm marketplace bằng đường dẫn: `/plugin marketplace add ./vn-ux-writing-skill`.

### Cách 2: Skills CLI (từng skill)

```bash
npx skills add duy211099/vn-ux-writing-skill --list                          # xem danh sách, không cài
npx skills add duy211099/vn-ux-writing-skill --skill ux-writing-vi -g -y     # cài một skill
```

`-g` cài cho mọi dự án của bạn, `-y` bỏ qua bước hỏi xác nhận. Cách này hợp với `ux-writing-vi`, `humanizer-vi`, `style-vi`. Hai lệnh `review` và `analyze` cần cài bằng plugin (Cách 1).

### Cách 3: Cài thủ công

```bash
git clone https://github.com/duy211099/vn-ux-writing-skill.git
mkdir -p ~/.claude/skills
ln -s "$PWD/vn-ux-writing-skill/skills/ux-writing-vi" ~/.claude/skills/ux-writing-vi
ln -s "$PWD/vn-ux-writing-skill/skills/humanizer-vi" ~/.claude/skills/humanizer-vi
ln -s "$PWD/vn-ux-writing-skill/skills/style-vi" ~/.claude/skills/style-vi
```

Dùng symlink thì sau này chỉ cần `git pull` là có bản mới. Không muốn symlink thì chép thư mục: `cp -r vn-ux-writing-skill/skills/ux-writing-vi ~/.claude/skills/`.

**Chỉ cài cho một dự án:** đặt thư mục skill vào `.claude/skills/` trong repo đó (và commit nếu muốn cả nhóm cùng dùng).

**Agent khác** (Codex, Cursor, Gemini CLI…): chép thư mục skill vào thư mục skills của agent đó. Nhiều agent đọc chung `~/.agents/skills/`.

### Đã chuyển sang `skills/`

Nếu bạn đã cài `ux-writing-vi` bằng symlink từ bản cũ: các skill giờ nằm trong `skills/`, nên sau `git pull` symlink cũ sẽ trỏ vào thư mục không còn tồn tại. Tạo lại:

```bash
ln -sfn "$PWD/vn-ux-writing-skill/skills/ux-writing-vi" ~/.claude/skills/ux-writing-vi
```

File giọng văn `docs/ux-voice.md` trong dự án của bạn vẫn dùng được, không cần đổi tên.

### Kiểm tra đã cài được chưa

Mở Claude Code mới và hỏi:

```
Có skill nào để viết chữ giao diện tiếng Việt không?
```

Claude sẽ nhắc đến `ux-writing-vi`. Bạn cũng có thể gọi thẳng bằng `/ux-writing-vi` (hoặc `/viet-writing:ux-writing-vi` nếu cài bằng plugin).

## Cách dùng

### Viết chữ giao diện

Làm việc bình thường trong repo có tiếng Việt (`vi.json`, `vi.yml`, `*_vi.arb`, `values-vi/strings.xml`, `vi.lproj`, hoặc chữ tiếng Việt viết thẳng trong component). Ví dụ:

```
Thêm nút "Đặt lại" cho danh sách đơn cũ, thêm key order.reorder vào en.json và vi.json.
```

`ux-writing-vi` viết tiếng Việt từ ý chứ không dịch từng chữ của chuỗi tiếng Anh, theo mẫu cho từng loại thành phần (lỗi luôn có bước tiếp theo, nút là động từ + đối tượng), giữ nguyên biến như `{{count}}`, `%s`, và chỉ sửa đúng chuỗi được nhờ.

Muốn rà lại chữ có sẵn thì dán chữ, gửi ảnh chụp màn hình, đưa đường dẫn trang web hoặc chỉ vào file. Kết quả trả về theo dạng `Trước → Sau — lý do` cho từng chuỗi.

### Sửa văn bản dài cho tự nhiên

Dán đoạn văn hoặc chỉ vào file, rồi nhờ "viết lại cho tự nhiên", "nghe như AI quá". `humanizer-vi` trả về bản đã sửa và một danh sách ngắn những gì đã đổi. Tên, số liệu, ngày tháng, giá tiền, đường dẫn giữ nguyên. Skill chạy khi bạn nhờ, khi bạn chỉ vào một file, khi bạn chạy `/viet-writing:review` hoặc `/viet-writing:analyze`, hoặc khi một skill khác gọi tới ở bước cuối. Văn bản agent tự viết chưa được rà tự động: muốn rà thì nhờ một câu hoặc chạy lệnh.

### Rà soát bằng lệnh

```
/viet-writing:review            # rà phần thay đổi so với HEAD (đã stage, chưa stage, file mới)
/viet-writing:review main       # so với nhánh hoặc commit khác
/viet-writing:analyze           # rà toàn bộ repo
/viet-writing:analyze src/      # chỉ rà một thư mục hoặc file
```

Cả hai lệnh tách chữ giao diện khỏi văn bản dài và dùng đúng quy tắc cho từng loại. `analyze` còn kiểm tra cả repo có thống nhất không: xưng hô, thuật ngữ, kiểu dấu thanh. Hai lệnh chỉ đề xuất, **không sửa file nào cho đến khi bạn đồng ý**.

Hai lệnh này cần cài bằng plugin (Cách 1), vì chúng gọi `ux-writing-vi` và `humanizer-vi` để rà chữ. Plugin cài cùng lúc ba skill `ux-writing-vi`, `humanizer-vi`, `style-vi` và hai lệnh này.

### File giọng văn `docs/giong-van.md`

Đây là nơi bạn điều khiển giọng của dự án. Lần đầu cần đến, skill tự tạo file này và báo bạn một dòng. Mọi skill trong plugin đều đọc nó, từ chuỗi giao diện đến bài viết dài. Mặc định:

| Lựa chọn | Mặc định | Ngân hàng, bảo hiểm, y tế |
|---|---|---|
| Gọi người dùng | *bạn*, hoặc bỏ đại từ | *quý khách*, hoặc bỏ đại từ |
| Ứng dụng tự xưng | Không ("chúng tôi", "mình") | *chúng tôi* chỉ khi nói về chính sách, pháp lý |
| Giọng | Trung tính, thân thiện | Trang trọng |
| Trợ từ | *nhé* dùng thưa; không *nha*, *ạ* | Không *nhé*; *vui lòng* khi cần |
| Dấu thanh | *xóa, hòa* (hoặc theo repo) | như bên trái |
| Tiền | `100.000đ` | `100.000 VND` |

Muốn đổi thì sửa thẳng file, hoặc nói với agent ("đổi sang gọi quý khách"). Nếu repo của bạn đã dùng sẵn *anh/chị* hay *xoá*, skill theo cách đó thay vì mặc định. Dự án đã có `docs/ux-voice.md` từ bản cũ thì skill dùng luôn file đó.

## Cập nhật và gỡ cài đặt

```bash
# Cập nhật
claude plugin marketplace update viet-writing && claude plugin update viet-writing@viet-writing   # plugin
npx skills update                                  # nếu cài bằng Skills CLI
cd vn-ux-writing-skill && git pull                 # nếu dùng symlink

# Gỡ
claude plugin uninstall viet-writing@viet-writing  # plugin
rm ~/.claude/skills/ux-writing-vi                  # symlink
rm -r ~/.claude/skills/ux-writing-vi               # bản chép
```

## Bên trong có gì

```
.claude-plugin/           # plugin.json, marketplace.json
skills/
├── ux-writing-vi/        # chữ giao diện: quy tắc, mẫu, thuật ngữ, ví dụ trước → sau
├── humanizer-vi/         # dấu hiệu văn AI và cách viết lại
├── style-vi/             # file giọng văn: mẫu và mặc định theo lĩnh vực
├── review/               # /viet-writing:review
└── analyze/              # /viet-writing:analyze
evals/<skill>/            # tình huống đánh giá và kết quả cho từng skill
scripts/                  # check_skill.py, package_skill.py
tests/
```

Các file trong `references/` cũng đọc được như một cẩm nang viết tiếng Việt, kể cả khi không dùng AI.

## Đóng góp

Rất mong nhận góp ý, nhất là những câu "đúng ngữ pháp nhưng nghe như dịch" hay những kiểu văn AI mà skill chưa bắt được. Mở issue hoặc pull request.

Trước khi gửi pull request:

```bash
python3 scripts/check_skill.py --all                # cấu trúc, liên kết, Unicode NFC, độ dài SKILL.md
python3 -m unittest discover -s tests -t .          # test cho các script và manifest
python3 scripts/package_skill.py --all skills dist  # đóng gói mỗi skill thành dist/<tên>.zip
claude plugin validate . --strict                   # kiểm tra manifest plugin
```

Bộ đánh giá hành vi nằm trong `evals/<skill>/` (ví dụ `evals/ux-writing-vi/`): tình huống, repo mẫu, và kết quả so sánh có/không có skill. Nếu bạn sửa quy tắc trong một skill, chạy lại các tình huống liên quan và ghi kết quả.

## Nguồn và giấy phép

- Khung bốn tiêu chuẩn (có mục đích, ngắn gọn, tự nhiên, rõ ràng) và các mẫu nội dung của `ux-writing-vi` phỏng theo [UX Writing Skill](https://github.com/content-designer/ux-writing-skill) của Christopher Greer (MIT).
- Quy tắc ngôn ngữ (viết hoa, dấu câu, định dạng số, tránh dịch từng chữ) được diễn đạt lại từ [Microsoft Vietnamese Localization Style Guide](https://learn.microsoft.com/globalization/reference/microsoft-style-guides).
- Cấu trúc của `humanizer-vi` (đánh dấu → viết lại → soát dữ kiện → bản cuối) phỏng theo [humanizer](https://github.com/blader/humanizer) của Siqi Chen (MIT). Các mẫu và ví dụ tiếng Việt được viết mới.
- Mọi ví dụ tiếng Việt trong skill được viết mới.

Giấy phép MIT, xem [LICENSE](LICENSE). Mỗi skill cũng có file `LICENSE` riêng, ví dụ [skills/ux-writing-vi/LICENSE](skills/ux-writing-vi/LICENSE).

**Ngoại lệ:** các văn bản đối chứng trong `evals/humanizer-vi/controls/` và file `evals/humanizer-vi/inputs/h12-khong-dau.md` lấy từ Wikipedia tiếng Việt, Tatoeba và văn bản luật. Phần lớn theo giấy phép CC BY-SA hoặc CC BY, không phải MIT. Xem `NOTICE.md` trong từng thư mục để biết giấy phép của từng file. Các file này chỉ dùng để đánh giá và không có trong gói skill.

---

## English

`viet-writing` is a Claude Code plugin of Vietnamese writing skills for AI agents. It's built for solo developers who write their own app text and have no one to check it. The skills make the tone and pronoun decisions for you, tell you in one line, and keep them consistent across the project.

### Skills

- **`ux-writing-vi`**: writes and reviews Vietnamese UI copy (buttons, labels, errors, empty states, dialogs, notifications). Runs on its own when the agent touches Vietnamese UI strings.
- **`humanizer-vi`**: removes signs of AI writing from Vietnamese prose (blog posts, emails, READMEs, product intros) without changing what it says. Runs when you ask, and as the last step after the agent writes Vietnamese prose.
- **`style-vi`**: creates and edits `docs/giong-van.md`, the one voice file per project that every skill reads.
- **`review`**: `/viet-writing:review [ref]` checks the Vietnamese in your current changes (against `HEAD`, or a branch or commit).
- **`analyze`**: `/viet-writing:analyze [path]` checks all Vietnamese in the repo, with a focus on consistency (pronouns, terms, tone-mark style).

`review` and `analyze` run only when you type them, and change no files until you say yes. They need the plugin install, since they use `ux-writing-vi` and `humanizer-vi`.

### Install

```bash
# Claude Code plugin (all five skills)
/plugin marketplace add duy211099/vn-ux-writing-skill
/plugin install viet-writing@viet-writing
# or from a shell:
claude plugin install viet-writing --marketplace duy211099/vn-ux-writing-skill

# Skills CLI, one skill at a time
npx skills add duy211099/vn-ux-writing-skill --list
npx skills add duy211099/vn-ux-writing-skill --skill ux-writing-vi -g -y

# Manually, for Claude Code
git clone https://github.com/duy211099/vn-ux-writing-skill.git
ln -s "$PWD/vn-ux-writing-skill/skills/ux-writing-vi" ~/.claude/skills/ux-writing-vi
```

For other agents, copy a skill folder into that agent's skills folder (often `~/.agents/skills/`).

**Moved to `skills/`:** the skills now live under `skills/`. If you symlinked the old `ux-writing-vi/` folder, the link breaks after `git pull`. Re-link with `ln -sfn "$PWD/vn-ux-writing-skill/skills/ux-writing-vi" ~/.claude/skills/ux-writing-vi`.

### Voice file

The first skill that needs it creates `docs/giong-van.md` and tells you in one line. Edit it to change the voice. Defaults are *bạn* with a neutral-friendly tone, and *quý khách* with a formal tone for banking, insurance and health. Projects that already have `docs/ux-voice.md` from an older version keep using it.

### Development

```bash
python3 scripts/check_skill.py --all
python3 -m unittest discover -s tests -t .
python3 scripts/package_skill.py --all skills dist
claude plugin validate . --strict
```

Behaviour evals live in `evals/<skill>/`.

### Credits

`ux-writing-vi` is adapted from Christopher Greer's [UX Writing Skill](https://github.com/content-designer/ux-writing-skill) (MIT). Language rules are paraphrased from the Microsoft Vietnamese Localization Style Guide. The structure of `humanizer-vi` is adapted from Siqi Chen's [humanizer](https://github.com/blader/humanizer) (MIT). All Vietnamese examples are original. Released under the MIT license.

The control texts in `evals/humanizer-vi/controls/` and `evals/humanizer-vi/inputs/h12-khong-dau.md` come from Vietnamese Wikipedia, Tatoeba and Vietnamese legal texts. Most are under CC BY-SA or CC BY, not MIT. See the `NOTICE.md` in each folder for each file's license. They are used for evals only and are not in the skill packages.
