# ux-writing-vi

Skill giúp AI agent (Claude Code và các agent hỗ trợ chuẩn Agent Skills) viết và sửa chữ trên giao diện tiếng Việt: nút, nhãn, thông báo lỗi, trạng thái trống, hộp thoại, thông báo đẩy, màn giới thiệu.

Dành cho lập trình viên làm sản phẩm một mình, không có người viết nội dung chuyên nghiệp. Bạn không cần biết lý thuyết UX writing. Skill tự chọn cách xưng hô và giọng văn hợp với ứng dụng, báo lại một dòng, và giữ thống nhất trên mọi màn hình.

## Skill làm gì

**Khi bạn đang code (tự động).** Mỗi khi agent thêm hoặc sửa chuỗi hiển thị trong repo có tiếng Việt (`vi.json`, `*_vi.arb`, `vi.lproj`, chữ viết thẳng trong component), skill:

- tạo file `docs/giong-van.md` lần đầu, ghi cách gọi người dùng (*bạn*, *quý khách*…), giọng điệu và thuật ngữ, rồi dùng lại cho mọi chuỗi sau;
- viết tiếng Việt từ ý của chuỗi tiếng Anh, không dịch từng chữ;
- theo mẫu cho từng loại thành phần (lỗi luôn có bước tiếp theo, nút ghi rõ hành động…);
- giữ nguyên biến như `{{count}}`, `%s`;
- chỉ sửa đúng chuỗi cần sửa, và nhắc bạn nếu thấy chuỗi cũ nào chưa ổn.

**Khi bạn nhờ rà soát.** Dán chữ, gửi ảnh chụp màn hình, đưa đường dẫn trang web, hoặc chỉ vào một file. Skill trả về từng chuỗi theo dạng:

```
Trước → Sau — lý do
"Bạn có chắc chắn muốn đăng xuất không?" → "Đăng xuất khỏi thiết bị này?" — Câu hỏi ngắn; nút ghi "Đăng xuất" / "Hủy".
```

## Cài đặt

**Claude Code**

```bash
npx skills add duy211099/vn-ux-writing-skill@ux-writing-vi -g -y
```

Hoặc cài thủ công:

```bash
git clone https://github.com/duy211099/vn-ux-writing-skill.git
ln -s "$PWD/vn-ux-writing-skill/ux-writing-vi" ~/.claude/skills/ux-writing-vi
```

Hướng dẫn đầy đủ: https://github.com/duy211099/vn-ux-writing-skill#cài-đặt

**Agent khác** (Codex, Cursor…): giải nén vào thư mục skills của agent đó, thường là `~/.agents/skills/`.

Kiểm tra: mở một repo có `vi.json` và nhờ agent thêm một nút mới.

## File giọng văn

Lần đầu chạy trong một repo, skill tạo `docs/giong-van.md` (dùng chung với các skill khác trong plugin `viet-writing`; nếu repo đã có `docs/ux-voice.md` từ bản cũ, skill dùng luôn file đó, không đổi tên). Mặc định:

- gọi người dùng là *bạn* (ngân hàng, bảo hiểm: *quý khách*), hoặc bỏ đại từ khi câu vẫn rõ;
- ứng dụng không tự xưng "chúng tôi", "mình";
- giọng trung tính, thân thiện; *nhé* dùng thưa; không *nha*, *ạ*;
- dấu thanh kiểu *xóa, hòa* (hoặc theo kiểu repo đang dùng).

Muốn đổi, sửa file đó. Các chuỗi viết sau sẽ theo bản đã sửa.

## Cấu trúc

```
ux-writing-vi/
├── SKILL.md                        # quy trình và quy tắc chính
├── references/
│   ├── xung-ho-va-giong-dieu.md    # xưng hô, giọng, trợ từ
│   ├── mau-noi-dung.md             # mẫu cho từng thành phần
│   ├── loi-dich-may-moc.md         # các câu nghe như dịch và cách sửa
│   ├── thuat-ngu.md                # thuật ngữ thường gặp
│   ├── dinh-dang.md                # ngày giờ, số, tiền, dấu câu, Unicode
│   └── tiep-can.md                 # trình đọc màn hình, chữ liên kết, alt text
├── templates/giong-van.md          # mẫu file giọng văn
└── examples/truoc-va-sau.md        # ví dụ trước → sau
```

## Nguồn và ghi công

- Khung bốn tiêu chuẩn (có mục đích, ngắn gọn, tự nhiên, rõ ràng) và các mẫu nội dung phỏng theo [UX Writing Skill](https://github.com/content-designer/ux-writing-skill) của Christopher Greer (giấy phép MIT).
- Quy tắc ngôn ngữ (viết hoa, dấu câu, định dạng số, tránh dịch từng chữ) được diễn đạt lại từ [Microsoft Vietnamese Localization Style Guide](https://learn.microsoft.com/globalization/reference/microsoft-style-guides). Không sao chép nguyên văn.
- Mọi ví dụ tiếng Việt được viết mới, không lấy từ các nguồn trên.

Giấy phép: MIT. Xem [LICENSE](LICENSE).

Góp ý và sửa lỗi: mở issue hoặc pull request, nhất là khi bạn thấy một câu "đúng nhưng nghe như dịch".

---

## English

`ux-writing-vi` is an agent skill for writing and reviewing Vietnamese UI copy. It's built for solo developers who write their own app text. It works in two modes:

- **While coding:** when the agent writes strings in a repo with a Vietnamese locale, the skill keeps one voice across the app through `docs/giong-van.md`. It writes Vietnamese from the intent of English source strings rather than translating them word for word, and it applies a pattern for each element.
- **On request:** give it text, a screenshot or a URL, and it returns `Trước → Sau — lý do` rewrites.

**Install for Claude Code:** symlink or copy `ux-writing-vi/` into `~/.claude/skills/`.

**Credits:** adapted from Christopher Greer's [UX Writing Skill](https://github.com/content-designer/ux-writing-skill) (MIT). Language rules are paraphrased from the Microsoft Vietnamese Localization Style Guide. All Vietnamese examples are original. Released under the MIT license.
