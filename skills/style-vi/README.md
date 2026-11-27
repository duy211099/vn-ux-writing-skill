# style-vi

Skill giúp AI agent (Claude Code và các agent hỗ trợ chuẩn Agent Skills) giữ một giọng văn tiếng Việt chung cho cả dự án, từ chuỗi giao diện đến bài blog và tài liệu.

Giọng văn nằm trong một file duy nhất: `docs/giong-van.md`. Mọi skill trong plugin `viet-writing` đều đọc file này. `style-vi` tạo file, trả lời khi bạn hỏi về nó, và sửa nó khi bạn muốn đổi giọng.

## Skill làm gì

**Tạo file giọng văn.** Lần đầu bạn hoặc một skill khác cần đến, skill đoán lĩnh vực của dự án từ tên, `package.json`, README và các màn hình có sẵn, rồi điền mặc định hợp với lĩnh vực đó. Nếu repo đã quen gọi người dùng là *quý khách* hay viết *xoá*, skill ghi theo cách đó. Skill tự chọn rồi báo lại một dòng:

```
Đã tạo docs/giong-van.md: gọi người dùng là "bạn", bài viết dài xưng "Xe Nhanh", câu xen kẽ, giọng trò chuyện (ứng dụng gọi xe). Sửa file này nếu muốn đổi.
```

**Trả lời "giọng văn của app là gì?".** Tóm tắt trong vài dòng: phần giao diện và phần văn bản dài.

**Đổi giọng.** Ví dụ "đổi sang gọi quý khách". Skill sửa file giọng văn, kéo theo những lựa chọn đi cùng (giọng trang trọng, bỏ *nhé*), rồi liệt kê các chuỗi còn theo giọng cũ. Các chuỗi đó chưa bị sửa cho đến khi bạn đồng ý.

## File giọng văn

File có hai phần:

- **Giao diện:** cách gọi người dùng, ứng dụng có tự xưng không, giọng điệu, trợ từ, kiểu dấu thanh (*xóa* hay *xoá*), thuật ngữ.
- **Văn bản dài** (`## Văn bản dài`): người viết tự xưng thế nào, câu dài hay ngắn, mức cá nhân, những cụm cần tránh, đoạn văn mẫu.

Dự án đã có `docs/ux-voice.md` từ bản cũ của `ux-writing-vi` thì skill dùng luôn file đó, không đổi tên và không tạo thêm file mới bên cạnh.

## Cài đặt

Nên cài cả plugin `viet-writing`, vì skill này chủ yếu phục vụ các skill khác trong plugin:

```
/plugin marketplace add duy211099/vn-ux-writing-skill
/plugin install viet-writing@viet-writing
```

Chỉ cài skill này:

```bash
npx skills add duy211099/vn-ux-writing-skill --skill style-vi -g -y
```

Hoặc cài thủ công:

```bash
git clone https://github.com/duy211099/vn-ux-writing-skill.git
ln -s "$PWD/vn-ux-writing-skill/skills/style-vi" ~/.claude/skills/style-vi
```

Hướng dẫn đầy đủ: https://github.com/duy211099/vn-ux-writing-skill#cài-đặt

## Cấu trúc

```
style-vi/
├── SKILL.md                               # tạo, trả lời, đổi giọng văn
├── references/mac-dinh-theo-linh-vuc.md   # mặc định cho từng lĩnh vực
└── templates/giong-van.md                 # mẫu file giọng văn
```

Giấy phép: MIT. Xem [LICENSE](LICENSE).

---

## English

`style-vi` is an agent skill that keeps one Vietnamese voice per project in one file, `docs/giong-van.md`, which every skill in the `viet-writing` plugin reads. It covers UI copy (how to address the user, register, particles, tone-mark style, terms) and long-form prose (the writer's self-reference, sentence length, how personal to be, phrases to avoid).

- **Create:** guesses the domain from the project and fills in that domain's defaults, following any pronoun or tone-mark style the repo already uses. It reports what it chose in one line instead of asking.
- **Answer:** summarises the current voice in a few lines.
- **Change:** edits the voice file, then lists the strings that no longer match. It changes them only after you say yes.

Projects that already have `docs/ux-voice.md` from an older `ux-writing-vi` keep using it.

**Install:** the whole `viet-writing` plugin is recommended (`/plugin marketplace add duy211099/vn-ux-writing-skill`, then `/plugin install viet-writing@viet-writing`). For this skill alone: `npx skills add duy211099/vn-ux-writing-skill --skill style-vi -g -y`, or symlink `skills/style-vi/` into `~/.claude/skills/`.

Released under the MIT license.
