# Vietnamese UX Writing Skill — Design

Date: 2026-11-27
Status: draft, awaiting approval

## Intent

A Claude skill that writes and improves Vietnamese interface text (buttons, labels, errors, empty states, notifications, onboarding, permission prompts) so that it sounds native and helps the user act.

**Who it's for:** solo developers who write their own app copy and have no UX writing experience. The author uses it first; it is published as open source for other Vietnamese devs.

**Why:** solo devs either write Vietnamese UI text in a rush while coding, or translate English UI text literally. Both produce copy that is unclear, inconsistent in pronouns, or "sounds translated". Professional UX writing guidance is in English, paywalled, or aimed at professionals.

**Success looks like:** a solo dev builds an app with Claude, and the Vietnamese strings that come out are consistent in voice, natural, and actionable — without the dev having to know any UX writing theory. When they ask for a review of existing copy, they get a better version plus a short reason they can learn from.

## Goals

1. **In-repo by default.** When Claude writes or edits UI strings in a code repo (JSX/TSX, i18n JSON/YAML, Flutter ARB, Swift/Kotlin string files, HTML templates), the skill applies automatically and keeps the voice consistent with a per-project voice file.
2. **Review on request.** User gives text, a screenshot, or a URL → skill returns an improved version with a one-line reason per change.
3. **Decides for the user.** A novice can't answer "which register?". The skill picks a sensible default, states it in one line, and lets the user override.
4. **Native, not translated.** Examples and patterns are written in Vietnamese from scratch, not translated from English.
5. **Shareable.** Installable as a standard agent skill (Claude Code, and other agents supporting the skills spec), MIT licensed, crediting the original.

## Non-goals

- Not a fork/translation of the original English skill's full content.
- Not a translation tool (English → Vietnamese i18n). It may improve Vietnamese strings that came from translation, but its job is good Vietnamese copy, not translation fidelity.
- Not for professional content designers' deep workflows (voice-chart workshops, research benchmarks, Figma plugin integration).
- Not a brand-voice generator for large companies.
- No English-language UX guidance.

## Anti-goals (failure even if it "works")

- Output that is grammatical but sounds translated (e.g. "Bạn có chắc chắn muốn…không?" everywhere, "Đã xảy ra lỗi", stacked "vui lòng").
- Asking a novice a menu of theory questions before helping.
- Inconsistent pronouns across one app (*bạn* on one screen, *quý khách* on another).
- Long lectures. Explanations are one line per change.
- Content copied from copyrighted sources.

## Constraints

- **Sources: free/open documents only.**
  - Original UX Writing Skill (MIT, Christopher Greer) — framework: four quality standards (purposeful, concise, conversational, clear), patterns, editing approach. Credit in README and LICENSE.
  - Microsoft Vietnamese Localization Style Guide (free PDF) — language rules: address forms, punctuation, capitalization, date/number/currency formats. It is copyrighted (free, not open-licensed), so **paraphrase rules; do not copy text**. Adapt its formal, software-oriented tone toward a friendlier app voice.
  - Google Material codelab (Vietnamese) — only as a cautionary "sounds translated" reference.
  - Excluded: *Strategic Writing for UX* (Podmajersky) and Khúc Cẩm Huyên's books (paywalled / copyrighted).
- All Vietnamese examples are written fresh.
- English benchmarks that don't carry over are dropped or replaced: US reading-grade levels, "use 'you'", English character counts. Replace with Vietnamese-appropriate guidance (e.g. short sentences, word-count limits per element, Vietnamese text expands vs. English when space is tight).
- Text must be Unicode NFC (pre-composed diacritics).

## Approaches considered

1. **Fork and translate the original** — keep all ~3,600 lines and swap examples. Most complete, but long, aimed at professionals, and translation invites the "sounds translated" problem. Rejected.
2. **New Vietnamese-first skill, crediting the original** — short `SKILL.md` built around the in-repo workflow, plus focused Vietnamese references. **Chosen**: matches novice users (short, decides for them) and the native-voice goal.
3. **Vietnamese add-on to the original English skill** — least work, but two installs and English examples pull Claude toward translated phrasing. Rejected.

## Design

### Skill structure

```
ux-writing-vi/
├── SKILL.md                         # when to use, the workflow, core rules, short pattern table
├── references/
│   ├── xung-ho-va-giong-dieu.md     # pronouns, register, particles, default + how to choose
│   ├── mau-noi-dung.md              # patterns per UI element, Vietnamese examples, do/don't
│   ├── dinh-dang.md                 # dates, times, numbers, currency (đ / VND), punctuation, capitalization, NFC
│   ├── loi-dich-may-moc.md          # "sounds translated" anti-patterns → natural rewrites
│   ├── thuat-ngu.md                 # starter glossary: loanword vs Vietnamese choices (OTP, email, đăng nhập…)
│   └── tiep-can.md                  # accessibility: alt text, screen readers, link text, Vietnamese specifics
├── templates/
│   └── giong-van.md                 # voice-file template that gets copied into the user's repo
├── examples/
│   └── truoc-va-sau.md              # before → after, with one-line reasons
├── README.md                        # Vietnamese first, short English section; install + credit
└── LICENSE                          # MIT, credits original author
```

