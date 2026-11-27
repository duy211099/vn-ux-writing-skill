---
name: style-vi
description: Use when the user asks about, sets up or changes the voice of a Vietnamese project — giọng văn, xưng hô, cách gọi người dùng, cách tự xưng, "đổi sang quý khách", "giọng văn của app là gì", setting a voice before writing a Vietnamese blog, docs or UI text — or when another skill needs the project voice file (docs/giong-van.md or docs/ux-voice.md) and none exists.
---

# Vietnamese project voice

One file holds a project's Vietnamese voice: `docs/giong-van.md`. Every skill in the `viet-writing` plugin reads it, for UI strings and for long-form prose. This skill creates it, answers questions about it, and changes it.

The user is usually a solo developer with no writing background. **Decide for them**, say what you decided in one line, and let them edit the file. Never ask them to pick a pronoun or tone, and never end with a list of questions.

## The voice file

- **Lookup order:** `docs/giong-van.md`, then `docs/ux-voice.md` (older name from `ux-writing-vi`). If only `docs/ux-voice.md` exists, it *is* the voice file: read it and write changes into it. Never move, rename or copy it unasked, and never create `docs/giong-van.md` next to it.
- **One file only.** Long-form voice goes in its `## Văn bản dài` section, not in a new file (`docs/blog-voice.md`, a style guide, a `CLAUDE.md` pointer, a README section). If an older file lacks that section, append it from the template.
- **Format:** [templates/giong-van.md](templates/giong-van.md). Keep its headings and `<!-- -->` comments so the user can see the options.
- **Placeholders:** a field still in the form `[ví dụ: …]` is unset. If every field under `## Văn bản dài` is unset, the project has no prose voice yet.

## Job 1 — create the file

Run this when no voice file exists and the user asks to set up a voice, asks about the voice, or another skill needs the file.

1. Copy [templates/giong-van.md](templates/giong-van.md) to `docs/giong-van.md`.
2. Guess the domain from the project name, `package.json` (`name`, `description`), README and existing screens. Take the whole row for that domain from [references/mac-dinh-theo-linh-vuc.md](references/mac-dinh-theo-linh-vuc.md): UI pronoun, register, particles, and the prose fields.
3. Let the project override the defaults: if existing Vietnamese strings consistently use one pronoun (*quý khách*, *anh/chị*, *bạn*) or one tone-mark style (*xóa* / *xoá*), record that. If existing Vietnamese prose (README, blog, docs) has the writer referring to themselves one way, record that.
4. Fill every field: `Lĩnh vực`, the UI sections, and under `## Văn bản dài` the fields `Người viết tự xưng`, `Độ dài câu`, `Mức cá nhân`, `Tránh dùng` (the seed list). Leave `Đoạn văn mẫu` as its placeholder unless the user gave a sample. Add the domain's own words to `Thuật ngữ ưu tiên` (*chuyến*, *tài xế* in a ride-hailing app).
5. Change no other file.
6. Reply with one line in this shape and nothing else about the voice: no list of assumptions, no tips on fields to fill, no alternatives to consider. Then carry on with whatever the user or the calling skill asked for.

   ```
   Đã tạo docs/giong-van.md: gọi người dùng là "bạn", bài viết dài xưng "Xe Nhanh", câu xen kẽ, giọng trò chuyện (ứng dụng gọi xe). Sửa file này nếu muốn đổi.
   ```

## Job 2 — answer "what's our voice?"

Read the voice file (create it with Job 1 first if there is none) and reply in this shape, at most five lines. Change no files.

```
Theo docs/giong-van.md (gọi xe):
- Giao diện: gọi "bạn" hoặc bỏ đại từ, ứng dụng không tự xưng, trung tính thân thiện, *nhé* thưa thớt, dấu kiểu *xóa*.
- Văn bản dài: xưng "Xe Nhanh", câu xen kẽ, giọng trò chuyện.
Sửa file đó để đổi.
```

If the prose section is all placeholders, write `- Văn bản dài: chưa chọn.` If the user asked about one thing only ("app gọi người dùng là gì?"), answer that in one line.

## Job 3 — change the voice

1. **Edit only the voice file.** Change the field the user named. Also change fields that would now contradict it, using the domain table: *quý khách* goes with a formal register, no *nhé*, *vui lòng* allowed; *mình* in prose goes with a personal tone. Leave the rest as it is.
2. **Find what now disagrees.** Search locale files (`vi.json`, `vi.yml`, `vi.ts`, `*_vi.arb`, `values-vi/strings.xml`, `vi.lproj`, `vi.po`), components with hardcoded Vietnamese, and Vietnamese prose (`.md`, `.mdx`) for the old value in every form. For a pronoun, that is case-insensitive whole-word matching: *Bạn có chắc…*, *của bạn*, *bạn ơi*, not only one phrase. For tone marks, every *oa/oe/uy* word (*xóa, hòa, hủy, khỏe*).
3. **List them, don't fix them.** Even when the fix is obvious and the list is short, the strings stay as they are until the user says yes.
4. Reply in this shape:

   ```
   Đã đổi docs/giong-van.md: gọi người dùng là "quý khách", giọng trang trọng, bỏ *nhé*.
   Các chuỗi còn dùng "bạn" (chưa sửa):
   - src/i18n/vi.json `trip.cancel`: "Bạn có chắc muốn hủy chuyến?"
   - src/i18n/vi.json `wallet.empty`: "Ví của bạn chưa có tiền"
   - src/screens/Home.tsx: "Chào bạn, hôm nay đi đâu?"
   Sửa các chuỗi này theo giọng mới không?
   ```

   If nothing disagrees, say so in the same line as the change.

## When another skill calls this one

Another skill (for example `ux-writing-vi` before writing strings) needs the voice file and none exists: run Job 1, give its one-line reply, and hand back. Don't answer questions or summarise.

## Common mistakes

| Mistake | Do instead |
|---|---|
| Writing a brand persona essay, tone tables, sample posts | Fill the template's fields; that's the whole file |
| Creating `docs/blog-voice.md`, a `CLAUDE.md` or any second file | Put prose settings in `## Văn bản dài` of the one voice file |
| Ending with "Xưng hô mình – bạn có đúng không?" or "Cần bạn xác nhận" | Decide from the domain table and the existing text; the file is the place to override |
| Creating `docs/giong-van.md` when `docs/ux-voice.md` exists | Edit `docs/ux-voice.md` where it is |
| Rewriting `vi.json` after a pronoun change | List the disagreeing strings and offer |
| Searching only for "của bạn" | Whole-word, any case: *Bạn* at the start of a sentence counts |
| Summarising the voice field by field in 20 lines | Five lines, in the Job 2 shape |
| Following the one-line announcement with "Mình đoán…", "Nếu muốn… thì đổi…", tips on empty fields | The line already says how to change it; stop there |
