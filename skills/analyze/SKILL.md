---
name: analyze
description: Use when the author runs /viet-writing:analyze to check all the Vietnamese text in a repo, or in a path given as the argument — locale files (vi.json, vi.yml, vi.ts, *_vi.arb, values-vi/strings.xml, vi.lproj, vi.po), hardcoded Vietnamese in components, and Vietnamese Markdown, HTML or text prose — for consistency (pronouns, tone-mark style, terms) and quality. Author-run only.
argument-hint: "[path]"
disable-model-invocation: true
---

# Analyze all the Vietnamese in a repo

The author ran `/viet-writing:analyze` to see the state of every Vietnamese string and paragraph at once. **Consistency is the point:** pronouns, tone-mark style and terms across files, which a per-change review cannot see. Show a summary first, then fixes for the worst files, then offer to fix. **Change nothing until the author says yes.**

Argument: `$ARGUMENTS`. Empty → the whole repo (the git root, or the current folder if it is not a repo). Otherwise only that path.

## 1. List the files

- In a git repo: `git ls-files --cached --others --exclude-standard -- <path>` (this respects `.gitignore`). Outside one: walk the folder.
- **Then skip by name, even if the file is tracked:** `node_modules/`, `vendor/`, `.git/`, build output (`dist/`, `build/`, `out/`, `.next/`, `coverage/`), lockfiles (`package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`, `Podfile.lock`, `*.lock`), minified files, binaries, and test fixtures and data (`tests/fixtures/`, `__fixtures__/`, `fixtures/`, `testdata/`, `__snapshots__/`, `*.test.*`, `*.spec.*`). A skipped folder is skipped even when the argument is its parent; it is checked only when the argument names it or a path inside it.
- Keep files that contain Vietnamese (letters such as *ă â đ ê ô ơ ư* or Vietnamese tone marks), found with `grep -l`:
  - **Locale files:** `vi.json`, `vi.yml`, `vi.ts`, `*_vi.arb`, `values-vi/strings.xml`, `vi.lproj/*`, `vi.po`, and the same names under a `vi/` folder.
  - **Components:** `.js`, `.jsx`, `.ts`, `.tsx`, `.vue`, `.svelte`, `.dart`, `.swift`, `.kt`, `.java`, templates: string literals and JSX text in Vietnamese. Not comments.
  - **Prose:** `.md`, `.mdx`, `.html`, `.txt`, `.rst` (README, docs, blog).

## 2. Read and tally

Read every kept file. For a big one, count with a short script (load the JSON, count keys, grep the patterns) instead of reading it line by line. Per file, count the strings or paragraphs and the ones with a problem.

Look for problems in this order:

1. **Across files** (the reason this command exists): user pronoun (*bạn*, *quý khách*, *anh/chị*, *mình*, none), tone-mark style (*xóa / xoá*, *hủy / huỷ*, *hòa / hoà*, *thủy / thuỷ*), the same thing named two ways (*món / sản phẩm / mục*), button verbs. Compare against the voice file, or the majority if there is none.
2. **UI strings:** `ux-writing-vi` Mode B rules: generic errors, "Bạn có chắc chắn… không?", "của bạn", "đã được… thành công", stacked *vui lòng*, English left in, placeholders.
3. **Prose:** `humanizer-vi`'s tells.

Both skills are in this plugin. Use the Skill tool for `ux-writing-vi` and `humanizer-vi` if they are listed; otherwise read `../ux-writing-vi/SKILL.md` and `../humanizer-vi/SKILL.md` next to this skill's folder, and their reference files when needed.

## 3. Voice

Read `docs/giong-van.md`, or `docs/ux-voice.md` if only that exists. If neither exists, use the domain defaults from `ux-writing-vi` (its `references/xung-ho-va-giong-dieu.md`), guessing the domain from `package.json`, the README and the strings; where the strings mostly agree on a pronoun or tone-mark style, the majority wins. **Never create, edit or offer to create a voice file.** Pick the target for each inconsistency yourself and say it; never ask the author to choose.