`SKILL.md` stays short (target under ~200 lines) and loads references only when needed (progressive disclosure). File names are Vietnamese without diacritics.

### The per-project voice file

- Location: `docs/ux-voice.md` in the user's repo (builder may adjust the path; must be a single, discoverable file).
- Contents (a handful of lines, not a workshop):
  - How the app addresses the user (default *bạn*)
  - How the app refers to itself (default: avoid self-reference; use the app name if needed; *chúng tôi* only for formal/finance contexts)
  - Register: friendly / neutral / formal (default: neutral-friendly)
  - Particles allowed (default: *nhé* sparingly in friendly moments; no *nha*, *ạ* in UI; *vui lòng* only in formal or apologetic contexts)
  - Preferred terms (e.g. "đăng nhập" not "login"; keep "OTP", "email")
  - A few examples from this app once they exist
- **Creation:** first time the skill runs in a repo without the file, it infers defaults from the app's domain (banking/government → more formal, *quý khách* possible; consumer/social → *bạn*, friendlier), writes the file, and tells the user in one line what it chose and how to change it. It does not ask questions first.
- If existing strings in the repo already use a consistent pronoun, the skill adopts it rather than imposing the default.

### Workflow

**Mode A — while coding (automatic).** Triggers when Claude writes or edits user-facing strings in a repo that has a Vietnamese locale (e.g. `vi.json`, `app_vi.arb`, `vi.lproj`) or Vietnamese UI text.

*Multi-language repos (decided by the author):* when Claude adds or changes a key whose source is English (e.g. `en.json`), the skill writes the Vietnamese value **fresh from the intent** of the English string, as copy, not as a literal translation. The "sounds translated" anti-patterns (`loi-dich-may-moc.md`) are therefore used while writing, not only in review.
1. Read `docs/ux-voice.md` (create it if missing, as above).
2. Identify the UI element type (button, error, empty state…) and look up the pattern.
3. Write the string following the voice file + pattern + formatting rules.
4. Keep terms consistent with the glossary and existing strings.
5. No explanation unless the change is non-obvious; the user is coding, not reviewing.
6. Only touch the strings in scope for the current task. If nearby existing strings are weak, mention them briefly and offer a review; don't rewrite them unasked.

**Mode B — review on request.** Input: pasted text, a screenshot, a URL, or "review the strings in this file/folder".
1. Extract the strings (from the image, page, or files).
2. For each weak string: show `Trước → Sau` plus a one-line reason (in Vietnamese).
3. Flag inconsistencies across strings (pronouns, terms).
4. In a repo, offer to apply the changes to the source files.

### Core rules (content of `SKILL.md`)

- The four quality standards from the original, explained briefly in Vietnamese terms.
- Short pattern table, one line per element, e.g.:
  - Button: `[Động từ] [đối tượng]` → "Lưu thay đổi", "Xóa tài khoản"; avoid "OK", "Đồng ý" when a specific verb fits.
  - Error: `[Điều gì không thành công]. [Vì sao]. [Cần làm gì].` → "Chưa lưu được thay đổi. Mất kết nối mạng. Kiểm tra mạng rồi thử lại."
  - Empty state, success, confirmation dialog, permission request, notification, form label/hint, onboarding.
- Top "sounds translated" traps to avoid, with natural alternatives.
- Pointers to each reference file and when to load it.

## Decided by the author (this conversation)

- Vietnamese only, for solo devs with no UX writing experience; author first, then public.
- Free/open sources only.
- In-repo usage is primary; review of text/screenshot/URL also supported.
- Approach 2: new Vietnamese-first skill, crediting the original.
- In multi-language repos, the skill writes Vietnamese values fresh from the English intent (not literal translation).

## Calls made by Claude (open to correction)

- Default address *bạn*; app avoids self-reference.
- The skill decides defaults and announces them instead of asking.
- Voice file at `docs/ux-voice.md`.
- Explanations and README in Vietnamese; `SKILL.md` instructions may be in English or Vietnamese — builder's choice based on what makes Claude follow it most reliably, with all examples in Vietnamese.
- Domain-based default register (formal for banking/government/health, friendly for consumer apps).
- Tone-mark placement (*xoá* vs *xóa*): follow the repo's existing style; otherwise default to the newer style (*xóa*, *hòa*) that most current apps use.
- Mode A touches only in-scope strings; it mentions other weak strings without rewriting them.
- This spec replaces the plan in `vietnamese-ux-writing-sources.md` where they differ: no paywalled books, no screenshots of real apps as source material. Every example is written fresh.

## Left to the builder

- Exact wording and length of each reference file.
- How the skill is tested: build a set of 15–25 real-looking weak Vietnamese strings across element types, compare output with and without the skill, and have the author judge. Include a repo scenario (e.g. a small React app with i18n JSON) to test Mode A and voice-file creation.
- Packaging (zip/build script) for sharing, following the agent skills spec.
- Which repo file types to recognise in Mode A beyond the common ones listed.
