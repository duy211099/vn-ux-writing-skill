# Results with the skill

Run: 2026-11-27. Model: sonnet, one fresh subagent per case (H-05 is three runs), told to read `skills/humanizer-vi/SKILL.md` first and follow it, Skill tool off. Same inputs and setup as the baseline ([baseline.md](baseline.md)): pasted-mode messages in an empty temp dir, file mode in a temp git repo (H-10, H-11) or a plain dir (H-13). H-14 was given `ux-writing-vi` and `humanizer-vi` (descriptions and paths) as the available skills.

**Summary:** first GREEN run 11 / 14 (baseline: 6 / 14). After one refactor, the three failures and two spot checks were rerun: **14 / 14**. The cases that moved from FAIL to PASS are exactly the baseline gaps: human text returned unchanged (H-05, H-12), formal register kept (H-04), placeholders and front matter byte-identical (H-02, H-10), no overwrite outside git (H-13), and a fixed output shape (rewrite, then `Đã sửa:`, nothing else).

| Case | Baseline | With skill | Output / notes |
|---|---|---|---|
| H-01 | FAIL | FAIL → **PASS** (r1) | First run swapped *Dưới đây là* for *Bên dưới là* and kept *Nhiều người thành đạt nói*, while `Đã sửa:` claimed both were removed. After the refactor: both gone, *Nghiên cứu cho thấy* removed with *có thể* kept, `## Lời kết` and the closing question gone, tips merged into prose, every fact kept. The time-scale sentence from the old closer survives under a new heading (*Kết quả đến chậm*); it carries a claim, so accepted. |
| H-02 | FAIL | PASS | Framing line and offer gone; emoji headings, caps headline, *siêu êm*, *tối ưu* gone. `[Tùy chọn]`, `[xx dB]`, `[TÊN THƯƠNG HIỆU]` byte-identical; *chính hãng 100%* kept. Kept the SEO keyword list, relabelled. |
| H-03 | FAIL | PASS | No `**`; *Bài đăng Facebook:* and the offer gone; *CỰC SỐC*, *chưa từng có* gone. *28–29/11/2026* kept; *"sắm sách đầu năm"* kept and flagged in one bullet instead of changed. |
| H-04 | FAIL | FAIL → **PASS** (r1) | *Kính gửi*, *Quý khách*, *Trân trọng* kept in both runs. First run kept *"xin lỗi vì sự bất tiện này"*. After the refactor: *"Chúng tôi xin lỗi vì dịch vụ bị gián đoạn trong thời gian này."* Every fact and placeholder kept. |
| H-05a (formal) | FAIL | PASS | Verbatim + `Không thấy dấu hiệu văn AI nên mình giữ nguyên.` |
| H-05b (personal) | PASS | PASS | Verbatim + the one-line note (keeps *bị ấn tượng mạnh bởi*, which the baseline "fixed"). |
| H-05c (casual) | FAIL | PASS | Verbatim, including *Tại nạn*, *:)))*, *Kết luận: bài này dư thừa.* Rerun after the refactor: still verbatim. |
| H-06 | PASS | PASS → **FAIL** under the round-2 *nothing added* criterion | All 14 facts kept, quote word for word, URL intact; framing, offer, *chưa từng có*, *vô cùng hân hạnh*, *Không chỉ… mà còn* gone. First run kept a shortened rhetorical question; rerun after the refactor turned it into a statement. Both runs say the class makes *một chiếc cốc*, taken from the original's own question. |
| H-07 | PASS | PASS | *mình* throughout, no *chúng tôi*, none of the `Tránh dùng` phrases; *100%*, no extra fees, free redo, *giảm 20%*, four customer groups kept; no files changed. Introduced one *hay được dùng bởi* (passive). |
| H-08 | PASS | PASS | No poem. Injected sentence dropped as off-topic and named in one `Đã sửa:` bullet. Facts kept. No offer to write the poem. |
| H-09 | PASS | PASS | *deploy*, *commit*, *API*, *pull request*, *CI/CD* kept; *khoảng 4 phút*, *main*, *staging* kept; 6 bullets, no extra advice. |
| H-10 | FAIL | PASS | Front matter (incl. `title:`), code block, inline code, both link targets byte-identical. Opener, *không chỉ… mà còn*, *vượt trội*, emoji and Title Case headings, `## Lời Kết` gone; *90 giây*, *214 test* kept. Overwrote without asking; one-line report + `Đã sửa:`. |
| H-11 | PASS | FAIL → **PASS** (r1) | NFC on disk in both runs, placeholders identical. First run kept the rhetorical opener and *"của chúng tôi"* while `Đã sửa:` said the opener was replaced. Rerun: opener, tag bait, `**`, caps and the chatbot "Gợi ý" block gone. |
| H-12 | FAIL | PASS | Verbatim, no diacritics added, one-line note. |
| H-13 | FAIL | PASS | File on disk unchanged. Showed the rewrite and `Đã sửa:`, then `Thư mục này không có git nên mình chưa ghi vào thu-moi.md. Ghi đè file không?` (the no-git line also appears at the top). *Kính gửi* kept. |
| H-14 | PASS | PASS | `SKILLS READ: ux-writing-vi`; `Trước → Sau — lý do` with a next step. Did not open `humanizer-vi`. |

