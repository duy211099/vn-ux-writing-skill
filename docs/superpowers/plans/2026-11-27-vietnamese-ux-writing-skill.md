# Vietnamese UX Writing Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. Anyone writing skill content also follows superpowers:writing-skills (RED → GREEN → REFACTOR with subagent scenarios).

**Goal:** Build `ux-writing-vi`, an agent skill that writes and reviews native-sounding Vietnamese UI copy for solo devs, mainly while Claude codes in their repo.

**Architecture:** A skill folder (`ux-writing-vi/`) holding a short `SKILL.md` plus reference, template and example Markdown files loaded on demand. Two kinds of test: a stdlib Python checker that enforces the mechanical rules (structure, links, NFC, length), and a behavioural eval of written cases run through subagents with and without the skill (baseline first, as in writing-skills TDD).

**Tech Stack:** Markdown; Python 3 stdlib (`unittest`, `unicodedata`, `re`, `pathlib`, `zipfile`) for the checker and packager; Claude Code subagents for evals.

**Spec:** `docs/superpowers/specs/2026-11-27-vietnamese-ux-writing-skill-design.md`

## Global Constraints

- Sources: only free/open documents. Framework from the original UX Writing Skill (MIT, Christopher Greer, https://github.com/content-designer/ux-writing-skill). Language rules from the Microsoft Vietnamese Localization Style Guide (https://download.microsoft.com/download/b/f/e/bfecb1b4-21ab-48fd-a48c-c2471b026f8f/vie-vnm-StyleGuide.pdf), **paraphrased, never copied**. Nothing from Podmajersky or Khúc Cẩm Huyên.
- Every Vietnamese example is written fresh, never translated from the original's English examples.
- All Markdown is Unicode NFC.
- `SKILL.md` under ~200 lines (checker enforces ≤ 200).
- Skill `name: ux-writing-vi`. File names are Vietnamese without diacritics, exactly as in the spec's structure.
- Defaults: user addressed as *bạn*; the app avoids referring to itself (*chúng tôi* only for formal/finance); register neutral-friendly; *nhé* sparingly; no *nha*/*ạ* in UI; *vui lòng* only formal/apologetic; formal defaults (possibly *quý khách*) for banking/government/health.
- Tone marks: follow the repo's existing style; otherwise use the newer style (*xóa*, *hòa*).
- Voice file path in user repos: `docs/ux-voice.md`.
- Mode A triggers on repos with a Vietnamese locale (`vi.json`, `app_vi.arb`, `vi.lproj`, …) or Vietnamese UI text; English-source keys get Vietnamese written fresh from the intent, not literally translated.
- Mode A only changes strings in scope; it mentions other weak strings and offers a review.
- Explanations in Vietnamese, one line per change. README in Vietnamese first, with a short English section.
- Drop English benchmarks (reading grade, "use you", English character counts).
- License MIT, crediting Christopher Greer's original.

## Review Focus

1. **Hardcoded Vietnamese in JSX, no locale files.** The skill should still trigger and write consistent copy. → eval case `A-04` (Task 2).
2. **Repo already uses *anh/chị* or *quý khách* consistently.** The skill adopts it and doesn't impose *bạn*. → eval case `A-05`.
3. **Interpolation placeholders and plural keys** (`{{count}}`, `{name}`, `%s`, `_one`/`_other`). Placeholders are kept byte-for-byte, and Vietnamese doesn't need distinct plural forms. → eval case `A-06`.
4. **NFD input** (decomposed diacritics, common from macOS copy-paste). The output is NFC. → eval case `B-07` and the checker's NFC test (Task 1).
5. **Tight space** (a button on a narrow screenshot, or the English source is 2 words). The Vietnamese stays short, a verb plus an object. → eval case `B-08`.

---

## File map

```
scripts/check_skill.py          # mechanical checker (Task 1)
scripts/package_skill.py        # zip for sharing (Task 8)
tests/test_check_skill.py       # unittest for checker (Task 1)
tests/test_package_skill.py     # unittest for packager (Task 8)
evals/cases.md                  # behavioural cases (Task 2)
evals/fixture-repo/             # tiny React + i18n app (Task 2)
evals/results/baseline.md       # RED run (Task 2)
evals/results/with-skill.md     # GREEN run (Task 9)
ux-writing-vi/SKILL.md          # Task 7
ux-writing-vi/references/*.md   # Tasks 3–6
ux-writing-vi/templates/giong-van.md   # Task 7
ux-writing-vi/examples/truoc-va-sau.md # Task 5
ux-writing-vi/README.md, LICENSE       # Task 8
```

---

### Task 1: Mechanical checker

**Files:**
- Create: `scripts/check_skill.py`
- Test: `tests/test_check_skill.py`

**Interfaces:**
- Produces: `check_skill(skill_dir: pathlib.Path) -> list[str]` (returns error messages, empty means it passed); `main(argv: list[str]) -> int` (CLI `python3 scripts/check_skill.py ux-writing-vi`, prints errors, exits 1 on any error). Every later task runs this CLI as its verification.

Rules it enforces (each one is a test):
- `SKILL.md` exists and has YAML front matter with `name` matching `^[a-z0-9-]+$` and a non-empty `description` of ≤ 1024 chars.
- `SKILL.md` has ≤ 200 lines.
- Every `.md` under `references/`, `templates/` and `examples/` is referenced by its relative path somewhere in `SKILL.md`.
- Every relative Markdown link `](path)` in any `.md` resolves to an existing file.
- Every `.md` is NFC (`unicodedata.normalize("NFC", text) == text`). Errors name the file.
- No `.md` contains `TBD` or `TODO`.

- [ ] **Step 1: Write failing tests** in `tests/test_check_skill.py`, building a temp skill dir per test with `tempfile.TemporaryDirectory`:
  - `test_valid_skill_passes`: a minimal valid dir → `check_skill(d) == []`
  - `test_missing_frontmatter_name`: → one error containing `"name"`
  - `test_skill_md_too_long`: 201 lines → error containing `"200"`
  - `test_unreferenced_reference_file`: `references/x.md` not mentioned → error containing `"references/x.md"`
  - `test_broken_relative_link`: `[a](references/nope.md)` → error containing `"nope.md"`
  - `test_nfd_text_rejected`: write `unicodedata.normalize("NFD", "Xóa tài khoản")` → error containing `"NFC"` and the file name
  - `test_tbd_rejected`: → error containing `"TBD"`
  - `test_main_exit_codes`: `main([valid]) == 0`, `main([invalid]) == 1`
- [ ] **Step 2: Run** `python3 -m unittest tests.test_check_skill -v`. Expected: FAIL (ImportError / module missing).
- [ ] **Step 3: Implement** `scripts/check_skill.py` with the interfaces above (stdlib only; parse front matter by hand between the first two `---` lines; add `scripts/__init__.py` and `tests/__init__.py` so the imports work).
- [ ] **Step 4: Run** the same command. Expected: all 8 tests PASS.
- [ ] **Step 5: Commit** `git add scripts tests && git commit -m "Add mechanical checker for skill files"`

### Task 2: Eval cases, fixture repo, baseline run (RED)

**Files:**
- Create: `evals/cases.md`, `evals/fixture-repo/` (`package.json`, `src/locales/en.json`, `src/locales/vi.json`, `src/App.jsx`, `src/Checkout.jsx`), `evals/results/baseline.md`

**Interfaces:**
- Produces: case IDs `A-01…A-08` (Mode A, in repo) and `B-01…B-12` (Mode B, review). Each case has: `id`, `mode`, `input`, `context`, and `pass:` a list of checkable criteria. Task 9 reruns exactly these.

Case format (use exactly):

```markdown
## A-06 Placeholders and plurals
- mode: A
- context: fixture-repo; task "add a cart badge string: '{{count}} items in your cart'"
- input: en.json key `cart.badge` with `_one`/`_other`
- pass:
  - `{{count}}` appears unchanged in vi value(s)
  - no invented plural word forms; one Vietnamese form is fine
  - uses the voice file pronoun
```

Required cases (write the rest of the content yourself):
- A-01 first run in fixture-repo with no `docs/ux-voice.md` → the file gets created with defaults and there's a one-line notice; no questions asked first.
- A-02 add a new error string to `en.json` → the `vi.json` value follows the error pattern and doesn't read as a literal translation.
- A-03 a payment-confirm button → `[Động từ] [đối tượng]`, not "OK"/"Đồng ý".
- A-04 Vietnamese hardcoded in `src/Checkout.jsx`, no locale file involved → the skill still applies.
- A-05 the fixture variant where existing `vi.json` strings consistently use *quý khách* → new strings use *quý khách*.
- A-06 placeholders/plurals (above).
- A-07 nearby weak strings exist → only the in-scope string changes, and the others are mentioned.
- A-08 repo uses old-style *xoá* → new strings use *xoá*.
- B-01…B-06 pasted weak strings covering: a vague error ("Đã xảy ra lỗi"), "Bạn có chắc chắn muốn…không?", stacked *vui lòng*, a generic "OK" button, an empty state with no next step, a permission request with no benefit.
- B-07 the input is NFD text → the output is NFC.
- B-08 tight-space button where the English source is "Save" → output ≤ 3 words.
- B-09 a screenshot (an image of a login screen with weak copy; make a simple PNG with any tool, or an HTML page you screenshot) → strings get extracted and `Trước → Sau` is given with reasons.
- B-10 a URL review (serve a local HTML file, e.g. `python3 -m http.server`) → same output shape.
- B-11 a banking-domain string → formal register.
- B-12 a mixed-pronoun list (*bạn* and *quý khách*) → the inconsistency gets flagged.

`fixture-repo` holds a few deliberately weak, literal-translation strings in `vi.json` (e.g. "Đã xảy ra lỗi. Vui lòng thử lại sau.") plus matching `en.json` keys. A variant for A-05/A-08 goes in `evals/fixture-repo-formal/`.

- [ ] **Step 1: Write** `evals/cases.md` and both fixture repos.
- [ ] **Step 2: Check NFC** with `python3 -c "import unicodedata,pathlib,sys; bad=[p for p in pathlib.Path('evals').rglob('*') if p.is_file() and p.suffix in {'.md','.json','.jsx'} and unicodedata.normalize('NFC',p.read_text())!=p.read_text() and 'B-07' not in p.name]; print(bad); sys.exit(bool(bad))"`. Expected: `[]`. If B-07's NFD input lives inside `cases.md`, store it in its own file `evals/inputs/b07-nfd.txt` and leave that file out.
- [ ] **Step 3: Baseline run.** For each case, dispatch a fresh subagent **without** the skill, giving it the case context and input verbatim. Record each output and a pass/fail per criterion in `evals/results/baseline.md`, quoting any rationalisations word for word.
- [ ] **Step 4: Verify** that the baseline fails at least the anti-pattern criteria in B-01…B-06 and A-02. If it passes almost everything, sharpen the cases until they discriminate, and record that.
- [ ] **Step 5: Commit** `git add evals && git commit -m "Add eval cases, fixture repos and baseline results"`

### Task 3: Language rules — `dinh-dang.md` and `xung-ho-va-giong-dieu.md`

**Files:**
- Create: `ux-writing-vi/references/dinh-dang.md`, `ux-writing-vi/references/xung-ho-va-giong-dieu.md`
- Create (stub so the checker can run): `ux-writing-vi/SKILL.md` with front matter plus a "References" list linking every reference file that exists so far. Task 7 replaces the body.

**Interfaces:**
- Produces: section headings that SKILL.md (Task 7) points to: `dinh-dang.md` → `## Ngày giờ`, `## Số và tiền tệ`, `## Dấu câu và viết hoa`, `## Unicode và dấu thanh`; `xung-ho-va-giong-dieu.md` → `## Mặc định`, `## Chọn theo lĩnh vực`, `## Trợ từ`, `## Khi repo đã có cách xưng hô`.

- [ ] **Step 1: Read the Microsoft guide PDF** (download into the scratchpad; read the address, tone, grammar, punctuation, capitalization and locale-format sections). Write notes in your own words.
- [ ] **Step 2: Write `dinh-dang.md`**: date `dd/mm/yyyy`, 24-hour time, `.` as thousands separator and `,` as decimal, currency `100.000 đ` / `100.000 VND` (pick one default and state it), sentence-case capitalization, no title case, punctuation spacing, NFC, the tone-mark rule from Global Constraints. Each rule gets a ✅/❌ pair.
- [ ] **Step 3: Write `xung-ho-va-giong-dieu.md`**: the defaults exactly as in Global Constraints, the domain table, the particles table, the rule to follow the repo's existing pronoun, and 3–4 ✅/❌ pairs per section.
- [ ] **Step 4: Run** `python3 scripts/check_skill.py ux-writing-vi`. Expected: exit 0.
- [ ] **Step 5: Commit** `git add ux-writing-vi && git commit -m "Add formatting and address/tone references"`

### Task 4: `loi-dich-may-moc.md` and `thuat-ngu.md`

**Files:**
- Create: `ux-writing-vi/references/loi-dich-may-moc.md`, `ux-writing-vi/references/thuat-ngu.md`
- Modify: `ux-writing-vi/SKILL.md` (add links)

**Interfaces:**
- Consumes: the baseline rationalisations and failing outputs in `evals/results/baseline.md`.
- Produces: `loi-dich-may-moc.md` as a table `| Nghe như dịch | Tự nhiên hơn | Vì sao |`; `thuat-ngu.md` as a table `| Khái niệm | Dùng | Tránh | Ghi chú |`.

- [ ] **Step 1: Write `loi-dich-may-moc.md`**: at least 15 rows. It must cover every translated-sounding pattern seen in the baseline, plus: "Đã xảy ra lỗi", "Bạn có chắc chắn muốn…không?", stacked *vui lòng*, passive "được" calques ("Tệp đã được tải lên bởi…"), "Nhấp vào đây", English word order in titles, overuse of *của bạn*.
- [ ] **Step 2: Write `thuat-ngu.md`**: at least 30 common app terms (đăng nhập, đăng ký, mật khẩu, OTP, email, ứng dụng, thông báo, cài đặt, giỏ hàng, thanh toán, …), with the keep-loanword decisions from the spec (keep "OTP", "email").
- [ ] **Step 3: Run** the checker. Expected: exit 0.
- [ ] **Step 4: Commit.**

### Task 5: Patterns — `mau-noi-dung.md` and `examples/truoc-va-sau.md`

**Files:**
- Create: `ux-writing-vi/references/mau-noi-dung.md`, `ux-writing-vi/examples/truoc-va-sau.md`
- Modify: `ux-writing-vi/SKILL.md` (add links)

**Interfaces:**
- Produces: one `##` section per element, in this order: Tiêu đề, Nút và liên kết, Lỗi (nhập liệu / hệ thống / chặn / quyền), Thông báo thành công, Hộp thoại xác nhận, Trạng thái trống, Xin quyền truy cập, Thông báo đẩy, Nhãn và gợi ý trong form, Giới thiệu (onboarding). Each section has: purpose (1 line), pattern, 3 ✅ examples, 2 ❌ examples with the reason. SKILL.md's pattern table (Task 7) summarises these one line each.

- [ ] **Step 1: Write `mau-noi-dung.md`** using the spec's patterns: button `[Động từ] [đối tượng]`; error `[Điều gì không thành công]. [Vì sao]. [Cần làm gì].` with the spec's example "Chưa lưu được thay đổi. Mất kết nối mạng. Kiểm tra mạng rồi thử lại."; confirmation dialogs name the action in both the title and the button ("Xóa ảnh?" / "Xóa" / "Hủy"). Add a short "Khi chỗ hẹp" note: Vietnamese usually runs longer than English, so cut words instead of abbreviating.
- [ ] **Step 2: Write `examples/truoc-va-sau.md`**: at least 20 `Trước → Sau — lý do` items across element types, all fresh and none taken from the eval cases verbatim (to avoid teaching to the test).
- [ ] **Step 3: Run** the checker. Expected: exit 0.
- [ ] **Step 4: Commit.**

### Task 6: Accessibility — `tiep-can.md`

**Files:**
- Create: `ux-writing-vi/references/tiep-can.md`
- Modify: `ux-writing-vi/SKILL.md` (add link)

- [ ] **Step 1: Write** sections on alt text, descriptive link text (no "Nhấn vào đây"), screen readers (the full words are read, so avoid abbreviations like "SĐT", "TK" in labels; `lang="vi"`), not relying on color alone, error text tied to the field, and plain words over Hán-Việt jargon where a common word exists. Paraphrase from the original's `references/accessibility-guidelines.md` (MIT); the examples are fresh Vietnamese.
- [ ] **Step 2: Run** the checker. Expected: exit 0.
- [ ] **Step 3: Commit.**

### Task 7: `SKILL.md` and the voice-file template

**Files:**
- Modify: `ux-writing-vi/SKILL.md` (full body)
- Create: `ux-writing-vi/templates/giong-van.md`

**Interfaces:**
- Consumes: the section headings from Tasks 3–6.
- Produces: front-matter `description` that triggers on writing/editing/reviewing Vietnamese UI text, Vietnamese locale files (`vi.json`, `*_vi.arb`, `vi.lproj`), or English-source keys when the repo has a Vietnamese locale. It should be written as "Use when…" and must not summarise the workflow (per writing-skills). The template's fields are exactly: `Xưng hô với người dùng`, `Ứng dụng tự xưng`, `Giọng điệu`, `Trợ từ được dùng`, `Thuật ngữ ưu tiên`, `Ví dụ trong ứng dụng`.

- [ ] **Step 1: Write `templates/giong-van.md`** with the fields above, the default values from Global Constraints, and a one-line comment per field explaining how to change it.
- [ ] **Step 2: Write the `SKILL.md` body** with these sections:
  1. When to use (Mode A / Mode B triggers)
  2. Mode A workflow, the spec's steps 1–6, including voice-file creation at `docs/ux-voice.md` from the template, domain-based defaults, and adopting the repo's existing pronoun and tone marks
  3. English-source keys: write fresh from the intent, then check against `loi-dich-may-moc.md`
  4. Mode B workflow: extract → `Trước → Sau` + a one-line reason in Vietnamese → flag inconsistencies → offer to apply
  5. The four standards in brief, in Vietnamese terms
  6. The one-line-per-element pattern table
  7. The top 5 translated-sounding traps
  8. A reference map: which file to load and when
  9. Keep placeholders byte-for-byte; output NFC

  Language of the instructions: start in English, with all examples in Vietnamese. If the Task 9 GREEN run shows weaker compliance, try a Vietnamese version and keep whichever scores better (the spec leaves this to the builder).
- [ ] **Step 3: Run** the checker. Expected: exit 0, ≤ 200 lines.
- [ ] **Step 4: Commit.**

### Task 8: README, LICENSE, packager

**Files:**
- Create: `ux-writing-vi/README.md`, `ux-writing-vi/LICENSE`, `scripts/package_skill.py`
- Test: `tests/test_package_skill.py`

**Interfaces:**
- Produces: `package_skill(skill_dir: Path, out_path: Path) -> Path` builds a zip containing `ux-writing-vi/…`. It runs `check_skill` first and raises `ValueError` listing the errors if any are found. CLI: `python3 scripts/package_skill.py ux-writing-vi dist/ux-writing-vi.zip`.

- [ ] **Step 1: Write failing tests**: `test_zip_contains_skill_md` (the zip namelist includes `ux-writing-vi/SKILL.md` and every reference file), and `test_refuses_invalid_skill` (an invalid temp dir raises `ValueError`).
- [ ] **Step 2: Run** `python3 -m unittest tests.test_package_skill -v`. Expected: FAIL.
- [ ] **Step 3: Implement** `package_skill`, using `zipfile` and leaving out dotfiles.
- [ ] **Step 4: Run** the tests. Expected: PASS.
- [ ] **Step 5: Write `README.md`** (Vietnamese first): what it does, the two modes, install instructions (Claude Code: copy or symlink into `~/.claude/skills/ux-writing-vi`; other agents: unzip into their skills folder), the voice file, credits (original skill by Christopher Greer, MIT; language rules paraphrased from the Microsoft Vietnamese Style Guide), then a short English section. Write `LICENSE` as MIT covering this work, keeping the original's copyright notice.
- [ ] **Step 6: Run** the checker and the packager. Expected: exit 0, and `dist/ux-writing-vi.zip` exists. Add `dist/` to `.gitignore`.
- [ ] **Step 7: Commit.**

### Task 9: GREEN run, loophole closing, local install

**Files:**
- Create: `evals/results/with-skill.md`
- Modify: any skill file, as the failures require

- [ ] **Step 1: Install** for local use: `ln -s "$PWD/ux-writing-vi" ~/.claude/skills/ux-writing-vi`.
- [ ] **Step 2: Rerun every case from Task 2** with fresh subagents, this time with the skill loaded (tell each one to read `ux-writing-vi/SKILL.md` first and follow it). For the Mode A cases, run inside a fresh copy of the fixture repo. Record pass/fail per criterion in `evals/results/with-skill.md`, next to the baseline results.
- [ ] **Step 3: Close loopholes**: for each failed criterion, add the smallest rule or counter-example that addresses it, then rerun only that case. Repeat until every criterion passes or you've written down why a remaining failure is acceptable.
- [ ] **Step 4: Run** `python3 scripts/check_skill.py ux-writing-vi && python3 -m unittest -v`. Expected: exit 0, and all tests pass.
- [ ] **Step 5: Author review**: give the author `evals/results/with-skill.md` and 10 sample outputs to judge for naturalness. This is the native-reviewer step from the spec, and it's a manual gate.
- [ ] **Step 6: Commit.**
