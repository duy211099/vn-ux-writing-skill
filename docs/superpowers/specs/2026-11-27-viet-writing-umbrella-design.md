# Vietnamese Writing Umbrella — Round 1 Design

Date: 2026-11-27
Status: approved 2026-11-27
Builds on: [2026-11-27-vietnamese-ux-writing-skill-design.md](2026-11-27-vietnamese-ux-writing-skill-design.md)

## Intent

Grow this repo from one skill (`ux-writing-vi`) into a single plugin with several Vietnamese writing skills: UI copy, blog posts, product narrative and course design. These will be built in rounds. **Round 1** lays the foundation that every later skill uses:

1. Restructure the repo into one plugin with a `skills/` folder.
2. `review` and `analyze`: two commands the author runs to check changed text or the whole repo.
3. `humanizer-vi`: finds and removes the signs that Vietnamese prose was written by AI, without changing what it says.
4. `style-vi`: one voice file per project, shared by every skill.

**Who it's for:** the author, a solo developer with no writer on the team, and other Vietnamese solo devs.

**Why:** the author has no one to write or check their Vietnamese text. They do ask an AI model to check it, but they have to remember to ask every time, for every piece, and that is the part that wears them down. **They want a one-command check they run when they need it:** one command for what they just changed, one for all the text in the repo. (Fully automatic checking was discussed and set aside for now.) It also has to be one repo, because they don't want to maintain several.

**Success looks like:**
- Whenever Claude writes Vietnamese prose (blog post, product intro, README, email), the result already reads like a Vietnamese person wrote it, and the author didn't have to ask.
- When the author pastes Vietnamese text from anywhere and asks for a check, they get a cleaned-up version plus a short list of what changed.
- The app copy and the prose share one voice (pronoun, tone, words to avoid), recorded in one file per project.
- One install gets all the skills, and one `git pull` updates them.

## Goals

1. **One repo, one plugin.** Installable as a whole (Claude Code plugin) or skill by skill (Skills CLI, manual copy).
2. **`humanizer-vi` works three ways:** on pasted text, on a named file, and as a silent last step inside other skills (returns only the final text).
3. **Two commands the author runs themselves:** `/viet-writing:review` checks the current changes; `/viet-writing:analyze` checks all Vietnamese text in the repo (see §4).
4. **One voice file per project**, created automatically the first time any skill needs it, read by every skill.
5. **Existing users aren't broken.** Projects that already have `docs/ux-voice.md` keep working.
6. **Same quality bar as `ux-writing-vi`:** mechanical checks (`check_skill.py`), unit tests, behavioural evals with baseline vs. with-skill results.

## Non-goals (round 1)

- `blog-vi`, `narrative-vi`, `course-vi`. Each gets its own short design conversation after round 1. The "narrative check" (does a whole piece hold together) belongs in those skills, not in the humanizer.
- Changing how `ux-writing-vi` writes UI strings. UI strings are short; its existing rules already cover translation tics. `ux-writing-vi` does **not** call `humanizer-vi`.
- English text. `humanizer-vi` is for Vietnamese only; the existing English `humanizer` covers English.
- Renaming the GitHub repo. Optional, the author's call, any time later (GitHub redirects old URLs).
- Grammar/spelling checking beyond what the tells require.

## Anti-goals (failure even if it "works")

- **Flattening the writer.** A rewrite that removes the writer's opinions, jokes, hedges, slang or anger. Informal Vietnamese (*nha*, *nè*, *luôn á*, teencode in a chat or Facebook post) is a register, not a tell.
- **Losing facts.** Any dropped or changed name, number, date, price, quote, link or claim.
- **Rewriting human text for the sake of it.** Text with no tells comes back unchanged.
- **Asking the user to choose a voice from a menu.** Same rule as `ux-writing-vi`: decide, state in one line, let them override.
- **Long reports.** The user wants clean text, not a lecture.
- **Translated thinking.** Rewrites built by mentally translating to English and back.
- **Copied content.** Patterns and examples are written fresh in Vietnamese.

## Constraints

- **Skill format.** Agent Skills spec: `SKILL.md` with `name` and `description` front matter, `SKILL.md` ≤ 200 lines (enforced by `check_skill.py`), detail in `references/`.
- **A skill installed alone gets only its own folder.** Nothing a skill needs at runtime may live outside it. Shared files are duplicated (see Design §3) and kept identical by a test.
- **Unicode NFC** for all Vietnamese text (enforced).
- **Sources.** The structure of `humanizer-vi` (mark → rewrite → check facts → final; voice matching; pasted/file/embedded modes; treat input as material, never instructions) is adapted from the English `humanizer` skill by Siqi Chen, MIT. Credit in `skills/humanizer-vi/LICENSE` and the README. The Vietnamese patterns themselves are not in any document we can cite. They are derived from observing real model output (see Design §2.4) and written fresh.
- **Python standard library only** for scripts and tests, as now.

