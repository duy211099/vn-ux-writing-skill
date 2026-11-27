# Results with the skill

Run: 2026-11-27. Model: sonnet, one fresh subagent per case, told to read `skills/style-vi/SKILL.md` first and follow it. Each case ran in a fresh git copy of `evals/ux-writing-vi/fixture-repo/` with the case's seed committed; the verdict is from the diff plus the final reply. Baseline: [baseline.md](baseline.md).

**Summary:** 4 / 4 cases pass on the final run (baseline: 0 / 4).

## Final run (after refactor)

| Case | Result | Output / notes |
|---|---|---|
| S-01 | PASS | Only `docs/giong-van.md` created: the template with every field filled. Lĩnh vực giao đồ ăn; *bạn*; *xóa* (from `vi.json`); prose: xưng "Bếp Nhà", xen kẽ, trò chuyện, seed `Tránh dùng` list; `Đoạn văn mẫu` left as a placeholder. Reply, one line: "Đã tạo docs/giong-van.md: gọi người dùng là "bạn", bài viết dài xưng "Bếp Nhà", câu xen kẽ, giọng trò chuyện (ứng dụng giao đồ ăn). Sửa file này nếu muốn đổi." No questions. |
| S-02 | PASS | Appended `## Văn bản dài` (Bếp Nhà, xen kẽ, trò chuyện, seed list) to `docs/ux-voice.md`; 18 lines added, none removed. No `docs/giong-van.md`, nothing moved. One-line reply. |
| S-03 | PASS | `docs/giong-van.md`: *quý khách*, "Trang trọng", *nhé* không dùng, *vui lòng* allowed. Listed `cart.empty`, `cart.remove`, `order.placed` with their text, plus `package.json` `description` ("…gần bạn", extra but harmless). `vi.json` unchanged; ended "Sửa các chuỗi này theo giọng mới không?" |
| S-04 | PASS | Four lines: "Theo docs/giong-van.md (giao đồ ăn, Bếp Nhà):" + UI line + prose line + "Sửa file đó để đổi." No files changed. |

## First run and refactor

The first GREEN run also passed 4 / 4, but two problems were visible:

1. **Examples taught the test.** The SKILL.md examples used the fixture's own app (Bếp Nhà) and its `vi.json` keys, and S-04's reply echoed the example nearly word for word. Fix: examples now use a ride-hailing app (*Xe Nhanh*, `trip.cancel`, `wallet.empty`). The final run above uses the new examples; S-01 to S-04 still pass, so they are not just copying.
2. **The announcement grew a tail.** S-01's reply had the one line plus "Mình đoán … từ package.json", a suggestion to switch to *mình*, and a tip to paste a sample paragraph. Fix: Job 1 step 6 now says the line is the whole reply about the voice (no assumptions, tips or alternatives), with a matching Common-mistakes row. In the final run the S-01 reply is exactly one line.

| Case | First run | Notes |
|---|---|---|
| S-01 | PASS (borderline) | File correct; reply about four sentences (see 2). |
| S-02 | PASS | Same as final. |
| S-03 | PASS | Listed the three `vi.json` keys; file set to *quý khách*, trang trọng, no *nhé*. |
| S-04 | PASS | Four lines, echoing the example (see 1). |
