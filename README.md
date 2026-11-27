# ux-writing-vi

**Skill viết chữ giao diện tiếng Việt cho AI agent.** Giúp Claude Code (và các agent hỗ trợ chuẩn Agent Skills) viết nút, nhãn, thông báo lỗi, trạng thái trống, hộp thoại, thông báo đẩy… nghe tự nhiên như người Việt viết, không như bản dịch, và thống nhất trên mọi màn hình.

Dành cho lập trình viên làm sản phẩm một mình, không có người viết nội dung. Bạn không cần biết UX writing: skill tự chọn cách xưng hô và giọng văn hợp với ứng dụng, báo lại một dòng, rồi giữ nguyên cho cả dự án.

```
Trước → Sau — lý do
"Đã xảy ra lỗi. Vui lòng thử lại sau." → "Chưa tải được ảnh lên. Ảnh vượt quá 5 MB. Chọn ảnh nhỏ hơn rồi thử lại." — Nói rõ việc gì hỏng, vì sao, và làm gì tiếp.
"Bạn có chắc chắn muốn xóa ảnh này không?" [Có] [Không] → "Xóa ảnh này?" [Xóa] [Hủy] — Câu hỏi ngắn; nút ghi rõ hành động.
```

[English below](#english)

---

## Cài đặt

### Cách 1: Skills CLI (nhanh nhất)

```bash
npx skills add duy211099/vn-ux-writing-skill@ux-writing-vi -g -y
```

`-g` cài cho mọi dự án của bạn, `-y` bỏ qua bước hỏi xác nhận.

### Cách 2: Claude Code, cài thủ công

```bash
git clone https://github.com/duy211099/vn-ux-writing-skill.git
mkdir -p ~/.claude/skills
ln -s "$PWD/vn-ux-writing-skill/ux-writing-vi" ~/.claude/skills/ux-writing-vi
```

Dùng symlink thì sau này chỉ cần `git pull` là có bản mới. Nếu không muốn symlink, chép cả thư mục:

```bash
cp -r vn-ux-writing-skill/ux-writing-vi ~/.claude/skills/
```

**Chỉ cài cho một dự án:** đặt thư mục vào `.claude/skills/ux-writing-vi` trong repo đó (và commit nếu muốn cả nhóm cùng dùng).

### Cách 3: Agent khác (Codex, Cursor, Gemini CLI…)

Chép thư mục `ux-writing-vi/` vào thư mục skills của agent đó. Nhiều agent đọc chung `~/.agents/skills/`:

```bash
mkdir -p ~/.agents/skills
cp -r vn-ux-writing-skill/ux-writing-vi ~/.agents/skills/
```

### Kiểm tra đã cài được chưa

Mở Claude Code mới và hỏi:

```
Có skill nào để viết chữ giao diện tiếng Việt không?
```

Claude sẽ nhắc đến `ux-writing-vi`. Bạn cũng có thể gọi thẳng bằng `/ux-writing-vi`.

## Cách dùng

Không cần gọi skill. Agent tự dùng khi việc bạn nhờ liên quan đến chữ giao diện tiếng Việt.

### 1. Khi đang code

Làm việc bình thường trong repo có tiếng Việt (`vi.json`, `vi.yml`, `*_vi.arb`, `values-vi/strings.xml`, `vi.lproj`, hoặc chữ tiếng Việt viết thẳng trong component). Ví dụ:

```
Thêm nút "Đặt lại" cho danh sách đơn cũ, thêm key order.reorder vào en.json và vi.json.
```

```
Khi cổng thanh toán quá thời gian chờ thì báo lỗi. Thêm order.paymentTimeout vào cả hai file locale.
```

Skill sẽ:

- **Lần đầu tiên:** tạo `docs/ux-voice.md` ghi cách gọi người dùng, giọng điệu, thuật ngữ, kiểu dấu thanh, rồi báo bạn một dòng. Không hỏi trước.
- **Viết tiếng Việt từ ý**, không dịch từng chữ của chuỗi tiếng Anh.
- **Theo mẫu cho từng loại thành phần:** lỗi luôn có bước tiếp theo, nút là động từ + đối tượng, hộp thoại có nút ghi rõ hành động.
- **Giữ nguyên biến** như `{{count}}`, `{name}`, `%s`, và cấu trúc số nhiều ICU.
- **Chỉ sửa đúng chuỗi được nhờ**, và liệt kê những chuỗi cũ còn yếu để bạn quyết định có sửa không.

### 2. Nhờ rà soát

Dán chữ, gửi ảnh chụp màn hình, đưa đường dẫn, hoặc chỉ vào file:

```
Rà lại chữ trên màn hình này giúp mình [đính kèm ảnh]
```

```
Review copy trang này: https://example.com/onboarding
```

```
Xem lại các chuỗi trong src/locales/vi.json
```

Kết quả trả về theo dạng `Trước → Sau — lý do` cho từng chuỗi. Skill cũng chỉ ra chỗ xưng hô lẫn lộn (*bạn* chỗ này, *quý khách* chỗ kia) và thống nhất lại.

### File giọng văn `docs/ux-voice.md`

Đây là nơi bạn điều khiển giọng của ứng dụng. Mặc định:

| Lựa chọn | Mặc định | Ngân hàng, bảo hiểm, y tế |
|---|---|---|
| Gọi người dùng | *bạn*, hoặc bỏ đại từ | *quý khách*, hoặc bỏ đại từ |
| Ứng dụng tự xưng | Không ("chúng tôi", "mình") | *chúng tôi* chỉ khi nói về chính sách, pháp lý |
| Giọng | Trung tính, thân thiện | Trang trọng |
| Trợ từ | *nhé* dùng thưa; không *nha*, *ạ* | Không *nhé*; *vui lòng* khi cần |
| Dấu thanh | *xóa, hòa* (hoặc theo repo) | như bên trái |
| Tiền | `100.000đ` | `100.000 VND` |

Muốn đổi, sửa thẳng file. Các chuỗi viết sau sẽ theo bản đã sửa. Nếu repo của bạn đã dùng sẵn *anh/chị* hay *xoá*, skill theo cách đó thay vì mặc định.

## Cập nhật và gỡ cài đặt

```bash
# Cập nhật
npx skills update                                  # nếu cài bằng Skills CLI
cd vn-ux-writing-skill && git pull                 # nếu dùng symlink

# Gỡ
rm ~/.claude/skills/ux-writing-vi                  # symlink
rm -r ~/.claude/skills/ux-writing-vi               # bản chép
```

## Bên trong có gì

```
ux-writing-vi/
├── SKILL.md                        # quy trình và quy tắc chính
├── references/
│   ├── xung-ho-va-giong-dieu.md    # xưng hô, giọng, trợ từ, chọn theo lĩnh vực
│   ├── mau-noi-dung.md             # mẫu cho từng thành phần giao diện
│   ├── loi-dich-may-moc.md         # câu nghe như dịch và cách sửa
│   ├── thuat-ngu.md                # thuật ngữ thường gặp
│   ├── dinh-dang.md                # ngày giờ, số, tiền, dấu câu, Unicode
│   └── tiep-can.md                 # trình đọc màn hình, alt text, chữ liên kết
├── templates/giong-van.md          # mẫu cho docs/ux-voice.md
└── examples/truoc-va-sau.md        # 24 ví dụ trước → sau
```

Các file tham khảo cũng đọc được như một cẩm nang viết chữ giao diện tiếng Việt, kể cả khi không dùng AI.

## Đóng góp

Rất mong nhận góp ý, nhất là những câu "đúng ngữ pháp nhưng nghe như dịch" mà skill chưa bắt được. Mở issue hoặc pull request.

Trước khi gửi pull request:

```bash
python3 scripts/check_skill.py ux-writing-vi       # cấu trúc, liên kết, Unicode NFC, độ dài SKILL.md
python3 -m unittest discover -s tests -t .         # test cho các script
python3 scripts/package_skill.py ux-writing-vi dist/ux-writing-vi.zip   # đóng gói
```

Bộ đánh giá hành vi nằm trong `evals/`: 20 tình huống, hai repo mẫu, và kết quả so sánh có/không có skill (`evals/results/`). Nếu bạn sửa quy tắc trong skill, chạy lại các tình huống liên quan và ghi kết quả.

## Nguồn và giấy phép

- Khung bốn tiêu chuẩn (có mục đích, ngắn gọn, tự nhiên, rõ ràng) và các mẫu nội dung phỏng theo [UX Writing Skill](https://github.com/content-designer/ux-writing-skill) của Christopher Greer (MIT).
- Quy tắc ngôn ngữ (viết hoa, dấu câu, định dạng số, tránh dịch từng chữ) được diễn đạt lại từ [Microsoft Vietnamese Localization Style Guide](https://learn.microsoft.com/globalization/reference/microsoft-style-guides).
- Mọi ví dụ tiếng Việt được viết mới.

Giấy phép MIT. Xem [ux-writing-vi/LICENSE](ux-writing-vi/LICENSE).

---

## English

`ux-writing-vi` is an agent skill for writing and reviewing Vietnamese UI copy. It's built for solo developers who write their own app text and have no UX writing background. It makes the tone and pronoun decisions for you, tells you in one line, and keeps them consistent across the app.

### Install

```bash
# Skills CLI
npx skills add duy211099/vn-ux-writing-skill@ux-writing-vi -g -y

# Or manually, for Claude Code
git clone https://github.com/duy211099/vn-ux-writing-skill.git
ln -s "$PWD/vn-ux-writing-skill/ux-writing-vi" ~/.claude/skills/ux-writing-vi
```

For other agents, copy `ux-writing-vi/` into that agent's skills folder (often `~/.agents/skills/`). To install for one project only, put it in `.claude/skills/` inside that repo.

### Use

- **While coding:** work as usual in a repo with Vietnamese UI (`vi.json`, `vi.yml`, `*_vi.arb`, `values-vi/strings.xml`, `vi.lproj`, or hardcoded Vietnamese strings). The skill:
  - creates `docs/ux-voice.md` on first use;
  - writes Vietnamese from the intent of English source strings rather than translating them word by word;
  - keeps placeholders intact;
  - changes only the strings in scope.
- **Review:** paste text, attach a screenshot, give a URL, or point at a file. You get `Trước → Sau — lý do` (before → after — reason) for each string.

Edit `docs/ux-voice.md` to change the voice. Defaults are *bạn* with a neutral-friendly tone, and *quý khách* with a formal tone for banking, insurance and health.

### Credits

Adapted from Christopher Greer's [UX Writing Skill](https://github.com/content-designer/ux-writing-skill) (MIT). Language rules are paraphrased from the Microsoft Vietnamese Localization Style Guide. All Vietnamese examples are original. Released under the MIT license.