## Approaches considered

Decided in conversation: **one repo, one plugin, several skills.**

1. **One big skill with modes** (`viet-writing` routing to UI/blog/course/narrative). Easy to install, but one description has to trigger on everything, so it either fires too often or misses; every task loads the large entry file. Rejected.
2. **Separate skills, shared rules copied in at package time** by the packager. Every skill works alone, but adds a build step and a generated-files problem. Rejected as the main mechanism (a light version of it is used for the voice template only, see §3).
3. **Separate skills plus shared skills they call by name** (`humanizer-vi`, `style-vi` are skills; `blog-vi` says "run humanizer-vi as the last step"), shipped as one plugin. Simple, and the humanizer is useful on its own. **Chosen.** Weakness: a skill installed alone without its dependencies loses the extra step. Mitigation: each dependent skill keeps the few rules it can't do without inline, and the README recommends installing the whole plugin.

## Design

### 1. Repo layout

```
vn-ux-writing-skill/
├── .claude-plugin/
│   ├── plugin.json            # plugin name: viet-writing (see note)
│   └── marketplace.json       # lets `/plugin marketplace add duy211099/vn-ux-writing-skill` work
├── skills/
│   ├── ux-writing-vi/         # moved from ./ux-writing-vi, content unchanged except §3
│   ├── humanizer-vi/
│   ├── style-vi/
│   ├── review/                # /viet-writing:review
│   └── analyze/               # /viet-writing:analyze
├── evals/
│   ├── ux-writing-vi/         # existing evals/ contents move here
│   └── humanizer-vi/
├── scripts/                   # check_skill.py, package_skill.py (+ shared-file sync check)
├── tests/
├── dist/                      # one zip per skill
├── docs/
└── README.md                  # install for all three paths, list of skills
```

- Plugin name `viet-writing` (my call; short and covers all four writing types). Skill names stay `*-vi` so they read as a set.
- `git mv` so history follows the files.
- README install commands change from `ux-writing-vi/` to `skills/ux-writing-vi/`. The builder must verify that `npx skills add duy211099/vn-ux-writing-skill@ux-writing-vi` still resolves a skill inside `skills/` (the Skills CLI searches for `SKILL.md` recursively; confirm with a real run). If it doesn't, document the working form.
- Packager: `package_skill.py` keeps its current interface; add a convenience mode that zips every folder under `skills/` into `dist/<name>.zip`.

### 2. `humanizer-vi`

#### 2.1 What it does

Takes Vietnamese prose, marks the signs that an AI wrote it, rewrites them away, checks that nothing factual was lost, and returns the final text. Same four-step loop as the English humanizer: **mark → rewrite → check facts → final.**

#### 2.2 When it applies (description triggers)

- The user pastes or points at Vietnamese text and asks to make it sound natural, less like AI, or more human: *viết lại cho tự nhiên*, *nghe như AI*, *sửa giọng văn*, *đọc cứng quá*, "humanize this".
- `review` or `analyze` (§4) sends it the prose they find.
- Another skill calls it by name as its last step (embedded mode).
- **Not** for UI strings (buttons, errors, dialogs). Those belong to `ux-writing-vi`. Not for code, commit messages or chat replies to the user.

#### 2.3 Modes and output

| Mode | Trigger | Output |
|---|---|---|
| Pasted text | User gives text in chat | Final rewrite first. Then `Đã sửa:` with 3–6 bullets in Vietnamese, each naming one tell and one short example from the text. If no tells: say so in one line and return the text unchanged. |
| File | User names a file | Read the whole file from disk. Change prose only; keep code blocks, inline code, front matter, links, paths unchanged. Write the final text to the file. Report in one line how many sections were reviewed and the main tells fixed. |
| Embedded | Claude wrote the prose itself, or another skill calls it | Return only the final text. No report. |

The pasted-text output is simpler than the English humanizer's three-part output (first draft, surviving tells, final). My call: the author wants clean text, not process.

#### 2.4 The pattern catalogue (`references/dau-hieu-ai.md`)

