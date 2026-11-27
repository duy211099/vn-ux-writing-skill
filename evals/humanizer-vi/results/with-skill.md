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
| H-06 | PASS | PASS | All 14 facts kept, quote word for word, URL intact; framing, offer, *chưa từng có*, *vô cùng hân hạnh*, *Không chỉ… mà còn* gone. First run kept a shortened rhetorical question; rerun after the refactor turned it into a statement. Both runs say the class makes *một chiếc cốc*, taken from the original's own question. |
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