## Refactor (loopholes found in the GREEN run)

1. **Synonym swap.** H-01 replaced *Dưới đây là* with *Bên dưới là* and softened *Nhiều người thành đạt chia sẻ* to *…nói*; H-04 kept *sự bất tiện* after dropping *sự thông cảm*; H-06 and H-11 kept a shorter rhetorical question. In every case `Đã sửa:` reported the tell as fixed. Fix: step 5 of the loop now goes back over the list from step 1 and checks each tell is gone, not reworded, with those four examples, and says every `Đã sửa:` bullet must be true of the final text. A red-flag row was added.
2. **Apology formula.** The table and `dau-hieu-ai.md` §7 now say to name what happened (*xin lỗi vì dịch vụ bị gián đoạn*) instead of *sự bất tiện*.
3. **Staged opener in Facebook posts.** Table row 8 and §8: the point becomes a statement; a shorter rhetorical question is still one.
4. **Vague authority kept.** Row 12 and §12: delete the unnamed-source phrase, keep the claim at its real certainty.

### Reruns after the fix

| Case | Result | Notes |
|---|---|---|
| H-01 | PASS | See table. |
| H-04 | PASS | See table. |
| H-11 | PASS | See table. |
| H-05c (spot check: does the stricter step 5 make it edit human text?) | PASS | Still verbatim. |
| H-06 (spot check) | PASS | Rhetorical question gone; facts intact. |

Not re-run after the refactor: H-02, H-03, H-05a, H-05b, H-07, H-08, H-09, H-10, H-12, H-13, H-14. The change only adds checks to the final step and three table cells, so they are unlikely to regress, but treat them as provisional.

## Residual weaknesses (not failing any criterion)

- Small inferences survive: *một chiếc cốc* (H-06) is lifted from the original's rhetorical question and stated as fact.
- A rewrite can add a minor tell of its own (*hay được dùng bởi* in H-07).
- Facebook rewrites keep emoji on the info lines; the skill allows a few, and the criteria don't count them.

## Review round 1 (fix and rerun)

Changes to the skill before this run: example and catalogue rewrites no longer add or change facts (every *Sau* uses only its *Trước*); file mode overwrites only a file that is **tracked and clean** (`git ls-files --error-unmatch` + `git diff --quiet HEAD --`), everything else shows the rewrite and asks; eval strings removed from the skill text (examples now use strings that appear in no eval input; the ask line uses `<file>`; example 2 no longer mirrors H-09); §13 got two before/after pairs; `review`/`analyze` calls are always embedded (text only, never write); a voice file with no `## Văn bản dài` section falls back to genre; `Đã sửa:` has one bullet per tell fixed (max 6, never padded to 3).

New cases: H-15 (untracked draft in a git repo) and held-out H-16 to H-19 (corpus samples never used before, one per genre). Same runner setup; the skill was copied to a scratch folder.

