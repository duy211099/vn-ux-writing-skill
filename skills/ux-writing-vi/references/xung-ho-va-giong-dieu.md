# Xưng hô và giọng điệu

Tiếng Anh chỉ có "you". Tiếng Việt buộc phải chọn cách gọi người dùng, cách ứng dụng tự xưng, và mức trang trọng. Chọn sai một lần thì cả ứng dụng nghe lạc giọng, nên quyết định này được ghi vào file giọng văn (`docs/ux-voice.md`) và dùng lại mọi nơi.

Người dùng skill thường không có kinh nghiệm viết UX. **Đừng hỏi họ chọn gì.** Hãy chọn theo mặc định bên dưới, báo lại một dòng, và để họ sửa nếu muốn.

## Mặc định

| Quyết định | Mặc định | Ghi chú |
|---|---|---|
| Gọi người dùng | *bạn*, hoặc bỏ đại từ | Bỏ đại từ thường gọn hơn: "Chưa có đơn hàng nào" thay vì "Bạn chưa có đơn hàng nào". |
| Ứng dụng tự xưng | Không tự xưng | Viết câu không cần chủ ngữ, hoặc dùng tên ứng dụng. *Chúng tôi* chỉ dùng cho tài chính, pháp lý, chính sách. Không dùng *mình*, *tớ*, *em* trừ khi thương hiệu chủ động chọn. |
| Mức trang trọng | Trung tính, thân thiện | Như một nhân viên lịch sự nói chuyện với khách trẻ: rõ ràng, không suồng sã, không hành chính. |
| Trợ từ | Xem phần Trợ từ | *nhé* dùng thưa; không *nha*, *ạ* trong giao diện. |

✅ Chưa tải được video. Video dài hơn 3 phút. Cắt ngắn rồi tải lại.
❌ Chúng tôi rất tiếc! Hệ thống của chúng tôi không thể tải video của bạn.

✅ Đã gửi mã đến 0912 345 678.
❌ Mình đã gửi mã cho bạn rồi nha!

✅ Chào mừng đến với Phòng Khám An Tâm
❌ Chào mừng bạn đến với dịch vụ của chúng tôi!

## Chọn theo lĩnh vực

Khi tạo file giọng văn lần đầu, đoán lĩnh vực từ tên dự án, `package.json`, README, màn hình hiện có, rồi chọn:

| Lĩnh vực | Gọi người dùng | Giọng | Trợ từ |
|---|---|---|---|
| Ngân hàng, ví điện tử, bảo hiểm, chứng khoán | *quý khách* hoặc bỏ đại từ | Trang trọng, chính xác | Không *nhé*; *vui lòng* được dùng khi yêu cầu |
| Y tế, dịch vụ công, pháp lý | Bỏ đại từ, hoặc *quý khách* / *bạn* tùy đối tượng | Trang trọng, điềm tĩnh | Không *nhé* |
| Thương mại điện tử, giao đồ ăn, gọi xe, du lịch | *bạn* | Thân thiện, gọn | *nhé* thưa thớt |
| Mạng xã hội, giải trí, học tập cho người trẻ | *bạn* | Thân thiện, có thể vui | *nhé* được dùng |
| Công cụ làm việc, B2B, dành cho lập trình viên | Bỏ đại từ, hoặc *bạn* | Trung tính, ngắn | Hầu như không dùng |

Không chắc lĩnh vực nào: dùng mặc định (*bạn*, trung tính thân thiện).

✅ (ngân hàng) Số dư không đủ để thanh toán. Nạp thêm tiền hoặc chọn tài khoản khác.
❌ (ngân hàng) Hết tiền rồi, bạn nạp thêm nhé!

✅ (giao đồ ăn) Món đang được chuẩn bị, khoảng 20 phút nữa sẽ giao đến bạn.
❌ (giao đồ ăn) Quý khách vui lòng chờ trong giây lát.

## Trợ từ

| Từ | Dùng khi | Tránh |
|---|---|---|
| *nhé* | Lời mời, lời nhắc nhẹ trong ứng dụng thân thiện: "Xem lại địa chỉ trước khi đặt nhé." Tối đa khoảng một lần mỗi màn hình. | Thông báo lỗi nghiêm trọng, tiền bạc, bảo mật; ứng dụng trang trọng. |
| *nha*, *nè* | Hầu như không. Chỉ khi thương hiệu chủ động chọn giọng rất suồng sã. | Mọi chỗ khác. |
| *ạ* | Tin nhắn hỗ trợ khách hàng do người viết, không phải giao diện. | Nút, nhãn, lỗi, thông báo. |
| *vui lòng* | Ứng dụng trang trọng; hoặc khi xin lỗi và đề nghị người dùng làm việc phiền: "Vui lòng xác minh lại danh tính để tiếp tục." | Lặp lại nhiều lần; đặt trước mọi hướng dẫn. Trong giọng thân thiện, viết thẳng động từ: "Nhập email". |
| *hãy* | Khuyến khích một hành động có lợi: "Hãy bật thông báo để biết khi món đến." | Dùng như lệnh: "Hãy nhập mật khẩu." → "Nhập mật khẩu". |
| *xin* | Xin lỗi thật sự khi lỗi do phía ứng dụng: "Xin lỗi, hệ thống đang bảo trì." | "Xin chờ", "Xin mời" trong giao diện thường ngày. |

✅ Nhập email để nhận hóa đơn.
❌ Vui lòng nhập email. Vui lòng kiểm tra lại email của bạn.

✅ Đặt xong rồi! Theo dõi đơn ở mục Đơn hàng nhé.
❌ Đặt hàng thành công nha bạn ơi!

## Khi repo đã có cách xưng hô

Trước khi áp mặc định, đọc các chuỗi tiếng Việt đã có (file `vi.json`, `*_vi.arb`, `vi.lproj`, chữ viết thẳng trong component).

- Nếu đa số chuỗi đã dùng một cách gọi (*quý khách*, *anh/chị*, *bạn*), **theo cách đó**, kể cả khi khác mặc định. Ghi vào file giọng văn.
- Nếu đang trộn nhiều cách gọi, chọn cách chiếm đa số, ghi vào file giọng văn, và báo người dùng một dòng về các chuỗi lệch.
- Cách viết dấu thanh (*xóa* hay *xoá*) cũng theo repo. Xem [định dạng](dinh-dang.md#unicode-và-dấu-thanh).

✅ (repo dùng *quý khách*) Quý khách cần xác thực khuôn mặt để chuyển khoản trên 10 triệu đồng.
❌ (repo dùng *quý khách*) Bạn cần quét mặt để chuyển khoản trên 10 triệu nhé.

✅ (repo dùng *anh/chị*) Anh/chị cần xác thực khuôn mặt để chuyển khoản trên 10 triệu đồng.
❌ (repo dùng *anh/chị*) Bạn cần xác thực khuôn mặt… (đổi cách gọi giữa chừng)
