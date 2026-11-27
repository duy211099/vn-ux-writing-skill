---
name: review
description: Use when the author runs /viet-writing:review to check the Vietnamese text in their current changes — staged, unstaged and untracked files compared with HEAD, or with a branch or commit given as the argument. Covers UI strings (locale files such as vi.json, hardcoded strings in components) and Vietnamese prose (Markdown, HTML, text). Author-run only.
argument-hint: "[branch or commit to compare against]"
disable-model-invocation: true
---

# Review the Vietnamese in the current changes

The author ran `/viet-writing:review` to check what they just changed. Find the Vietnamese text in the lines they added or changed, apply `ux-writing-vi`'s rules to UI strings and `humanizer-vi`'s loop to prose, and show the proposed fixes. **Change nothing until the author says yes.**

Argument: `$ARGUMENTS`. Empty → compare with `HEAD`. Otherwise it is a branch or commit, and you compare with the commit where the current branch split from it: `git merge-base <arg> HEAD`. Commits added to `<arg>` after that point are not this change.

## 1. Check that there is something to compare

Run these in order. Each stop is one line of output and nothing else: no review of the files anyway, no `git init`, no commit.

| Check | If it fails, reply with this line and stop |
|---|---|
| `git rev-parse --is-inside-work-tree` | `Thư mục này chưa phải repo git nên không có thay đổi để so. Chạy /viet-writing:analyze để rà toàn bộ chữ tiếng Việt trong thư mục.` |
| `git rev-parse --verify HEAD` (or the argument) | No commits: `Repo chưa có commit nào nên chưa có gì để so. Chạy /viet-writing:analyze để rà toàn bộ chữ tiếng Việt trong thư mục.` Bad argument: `Không tìm thấy nhánh hoặc commit "<arg>".` |
| Any change at all (step 2 finds no changed Vietnamese line) | `Không có chữ tiếng Việt nào trong phần vừa thay đổi.` |

## 2. Collect the changed lines

- **Tracked files:** `git diff <base> -U0` where `<base>` is `HEAD`, or with an argument `base=$(git merge-base <arg> HEAD)`, never the argument itself (its tip includes work that is not part of this change). This one command covers staged and unstaged changes together. Never use `git diff` alone (unstaged only) or `git diff --cached` alone (staged only): each misses half the change.
- **Untracked files:** `git ls-files --others --exclude-standard`. Every line in them is new.
- Drop lockfiles, `node_modules/`, `vendor/`, build output, binaries and minified files.
- Keep only added or changed lines that contain Vietnamese. Deleted lines are not reviewed.
- **The diff decides the scope.** A string or paragraph that the diff did not touch is out of scope, however bad it is. Don't fix it, list it, or mention it, not even in a closing "ngoài phạm vi" note.

## 3. Sort each changed piece

| Piece | Kind | Rules |
|---|---|---|
| A value in a locale file (`vi.json`, `vi.yml`, `vi.ts`, `*_vi.arb`, `values-vi/strings.xml`, `vi.lproj/*`, `vi.po`) | UI string | `ux-writing-vi`, Mode B |
| A Vietnamese string literal or JSX text in component code | UI string | `ux-writing-vi`, Mode B |
| A paragraph, list item or heading in `.md`, `.mdx`, `.html`, `.txt`, `.rst` (README, docs, blog) | Prose | `humanizer-vi` loop |
| Code comments, commit messages, test data | — | Skip |

For prose, the unit is the **whole paragraph** that contains a changed line: read the file around the diff to get it. Unchanged paragraphs next to it are context, not material.

## 4. Load the rules

Both skills are in this plugin. Use the Skill tool for `ux-writing-vi` and `humanizer-vi` if they are listed; otherwise read `../ux-writing-vi/SKILL.md` and `../humanizer-vi/SKILL.md` next to this skill's folder, and the reference files they point to when you need them.

- **UI strings:** follow `ux-writing-vi` Mode B: element patterns, the four standards, top traps, mechanics (placeholders byte for byte, tone-mark style, NFC). A string that is already good is not listed.
- **Prose:** run `humanizer-vi`'s loop on each changed paragraph: mark → decide → rewrite → check facts → final. A paragraph with no tells is not listed. Every name, number, date, price, code and link survives unchanged, and nothing is added.

## 5. Voice

Read `docs/giong-van.md`, or `docs/ux-voice.md` if only that exists. If neither exists, use the domain defaults from `ux-writing-vi` (its `references/xung-ho-va-giong-dieu.md`), guessing the domain from `package.json`, the README and existing strings, and following any pronoun or tone-mark style the existing strings already use. **Never create, edit or offer to create a voice file**; that is the job of `style-vi` or `ux-writing-vi` when they write.

