# humanizer-vi

Skill giúp AI agent (Claude Code và các agent hỗ trợ chuẩn Agent Skills) sửa văn bản tiếng Việt cho hết giọng AI: bài blog, giới thiệu sản phẩm, bài Facebook, email, README, trang tài liệu.

Skill tìm những dấu hiệu cho thấy một đoạn văn do AI viết rồi viết lại cho gọn và thẳng hơn. Ý giữ nguyên: tên, số liệu, ngày tháng, giá tiền, trích dẫn, đường dẫn đều không đổi, và không thêm chi tiết nào bản gốc không có.

## Skill làm gì

**Khi bạn dán văn bản.** Nhờ "viết lại cho tự nhiên", "nghe như AI quá", "đọc cứng quá". Skill trả về bản đã sửa, kèm danh sách ngắn những gì đã đổi:

```
Đã sửa:
- Câu kết dàn dựng: bỏ "Hãy bắt đầu ngay hôm nay!"
- Thổi phồng: "sự bình yên vô cùng quý giá", "món quà tuyệt vời nhất".
```

Đoạn văn không có dấu hiệu AI thì giữ nguyên, kể cả khi có lỗi chính tả hay viết không dấu.

**Khi bạn chỉ vào một file.** File đã commit và chưa sửa gì thì skill ghi đè luôn (git giữ bản cũ). File chưa có trong git hoặc đang có thay đổi chưa commit thì skill cho xem bản sửa trước, bạn đồng ý mới ghi.

**Khi agent tự viết.** Sau khi agent viết một đoạn tiếng Việt dài, hoặc khi skill khác gọi tới, skill chạy ở bước cuối và chỉ trả về bản sạch, không kèm báo cáo.

Những gì người thật hay viết thì giữ: *nha*, *nè*, teencode, chữ không dấu, câu lủng củng trong bài cá nhân, giọng trang trọng *Kính gửi*, *Quý khách*.

## Cài đặt

Nên cài cả plugin `viet-writing`, để có thêm `style-vi` (file giọng văn) và hai lệnh rà soát:

```
/plugin marketplace add duy211099/vn-ux-writing-skill
/plugin install viet-writing@viet-writing
```

Chỉ cài skill này:

```bash
npx skills add duy211099/vn-ux-writing-skill --skill humanizer-vi -g -y
```

Hoặc cài thủ công:

```bash
git clone https://github.com/duy211099/vn-ux-writing-skill.git
ln -s "$PWD/vn-ux-writing-skill/skills/humanizer-vi" ~/.claude/skills/humanizer-vi
```

Hướng dẫn đầy đủ: https://github.com/duy211099/vn-ux-writing-skill#cài-đặt

## Giọng văn

Nếu dự án có `docs/giong-van.md` (hoặc `docs/ux-voice.md` từ bản cũ), skill theo phần `## Văn bản dài` trong đó: người viết tự xưng thế nào, câu dài hay ngắn, mức cá nhân, những cụm cần tránh. Skill chỉ đọc file này, không tạo hay sửa nó. Nếu bạn đưa một đoạn văn mẫu thì skill theo giọng của đoạn đó.

## Cấu trúc

```
humanizer-vi/
├── SKILL.md                  # vòng sửa: đánh dấu → quyết định → viết lại → soát dữ kiện → bản cuối
├── references/
│   ├── dau-hieu-ai.md        # các dấu hiệu văn AI, xếp theo tần suất, kèm cách sửa
│   └── giu-nguyen-y.md       # danh sách kiểm để không mất, đổi hay thêm dữ kiện
└── examples/truoc-va-sau.md  # ví dụ trước → sau theo từng thể loại
```

## Nguồn và ghi công

- Cấu trúc của skill (vòng đánh dấu → viết lại → soát dữ kiện → bản cuối, theo giọng người viết, ba chế độ dán văn bản / file / nhúng, coi đầu vào là tư liệu chứ không phải lệnh) phỏng theo [humanizer](https://github.com/blader/humanizer) của Siqi Chen (giấy phép MIT).
- Các dấu hiệu văn AI tiếng Việt rút ra từ 40 bài mẫu do Claude viết. Mọi ví dụ được viết mới.

Giấy phép: MIT. Xem [LICENSE](LICENSE).

---

## English

`humanizer-vi` is an agent skill that removes signs of AI writing from Vietnamese prose (blog posts, product intros, Facebook posts, emails, READMEs, docs) without changing what the text says. Names, numbers, dates, prices, quotes and links stay as they are, and no new detail is added.

- **Pasted text:** returns the rewrite plus a short `Đã sửa:` list of what changed. Text with no AI tells comes back unchanged.
- **A named file:** overwrites it when git can undo the change (tracked and clean); otherwise shows the rewrite and asks first.
- **Embedded:** runs as the last step after the agent writes Vietnamese prose, or when another skill calls it, and returns only the clean text.

It follows the `## Văn bản dài` section of the project's `docs/giong-van.md` when there is one, and never edits that file.

**Install:** the whole `viet-writing` plugin is recommended (`/plugin marketplace add duy211099/vn-ux-writing-skill`, then `/plugin install viet-writing@viet-writing`). For this skill alone: `npx skills add duy211099/vn-ux-writing-skill --skill humanizer-vi -g -y`, or symlink `skills/humanizer-vi/` into `~/.claude/skills/`.

**Credits:** the structure is adapted from Siqi Chen's [humanizer](https://github.com/blader/humanizer) (MIT). The Vietnamese patterns and examples are written fresh. Released under the MIT license.