## 4. Size limits

Keep the reply readable, however big the repo:

- Rewrite in detail at most **3 files**, at most **15 `Trước → Sau` lines** and **2 prose paragraphs** in total. Pick the worst files, and within a file the worst strings; one line per problem kind is better than ten of the same kind.
- Many keys with the same fix take one line: `trip.rated1, trip.rated2… (18 khóa): "…" → "…" — lý do`.
- Everything else is counted in the summary and named under `Chưa rà chi tiết:`. Never cut silently. A script that greps for known problems finds those problems only: strings you checked that way, and did not read, go under `Chưa rà chi tiết:` as `đã quét bằng mẫu lỗi, chưa đọc từng chuỗi` with their count, never as "không có lỗi".
- A file too large to read at all (over about 5,000 lines, or generated or minified) is named under `Bỏ qua vì quá lớn:`.

## 5. Output

Your reply is exactly these parts, in this order, in Vietnamese:

1. **One voice line.** `Giọng: theo docs/giong-van.md (gọi "bạn", dấu kiểu xóa).` or `Giọng: chưa có file giọng văn, dùng mặc định cho ứng dụng gọi xe (gọi "bạn", dấu kiểu xóa theo đa số chuỗi).`
2. **`Tổng quan`**: one line per file, worst first: `src/i18n/vi.json — 120 chuỗi, 14 cần sửa`, `docs/gioi-thieu.md — 9 đoạn, 6 có dấu hiệu văn AI`. Then `Lỗi lặp lại:` with 3–5 bullets, each a problem, how often, and where: `- Lẫn xưng hô: "bạn" ở src/i18n/vi.json, "quý khách" ở src/driver/vi.json (6 chuỗi)`. Then `Nặng nhất:` the 1–3 worst files.
3. **Details for the worst files.** The file path on its own line, then:
   - UI strings: `key: "trước" → "sau" — lý do`, one per line, the reason in Vietnamese.
   - Prose: the rewritten paragraph, a blank line, `Đã sửa:` and 1–6 bullets, in `humanizer-vi`'s pasted-text shape.
4. **`Chưa rà chi tiết:`** the files, or the keys, that were counted but not rewritten. **`Bỏ qua:`** one line naming the skipped folders and files (`node_modules/, tests/fixtures/, package-lock.json`).
5. **The offer, as the last line,** naming one real file and one real problem from this repo: `Mình sửa tiếp src/driver/vi.json, hay sửa lẫn xưng hô trên mọi file (đổi về "bạn")?`

Nothing else: no intro, no tables of every string, no code-bug notes, no advice on generator scripts or build setup, no questions about voice.

## 6. Writing only after a yes

Until the author answers yes to the offer (*ok*, *sửa đi*, *sửa file đó*, *sửa lỗi xưng hô*), you are read-only: no Edit or Write, no `git` command that changes anything.

When they say yes:

- Do exactly the scope they chose: one file (every problem in it, as shown or in the same style), or one problem across every file that has it, and nothing else.
- Strings you already showed are written exactly as shown. For the rest, follow the same rules and list each change in the reply as `key: "trước" → "sau"`.
- Write NFC; check that JSON and YAML still parse. Don't stage or commit.
- End with one line saying what was written.

## Red flags

| You catch yourself… | Instead |
|---|---|
| Reading `tests/fixtures/` or `node_modules/` "for completeness" | Skipped by name. One `Bỏ qua:` line. |
| Listing every problem string in a 1,000-key file | Worst few in detail, the rest counted and named under `Chưa rà chi tiết:`. |
| "Các chuỗi còn lại không có lỗi" after a grep or a script | Say how many were only scanned by pattern, under `Chưa rà chi tiết:`. |
| "Bạn muốn dùng bạn hay quý khách?" | Decide by the voice file or the majority; say it in the summary. |
| Bullet critiques of a paragraph | Rewrite it, then `Đã sửa:`. |
| Creating `docs/giong-van.md` | Never. Say you used the defaults. |
| Fixing files before the author answers | Show, offer, wait for yes. |