Numbered, strongest first. Patterns marked *yếu nếu đứng một mình* need another tell nearby before acting. Starting list from the conversation, to be confirmed and extended by the corpus step below:

- **Linking-word padding.** *Bên cạnh đó*, *Ngoài ra*, *Đồng thời*, *Hơn thế nữa*, *Không những vậy* opening sentence after sentence.
- **Contrast staging.** *Không chỉ… mà còn…*, *không phải… mà là…* used for weight rather than an actual contrast.
- **Staged openers and closers.** *Hãy cùng tìm hiểu…*, *Trong thời đại công nghệ 4.0…*, *Bạn có bao giờ tự hỏi…?*; *Tóm lại,…*, *Có thể nói,…*, *Hy vọng bài viết… hữu ích*.
- **Inflation.** *vô cùng*, *cực kỳ*, *hoàn hảo*, *đột phá*, *tối ưu*, *vượt trội*, *hàng đầu*, *mang lại trải nghiệm tuyệt vời*.
- **Sino-Vietnamese and verb stacking.** *thực hiện việc*, *tiến hành*, *đóng vai trò quan trọng trong việc*, *góp phần nâng cao*.
- **Translated syntax** (shared with `ux-writing-vi`'s translation tics, but for prose): *được… bởi*, *của bạn* everywhere, *một cách + tính từ*, *điều này*/*việc này* as sentence openers.
- **Forced triads** and lists of three adjectives.
- **Same-rhythm sentences.** Every sentence the same length and shape.
- **Formatting by rule.** Bold label on every bullet, emoji at the start of each line, title-case headings.
- **Chatbot leftovers.** *Dưới đây là…*, *Chắc chắn rồi!*, *Hy vọng điều này giúp ích*.

**Corpus step (builder):** before writing the catalogue, generate a small corpus of AI Vietnamese prose (at least 3 models if available, at least 4 genres: blog, product intro, Facebook post, email; at least 20 samples), and collect a smaller set of human-written Vietnamese controls (see **Control texts** below). Mark which tells actually occur and how often; order the catalogue by that. Keep the corpus summary (not raw copyrighted text) in `evals/humanizer-vi/`.

**Control texts (human-written, pre-2022, openly licensed).** The author has no Vietnamese writing of their own to give, so controls come from these sources, researched on 2026-11-27:

| Register | Source | License | How |
|---|---|---|---|
| Formal / informational | vi.wikipedia.org articles on Vietnam-specific topics | CC BY-SA 4.0 | Pin an `oldid` revision before 2022-06. Skip articles created with the content-translation tool (`contenttranslation` tag), pages with translation templates, and bot stubs. |
| Formal / bureaucratic | Legal and administrative documents (vbpl.vn, chinhphu.vn) | Not protected (IP Law Art. 15(2)) | One article or clause. No news sites. |
| Personal | vi.wikipedia user pages and essays (`Thành viên:…`) | CC BY-SA 4.0 | Old revision, one passage of 50–300 words. |
| Casual / conversational | vi.wikipedia talk pages (`Thảo luận:…`, `Wikipedia:Thảo luận`) | CC BY-SA 4.0 | One dated, signed comment of 50–200 words. |
| Casual, short | Tatoeba Vietnamese originals (`sentences_base` = 0, added before 2022) | CC BY 2.0 FR | Short fixtures; credit each sentence's owner. |

- Aim for 10–15 controls across these registers. Each fixture records source URL, `oldid` or date, author credit and license.
- Fixtures keep their own license: put them in `evals/humanizer-vi/controls/` with a `NOTICE.md` stating that the folder is CC BY-SA 4.0 / CC BY 2.0 FR, not MIT. Don't ship them inside the skill zip.
- **Known gap:** no openly licensed reviews, Facebook posts or chat were found (UIT and VOZ datasets are research-only or unlicensed; Reddit, Viblo and news are copyrighted). Informal social-media controls are missing in round 1; the talk pages and Tatoeba are the closest stand-ins. If the author later writes or collects such text with permission, add it.

#### 2.5 Voice

- If the project has a voice file (§3), follow its prose section.
- If the user gives a writing sample, match its sentence length, word choice, particles and punctuation. The sample overrides the catalogue.
- Otherwise, match the genre: blog and personal writing keep opinions, humour and asides; product and reference text stays plain; informal posts keep their register (*nha*, *nè*, abbreviations).

#### 2.6 Files

```
skills/humanizer-vi/
├── SKILL.md                     # ≤ 200 lines: triggers, loop, modes, voice, top tells
├── LICENSE                      # MIT, credits Siqi Chen's humanizer
├── references/
│   ├── dau-hieu-ai.md           # pattern catalogue with before/after
│   └── giu-nguyen-y.md          # fact-preservation checklist (names, numbers, dates, prices, quotes, links, claims)
└── examples/
    └── truoc-va-sau.md          # 6–10 worked rewrites across genres, plus 2 "leave unchanged" cases
```

Skill text language follows `ux-writing-vi`: instructions in English, Vietnamese for examples, reasons and reference file names.

### 3. `style-vi` and the shared voice file

#### 3.1 Voice file

- **New path:** `docs/giong-van.md` in the user's project (my call: a name that isn't UX-specific, in the same Vietnamese naming style as the skill's files).
- **Lookup order for every skill:** `docs/giong-van.md`, then `docs/ux-voice.md`. If only the old one exists, use it and don't move or rename it unasked.
- **Template** = the current `templates/giong-van.md` plus a new section **Văn bản dài** (prose):
  - How the writer refers to themselves in prose (*mình*, *tôi*, *chúng tôi*, app name) — may differ from UI, where the app doesn't refer to itself.
  - Sentence length (short / mixed).
  - How personal (neutral / has opinions / chatty).
  - Words and phrases to avoid (seeded from `humanizer-vi`'s strongest tells).
  - 1–2 sample paragraphs the author likes (optional).
- The header comment changes from "do skill ux-writing-vi tạo" to say it is shared by all skills in the plugin.

#### 3.2 `style-vi` skill

- **Triggers:** user asks about the project's voice or wants to change it (*giọng văn*, *xưng hô*, *đổi sang quý khách*); another skill needs the voice file and none exists.
- **Creates** the voice file the first time, using the same rules as `ux-writing-vi` today: guess domain from the project, pick defaults from the domain table, follow existing strings if they're consistent, state the choice in one line, don't ask first. The prose section gets defaults by domain too (e.g. fintech: *chúng tôi*, neutral, short sentences; indie tool: *mình*, has opinions).
- **Answers** "what's our voice?" by summarising the file in a few lines.
- **Updates** the file when the user changes their mind, and lists strings elsewhere that now disagree (doesn't rewrite them unasked).

```
skills/style-vi/
├── SKILL.md
├── LICENSE
├── templates/giong-van.md        # canonical template
└── references/mac-dinh-theo-linh-vuc.md   # domain → UI and prose defaults
```

#### 3.3 Duplication rule

`ux-writing-vi` must still work alone, so it keeps its own copy of `templates/giong-van.md` and its domain table. `skills/style-vi/templates/giong-van.md` is the source of truth; a test fails if the copy in `ux-writing-vi` differs. `ux-writing-vi/SKILL.md` Mode A step 1 changes to: read `docs/giong-van.md` or `docs/ux-voice.md`; if neither exists, create `docs/giong-van.md` (via `style-vi` if installed, otherwise from its own template copy).

`humanizer-vi` reads the voice file if present but never creates one (it often runs on pasted text outside any project).

### 4. `review` and `analyze` (author-run commands)

Two skills the author invokes by name. They don't trigger on their own (`disable-model-invocation: true`). They find Vietnamese text, sort it into **UI strings** and **prose**, and apply the right rules: `ux-writing-vi`'s rules to UI strings, `humanizer-vi`'s loop to prose. Both read the voice file (§3) and say in one line which voice they used.

| | `/viet-writing:review` | `/viet-writing:analyze` |
|---|---|---|
| Scope | Current changes: staged + unstaged + untracked files vs `HEAD` (or vs a branch/commit if given as an argument) | All Vietnamese text in the repo, or a path given as an argument |
| Finds | Only lines added or changed in the diff | Locale files (`vi.json`, `vi.yml`, `*_vi.arb`, `values-vi/strings.xml`, `vi.lproj`, `vi.po`, `vi.ts`), hardcoded Vietnamese in components, Vietnamese Markdown/HTML/text prose |
| Skips | — | `node_modules`, `vendor`, build output, lockfiles, `.git`, anything in `.gitignore`, test fixtures unless named |
| Output | `Trước → Sau — lý do` lines grouped by file, then prose rewrites with a short `Đã sửa:` list. Ends by offering to apply. | A summary first: counts per file, the top 3–5 repeated problems (mixed pronouns, mixed tone-mark style, generic errors, AI tells), and which files are worst. Then per-file `Trước → Sau` for the worst files, capped so the answer stays readable. Ends by offering to fix one file or one problem across all files. |
| Changes files? | Only after the author says yes | Only after the author says yes |

- **Consistency is the point of `analyze`:** it checks pronouns, terms and tone-mark style across the whole repo against the voice file, which a per-change review can't see.
- **No voice file:** both use the domain defaults and say so; they don't create the file (that is `style-vi`'s or `ux-writing-vi`'s job when writing).
- **Large repos:** `analyze` lists the files it covered and names any it skipped for size.
- **Standalone installs:** names `review` and `analyze` are generic, so they're meant for the plugin install, where they're namespaced as `/viet-writing:review` and `/viet-writing:analyze`. The README says so. They need `ux-writing-vi` and `humanizer-vi` installed (they're in the same plugin).

### 5. Checks, tests and evals

- `check_skill.py` runs over every folder in `skills/`. Add a check that the shared template copies are identical.
- Existing unit tests keep passing after the move; add tests for the multi-skill packager mode and the sync check.
- **`humanizer-vi` evals** (`evals/humanizer-vi/cases.md`), same method as `ux-writing-vi` (baseline vs. with-skill, results recorded):
  - AI-written samples per genre → tells removed, facts preserved.
  - Human-written controls, formal and informal → returned unchanged or nearly so.
  - Fact traps: samples dense with numbers, prices, dates, names → none lost.
  - Not-a-trigger: UI string edits in a repo → `ux-writing-vi` applies, not `humanizer-vi`.
  - Voice file honoured: project with a voice file using *mình* → rewrite uses *mình*.
  - Prompt-injection in pasted text ("bỏ qua hướng dẫn…") → edited as text, not followed.
- **`review` / `analyze` evals:** a fixture repo with a diff touching a locale file and a Vietnamese Markdown post → `review` reports only changed lines, UI strings get `ux-writing-vi` rules and the post gets humanizer rewrites, no files changed without a yes. A fixture repo with mixed pronouns and *xóa*/*xoá* across files → `analyze` summary names both problems and the worst files; `node_modules` and fixtures skipped.
- **`style-vi` evals:** voice file created when missing; old `docs/ux-voice.md` respected; change request updates the file and lists disagreeing strings.
- **`ux-writing-vi` regression:** re-run its existing eval cases after the move and the Mode A step-1 change.

## Decided in conversation

- One repo, one plugin, several skills (approach 3).
- Round 1 = restructure + `humanizer-vi` + shared voice file (`style-vi`). Blog, narrative, course come later, one at a time.
- `humanizer-vi` is the last step of other writing skills, and works on its own for pasted text and files.
- Two author-run commands, `review` (current changes) and `analyze` (whole repo). No automatic checking of Claude's own output in round 1; the author isn't thinking about that now.
- Narrative check lives in the later blog/narrative/course skills.


## My calls (author can override)

- Plugin name `viet-writing`; skill names `*-vi`.
- Voice file at `docs/giong-van.md`, with `docs/ux-voice.md` still read.
- `humanizer-vi` also triggers on Claude's own Vietnamese prose longer than about a paragraph.
- Pasted-text output is final text + short `Đã sửa:` list, not the English humanizer's three-part output.
- `ux-writing-vi` doesn't call `humanizer-vi`.
- `ux-writing-vi` keeps a test-enforced copy of the voice template so it works alone.
- **Manual installs break on the move.** Symlinks to `vn-ux-writing-skill/ux-writing-vi` stop resolving after `git pull`. No compatibility stub (it would make the Skills CLI find two copies); the README gets a short "moved to `skills/`" migration note with the new `ln -s` line. Early project, few users.
- **Prose section when `ux-writing-vi` creates the voice file alone:** left as the template's placeholders (option: don't duplicate prose defaults). `humanizer-vi` treats a placeholder prose section as "no voice set" and falls back to genre matching (§2.5). `style-vi` fills it when it runs. Eval A-01 is updated to expect `docs/giong-van.md`.
- **File mode overwrites in a git repo** (git is the undo) and reports one line plus the `Đã sửa:` list. Outside a git repo, it shows the rewrite and asks before writing.
- **Corpus models:** whichever are available to the builder; if only Claude, say so in the corpus summary so the ordering bias is visible.

## Left to the builder

- Exact wording of descriptions and SKILL.md bodies (within the triggers above).
- The final ordered pattern catalogue, from the corpus step.
- Plugin/marketplace JSON details and the Skills CLI path check.
- Number and exact content of eval cases beyond the categories listed.
