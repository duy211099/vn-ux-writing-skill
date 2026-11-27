---
title: "CI Cho Dự Án Nhỏ: Hướng Dẫn Toàn Diện Từ A Đến Z"
date: 2026-11-20
tags: [ci, github-actions]
draft: false
---

Bạn có bao giờ tự hỏi làm sao để dự án nhỏ của mình cũng có quy trình kiểm thử chuyên nghiệp như các công ty lớn? Hãy cùng tìm hiểu nhé!

## 🚀 Vì Sao Cần CI?

CI không chỉ là một công cụ, mà còn là người bạn đồng hành đáng tin cậy. Nó giúp phát hiện lỗi sớm, tiết kiệm thời gian và nâng cao chất lượng code một cách vượt trội. Với dự án của mình, mỗi lần push mất khoảng 90 giây để chạy hết 214 test.

## ⚙️ Cấu Hình Đầu Tiên

Tạo file `.github/workflows/test.yml` với nội dung sau:

```yaml
name: test
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci && npm test
```

**Lưu ý:** Bước `npm ci` sẽ cài đúng phiên bản ghi trong `package-lock.json`, giúp kết quả ổn định và nhất quán.

Xem thêm [tài liệu chính thức của GitHub Actions](https://docs.github.com/en/actions) và [bài trước về npm scripts](../npm-scripts/).

## Lời Kết

Tóm lại, CI là khoản đầu tư nhỏ nhưng mang lại giá trị vô cùng to lớn. Hãy bắt đầu ngay hôm nay!
