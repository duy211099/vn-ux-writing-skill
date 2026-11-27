# Tiếp cận

Viết sao cho người dùng trình đọc màn hình, người lớn tuổi, người đang vội hoặc căng thẳng vẫn hiểu và dùng được. Phần lớn quy tắc ở đây cũng làm chữ tốt hơn cho mọi người. Diễn đạt lại và điều chỉnh từ phần hướng dẫn tiếp cận của bộ UX Writing Skill gốc (MIT, Christopher Greer); ví dụ viết mới cho tiếng Việt.

## Văn bản thay thế (alt text)

- Ảnh mang thông tin: mô tả điều người dùng cần biết, không mô tả kỹ thuật. Không mở đầu bằng "Hình ảnh của…".
- Ảnh trang trí: để `alt=""` để trình đọc màn hình bỏ qua.
- Nút chỉ có biểu tượng: luôn có nhãn đọc được (`aria-label`, `contentDescription`, `accessibilityLabel`).

| ✅ | ❌ |
|---|---|
| `alt="Phở bò tái, tô lớn"` | `alt="Hình ảnh của món ăn"` |
| Nút ♡: `aria-label="Lưu vào yêu thích"` | Nút ♡ không có nhãn, đọc lên là "nút" |

## Chữ liên kết

Chữ của liên kết phải tự nói nó dẫn đi đâu, vì người dùng trình đọc màn hình thường nghe danh sách liên kết tách khỏi câu.

| ✅ | ❌ |
|---|---|
| Xem chính sách bảo mật | Xem thêm tại đây |
| Tải hóa đơn tháng 11 (PDF, 200 KB) | Tải về |

## Trình đọc màn hình

- Trình đọc màn hình đọc từng chữ. Viết tắt như "SĐT", "TK", "MK", "ĐH" sẽ bị đọc thành từng chữ cái. Viết đầy đủ trong nhãn và thông báo.
- Khai báo ngôn ngữ để máy đọc đúng giọng tiếng Việt: `<html lang="vi">`; đoạn tiếng Anh xen giữa thì `lang="en"`.
- Thông báo lỗi và trạng thái hiện ra sau khi thao tác cần được đọc lên (`role="alert"` hoặc `aria-live` trên web; tương đương trên di động).
- Ký hiệu trang trí (•, →, ★★★★☆) nên có chữ đi kèm: "4 trên 5 sao".
- Số tiền và ngày giờ viết theo [định dạng](dinh-dang.md) để máy đọc tự nhiên.

| ✅ | ❌ |
|---|---|
| Số điện thoại | SĐT |
| Đánh giá 4 trên 5 sao | ★★★★☆ |

## Không chỉ dựa vào màu

Lỗi, trạng thái, mục bắt buộc phải nói bằng chữ, không chỉ tô đỏ hay xanh.

| ✅ | ❌ |
|---|---|
| Ô viền đỏ + chữ "Mật khẩu cần ít nhất 8 ký tự" | Chỉ tô đỏ viền ô |
| Nhãn "Email (bắt buộc)" | Nhãn "Email" màu đỏ, không giải thích |

## Lỗi gắn với ô nhập

- Lỗi hiện ngay dưới ô bị sai, và được liên kết với ô đó (`aria-describedby`) để trình đọc màn hình đọc cùng.
- Form dài: ngoài lỗi từng ô, có một dòng tóm tắt ở đầu ("Còn 2 ô cần sửa") và đưa con trỏ đến ô sai đầu tiên.
- Không xóa những gì người dùng đã nhập khi báo lỗi.

## Từ ngữ dễ hiểu

- Dùng từ thông dụng thay cho Hán Việt hoặc thuật ngữ khi có từ phổ biến: "xem" thay "truy xuất", "đổi" thay "thay đổi cấu hình", "gửi" thay "đệ trình".
- Mỗi câu một ý; câu ngắn (thường dưới 20 chữ trong giao diện).
- Đưa thông tin quan trọng nhất lên đầu câu.
- Bối cảnh căng thẳng (tiền, sức khỏe, bảo mật, hết thời gian): bình tĩnh, cụ thể, nói ngay người dùng còn bao nhiêu thời gian và tiền/dữ liệu có an toàn không.

| ✅ | ❌ |
|---|---|
| Xem lịch sử giao dịch | Truy xuất lịch sử giao dịch |
| Tiền chưa bị trừ. Bạn còn 4 phút để hoàn tất thanh toán. | Phiên thanh toán sắp hết hiệu lực! |