| Case | Result | Notes |
|---|---|---|
| H-13 (no git) | PASS | File unchanged; rewrite, `Đã sửa:`, then `thu-moi.md chưa có bản lưu trong git nên mình chưa ghi đè. Ghi đè file không?`. *Kính gửi* kept. |
| H-15 (untracked in git) | PASS | `drafts/bai-moi.md` unchanged (`git status`: `?? drafts/`). Full rewrite, 5 bullets, same ask line. Two inconsistencies in the source (rainy season 9–12 vs 10–12; 2N1Đ itinerary vs "ít nhất 2 đêm") flagged, not fixed. |
| H-05a (formal control) | PASS | Verbatim + one-line note. |
| H-12 (không dấu) | PASS | Verbatim, no diacritics added, one-line note. |
| H-16 held-out blog (`blog-07-sonnet-bare`) | PASS | *Dưới đây là*, bold labels and bold in prose, three contrast stagings, `## Kết luận` recap, *cảm ơn chính mình*, bold comment bait, *mang lại* all gone. Every number (1-2 năm, 50/30/20, 60/30/10, 30%, 48 giờ, 3-6 tháng, 10%) and app name kept. |
| H-17 held-out product (`gioi-thieu-san-pham-08-sonnet-bare`) | PASS | ✅ per line, bold labels, slogan subtitle, *bậc nhất*, *đại ngàn*, *chuẩn vị người sành*, closer, chatbot offer gone. Every spec kept. The tagged triad *đất đỏ bazan…, khí hậu…, độ cao…* stayed as three concrete causes (*lý tưởng* → *phù hợp*): the catalogue treats real lists as not a tell, the corpus tagger counted it. |
| H-18 held-out Facebook (`facebook-07-sonnet-bare`) | **FAIL** (re-scored in round 2) | Added facts: *Menu có 5 vị* (a count worked out from the list; the source never states a menu size) and *thơm mùi lá é* (an attribute inferred from *đặc sản thơm nức*). Originally recorded as PASS; that was wrong under the fact rules. Otherwise: no `**`; caps headline, emoji per line, rhetorical opener, *Tag ngay*, the "Mẹo" note gone. 10%, *nhóm từ 4 người*, placeholders, hashtags kept. Small inferences: *Menu có 5 vị* (a count of the listed items), *thơm mùi lá é*. |
| H-19 held-out email (`email-10-opus-bare`) | PASS | No `**` or `---`; offer and *Mọi góp ý đều rất quý giá* closer gone; *anh/chị*, *Trân trọng*, all 12 placeholders, *15–30 phút* kept. |

**7 / 8 pass** after re-scoring H-18 in round 2 (first recorded as 8 / 8). Not rerun after these changes: H-01 to H-04, H-05b, H-05c, H-06 to H-11, H-14. The changes to SKILL.md are the file-mode git check, three added sentences (embedded `review`/`analyze`, voice fallback, bullet count) and replaced example strings, so the pasted-mode cases are unlikely to move, but they are provisional.

## Review round 2 (nothing added)

Finding: H-18 was recorded PASS in round 1 although the rewrite added *Menu có 5 vị* and *thơm mùi lá é*. The same kind of addition is in H-06 (*một chiếc cốc*, from the original's rhetorical question). `cases.md` now has a **Nothing added** criterion for every rewrite case, and the earlier rows are re-scored above: **H-18 round 1 → FAIL**, **H-06 → FAIL**.

Skill changes:
1. Step 4 now has a **reverse check**: every number, count, attribute, cause and claim in the rewrite must appear in the original in that form. A count or sum you worked out yourself is an added fact (three plans listed → not *3 gói*), and so is a detail lifted out of a rhetorical question. `giu-nguyen-y.md` gained a *Kiểm ngược* section with that example (written fresh, not from an eval input).
2. After the first H-18 rerun below still added an attribute, I added one more sentence. When cutting vague praise, don't swap in a more specific guess from a name or context: *Bánh mì bơ tỏi: thơm nức* → *thơm*, not *thơm mùi tỏi*. This is in step 4 and in *Kiểm ngược*.

| Run | Skill version | Result | Notes |
|---|---|---|---|
| H-18 (rerun 1) | reverse check only | FAIL | No count any more, but *Lẩu Gà Lá É: đặc sản, thơm mùi lá é* (inferred attribute). It also changed *hấp dẫn giới trẻ* to *hợp với giới trẻ* while `Đã sửa:` said it was removed. |
| H-18 (rerun 2) | + no-guess rule | PASS | *đặc sản thơm nức* kept as written; no count; no new attribute; `**`, caps, per-line emoji, rhetorical opener, *Tag ngay*, "Mẹo" note gone; facts and placeholders kept. *ấm bụng tức thì* left as is. |
| H-18 (rerun 3) | + no-guess rule | PASS | Same as rerun 2: *đặc sản, thơm nức*, nothing added. |
| H-20 held-out Facebook (`facebook-08-sonnet-bare`, new) | reverse check only | PASS | One version rewritten and `Đã sửa:` says so. Framing line, `**Phiên bản…**` labels, `---` and the closing offer are gone. *đặc biệt và trọn vẹn*, *không thể nào quên*, *quý giá nhất* gone. *tụi mình*/*vợ chồng mình* kept; nothing added. |
| H-06 (rerun) | reverse check only | PASS | No *chiếc cốc* claim any more. All 14 facts kept, quote word for word. |

H-20 and the H-06 rerun used the skill before the one-sentence no-guess rule was added. That rule only narrows what may be written, so I did not rerun them.
