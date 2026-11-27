# Định dạng

Quy tắc trình bày chữ, số, ngày giờ và tiền trong giao diện tiếng Việt. Các quy tắc ngôn ngữ được diễn đạt lại từ *Microsoft Vietnamese Localization Style Guide* và điều chỉnh cho ứng dụng tiêu dùng.

## Ngày giờ

- Ngày: `dd/mm/yyyy`, có số 0 ở đầu khi cần để cột thẳng hàng: `05/03/2026`.
- Ngày dạng chữ: "27 tháng 11, 2026" hoặc "Thứ Sáu, 27/11/2026". Tên tháng viết thường ("tháng 11"), tên thứ viết hoa ("Thứ Sáu").
- Giờ: 24 giờ, dấu hai chấm: `14:30`. Không dùng AM/PM.
- Thời gian tương đối khi gần: "Vừa xong", "5 phút trước", "Hôm qua, 20:15".
- Khoảng thời gian: "2–3 ngày" (gạch nối ngắn, không cách) hoặc "từ 2 đến 3 ngày". Không viết tắt "mins", "p", "h".

| ✅ | ❌ |
|---|---|
| Giao lúc 14:30, 05/03/2026 | Giao lúc 2:30 PM, 3/5/2026 |
| Giao trong 2–3 ngày | Ship 2-3 days |

## Số và tiền tệ

- Dấu chấm phân cách hàng nghìn, dấu phẩy cho phần thập phân: `1.526`, `5,25 cm`, `4,5 sao`.
- Số đếm viết bằng chữ số ("2 món", "3 ngày"); số thứ tự thường viết bằng chữ ("lần đầu tiên", "bước thứ hai").
- Tiền đồng — mặc định cho ứng dụng tiêu dùng: `100.000đ` (không cách, chữ đ thường). Ứng dụng ngân hàng, hóa đơn, hoặc khi có nhiều loại tiền: `100.000 VND`. Chọn một kiểu và dùng thống nhất.
- Tiền nước ngoài: giữ ký hiệu gốc, đổi dấu phân cách: `$1.526,75`.
- Số lớn trong câu thân thiện có thể viết gọn: "1,2 triệu lượt tải". Trong số tiền cần chính xác thì viết đủ.

| ✅ | ❌ |
|---|---|
| Tổng cộng: 245.000đ | Tổng cộng: 245,000 VNĐ |
| Đánh giá 4,8 | Đánh giá 4.8 |
| Hạn mức còn lại: 15.000.000 VND | Hạn mức còn lại: 15tr |

## Dấu câu và viết hoa

- **Chỉ viết hoa chữ đầu câu** và danh từ riêng. Tiêu đề, nút, mục menu cũng vậy. Không viết hoa từng chữ kiểu tiếng Anh.
- Tên riêng viết hoa mỗi chữ: "Việt Nam", "Hà Nội". Tên tính năng mang thương hiệu giữ nguyên cách viết của thương hiệu.
- Không có dấu cách trước `. , : ; ? !`; có một dấu cách sau.
- Không dùng dấu phẩy trước "và", "hoặc".
- Tiêu đề, nhãn, nút: không chấm câu ở cuối. Thông báo nhiều câu: chấm câu bình thường.
- Hạn chế dấu chấm than. Một lỗi không cần "!", một lời chào có thể có.
- Danh sách sau dấu hai chấm nằm trong câu thì viết thường; mỗi mục xuống dòng thì viết hoa chữ đầu.
- Dùng ngoặc kép cong “…” hoặc thẳng "…", nhưng thống nhất trong cả ứng dụng.

| ✅ | ❌ |
|---|---|
| Đăng nhập vào tài khoản | Đăng Nhập Vào Tài Khoản |
| Lưu thay đổi | Lưu Thay Đổi. |
| Số điện thoại chưa đúng. Kiểm tra lại rồi thử lần nữa. | Lỗi : Số điện thoại không hợp lệ ! |

## Unicode và dấu thanh

- Luôn lưu và xuất chữ ở dạng **Unicode NFC** (dựng sẵn). Văn bản dán từ macOS hoặc một số bộ gõ có thể ở dạng NFD (tổ hợp), trông giống nhau nhưng làm hỏng tìm kiếm, so sánh chuỗi và đôi khi hiển thị sai. Khi viết code xử lý chuỗi người dùng nhập, chuẩn hóa về NFC (`str.normalize("NFC")` trong JavaScript, `unicodedata.normalize("NFC", s)` trong Python).
- Vị trí dấu thanh có hai kiểu: kiểu truyền thống (*xóa, hòa, thủy*) và kiểu mới (*xoá, hoà, thuỷ*). Cả hai đều đúng.
  - Nếu repo đã dùng một kiểu, **theo kiểu của repo**.
  - Nếu chưa có, dùng kiểu truyền thống (*xóa, hòa*) vì phổ biến nhất trong ứng dụng hiện nay.
  - Không trộn hai kiểu trong cùng một ứng dụng. Kiểu áp dụng cho mọi từ có *oa, oe, uy*, không chỉ từ đã thấy: repo dùng *xoá* thì cũng viết *huỷ, hoà, khoẻ, thuỷ*; repo dùng *xóa* thì viết *hủy, hòa, khỏe, thủy*.
- Không bỏ dấu tiếng Việt trong giao diện, kể cả trong nút ngắn hay thông báo đẩy.

| ✅ | ❌ |
|---|---|
| Xóa ảnh (repo dùng *xóa*) | Xoá ảnh ở màn này, Xóa thẻ ở màn kia |
| Đặt hàng thành công | Dat hang thanh cong |