## 6. Output

Your reply is exactly these parts, in this order, in Vietnamese:

1. **One voice line** (this command's rule; it overrides `ux-writing-vi` Mode B's "never mention the voice file"). `Giọng: theo docs/giong-van.md (gọi "bạn", dấu kiểu xóa).` or, with no voice file, `Giọng: chưa có file giọng văn, dùng mặc định cho ứng dụng gọi xe (gọi "bạn", dấu kiểu xóa).`
2. **UI strings, grouped by file.** The file path on its own line, then one line per changed string, key first:

   ```
   src/locales/vi.json
   trip.cancelled: "Chuyến đi của bạn đã được hủy thành công" → "Đã hủy chuyến" — Bỏ bị động và "của bạn"; thông báo thành công chỉ cần "Đã + động từ".
   ```

3. **Prose, grouped by file.** The file path on its own line, then for each changed paragraph that has tells: the rewritten paragraph, a blank line, `Đã sửa:` and one bullet per tell fixed (1–6, never padded), in `humanizer-vi`'s pasted-text shape:

   ```
   Xe Nhanh có mặt ở Đà Nẵng từ 15/3/2027, đón khách từ 5 giờ sáng.

   Đã sửa:
   - Mở bài dàn dựng: bỏ "Trong kỷ nguyên số"
   - Thổi phồng: bỏ "trải nghiệm di chuyển tuyệt vời"
   ```

4. **Size limit.** If more than about 30 changed strings or paragraphs need fixing, keep the reply readable: strings with the same fix take one line (`trip.rated1, trip.rated2… (18 khóa): "…" → "…" — lý do`), rewrite in detail only the worst ones, and name the rest, with their count, under `Chưa rà chi tiết:`. Never cut silently.
5. **The offer, as the last line:** `Áp dụng các thay đổi này vào file không?`

Nothing else: no intro, no summary of the diff, no diff blocks, no notes on unchanged lines, no "kiểm tra trước khi đăng" list, no questions about voice. If nothing in the change needs fixing, reply with the voice line and `Phần chữ tiếng Việt vừa đổi đã ổn, không cần sửa.`

## 7. Writing only after a yes

Until the author answers yes (*ok*, *áp dụng*, *được*, *yes*, *sửa đi*), you are read-only: no Edit or Write, no `git add`, `stash`, `checkout`, `restore` or commit.

When they say yes:

- Write exactly what you showed: each `Sau` string replaces its old value, each rewritten paragraph replaces the whole old paragraph. Nothing else in the file changes: no other key, paragraph, formatting or trailing newline. Items you only named under `Chưa rà chi tiết:` are written only if the author asks for them; then follow the same rules and list each change as `key: "trước" → "sau"`.
- If they say yes to part of it (*chỉ sửa vi.json*), write only that part.
- Leave git alone: don't stage, unstage or commit. A file that was staged stays staged with your change unstaged on top.
- Write NFC. Check that a JSON or YAML file still parses.
- Reply in one line: `Đã áp dụng 1 chuỗi trong src/locales/vi.json và 2 đoạn trong docs/blog/ten-bai.md.`

## Red flags

| You catch yourself… | Instead |
|---|---|
| Reviewing a key or paragraph the diff didn't touch, or adding "ngoài phạm vi thay đổi…" | The diff is the scope. Leave it out entirely. |
| Using `git diff --cached` or plain `git diff` only | `git diff HEAD` (or the merge-base) plus untracked files. |
| `git diff main` when the argument is `main` | `git diff $(git merge-base main HEAD)`: the tip of `main` has commits this branch never touched. |
| Listing problems in a paragraph instead of rewriting it | Rewrite it, then `Đã sửa:`. |
| Writing *2 tuần*, *miễn phí*, *ứng dụng số 1* that the text didn't say | Added facts are errors. Use only what the text says. |
| "Repo chưa có commit, mình rà tất cả file luôn" | One line, offer `/viet-writing:analyze`, stop. |
| Fixing the file "luôn cho nhanh" before the author answers | Show, offer, wait for yes. |
| Asking which pronoun or tone the author prefers | Use the voice file or the defaults, say so in one line. |
| Creating `docs/giong-van.md` because it's missing | Never. Say you used the defaults. |
| Forty `Trước → Sau` lines for a big change | Group same-fix keys in one line; the rest under `Chưa rà chi tiết:`. |
