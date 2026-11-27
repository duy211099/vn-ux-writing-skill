# Mẫu nội dung theo thành phần

Mỗi thành phần giao diện có một việc riêng. Viết theo mẫu dưới đây, rồi chỉnh cho đúng giọng trong file giọng văn (`docs/ux-voice.md`). Các ví dụ dùng giọng mặc định (*bạn* hoặc bỏ đại từ, trung tính thân thiện).

Bốn tiêu chuẩn cho mọi chuỗi: **có mục đích** (giúp người dùng làm được việc), **ngắn gọn** (mỗi chữ có việc của nó), **tự nhiên** (như người nói, không như văn bản dịch), **rõ ràng** (một nghĩa, đúng sự thật).

## Tiêu đề

Cho người dùng biết họ đang ở đâu hoặc đang làm gì.

Mẫu: cụm danh từ, hoặc động từ + đối tượng nếu màn hình là một việc. Viết hoa chữ đầu, không chấm câu.

- ✅ Lịch sử đơn hàng
- ✅ Đổi mật khẩu
- ✅ Thêm thẻ ngân hàng
- ❌ Màn Hình Lịch Sử Các Đơn Hàng Của Bạn — viết hoa từng chữ, thừa chữ.
- ❌ Trang quản lý thông tin cá nhân người dùng — dài, từ của hệ thống. Dùng "Hồ sơ".

## Nút và liên kết

Cho người dùng làm một việc. Đọc nút là biết bấm vào sẽ xảy ra gì.

Mẫu: `[Động từ] [đối tượng]`. Hai đến bốn chữ. Nút trong hộp thoại lặp lại động từ của tiêu đề. Liên kết là chữ mô tả nơi đến, không phải "tại đây".

- ✅ Đặt món
- ✅ Thanh toán 245.000đ
- ✅ Xem chính sách đổi trả (liên kết)
- ❌ OK / Đồng ý / Xác nhận — không nói nút làm gì.
- ❌ Bấm vào đây — liên kết không nói dẫn đi đâu; trình đọc màn hình đọc lên vô nghĩa.

**Khi chỗ hẹp:** tiếng Việt thường dài hơn tiếng Anh. Bớt chữ, đừng viết tắt. "Lưu thay đổi" → "Lưu"; "Thêm vào giỏ hàng" → "Thêm vào giỏ". Không dùng "L.", "TK", "SĐT" trên nút.

## Lỗi

Nói việc gì không thành công, vì sao, và làm gì tiếp. Không đổ lỗi, không giật mình.

Mẫu chung: `[Điều gì không thành công]. [Vì sao]. [Cần làm gì].` Câu nào đã rõ từ ngữ cảnh thì bỏ.

Mở đầu bằng "Chưa… được", "Không… được" hoặc tên vấn đề cụ thể. Không mở đầu bằng "Lỗi:", "Đã xảy ra lỗi", "Có lỗi xảy ra". Nếu chuỗi gốc (kể cả tiếng Anh) không có bước tiếp theo, **thêm bước tiếp theo**.

### Lỗi nhập liệu

Hiện ngay dưới ô nhập, nói cách sửa.

- ✅ Email cần có ký tự @
- ✅ Mật khẩu cần ít nhất 8 ký tự
- ✅ Chọn ngày từ hôm nay trở đi
- ❌ Email không hợp lệ — không nói sai ở đâu.
- ❌ Trường này là bắt buộc! — "trường" là từ lập trình; nói tên ô: "Nhập số điện thoại".

### Lỗi hệ thống

Khi máy chủ hoặc mạng hỏng. Hiện trong hộp thoại hoặc thanh thông báo.

- ✅ Chưa lưu được thay đổi. Mất kết nối mạng. Kiểm tra mạng rồi thử lại.
- ✅ Thẻ bị từ chối. Thử thẻ khác hoặc chọn ví điện tử.
- ✅ Không gửi được mã. Đợi 60 giây rồi chọn "Gửi lại mã".
- ❌ Đã xảy ra lỗi (500). Vui lòng thử lại sau. — mã lỗi không giúp ai; "sau" là khi nào?
- ❌ Thanh toán thất bại! — trật tự tiếng Anh, không có bước tiếp theo.

### Lỗi chặn

Người dùng không thể tiếp tục cho đến khi xử lý xong. Toàn màn hình hoặc hộp thoại lớn.

- ✅ Cần cập nhật ứng dụng. Phiên bản này không còn được hỗ trợ. [Cập nhật]
- ✅ Tài khoản đang tạm khóa vì nhập sai mật khẩu 5 lần. Mở khóa sau 30 phút hoặc đặt lại mật khẩu.
- ✅ Gói Pro đã hết hạn. Gia hạn để tiếp tục xuất báo cáo. [Gia hạn]
- ❌ Bạn không có quyền truy cập. — không nói vì sao, không có lối ra.
- ❌ Phiên bản quá cũ!!! — giật mình, không có nút.

### Lỗi quyền truy cập

Người dùng đã từ chối một quyền mà tính năng cần.

- ✅ Cần quyền camera để quét mã QR. Mở Cài đặt để bật lại. [Mở Cài đặt]
- ✅ Chưa có quyền vị trí nên chưa tìm được quán gần bạn. [Bật vị trí] [Nhập địa chỉ]
- ✅ Không đọc được danh bạ. Bạn vẫn có thể nhập số điện thoại.
- ❌ Permission denied. — tiếng Anh, không có lối ra.
- ❌ Ứng dụng không thể hoạt động nếu không có quyền. — đe dọa, không cụ thể.

## Thông báo thành công

Xác nhận việc đã xong. Ngắn, cụ thể, đôi khi kèm bước tiếp theo.

Mẫu: `Đã [động từ] [đối tượng]` hoặc `[Đối tượng] đã [trạng thái]`. Không dùng bị động "đã được… thành công".

- ✅ Đã lưu thay đổi
- ✅ Đã gửi hóa đơn qua email
- ✅ Đặt xong rồi! Món sẽ đến trong khoảng 25 phút.
- ❌ Thành công! — thành công việc gì?
- ❌ Hồ sơ của bạn đã được cập nhật thành công. — bị động, thừa chữ.

## Hộp thoại xác nhận

Chỉ dùng trước hành động khó hoàn tác. Nếu có thể hoàn tác, bỏ hộp thoại và dùng thông báo kèm nút "Hoàn tác".

Mẫu: tiêu đề là câu hỏi ngắn nêu hành động (`[Động từ] [đối tượng]?`); một dòng nói hậu quả; nút chính lặp lại động từ, nút phụ là "Hủy".

- ✅ Hủy đơn hàng? / Món đã đặt sẽ không được giao. / [Hủy đơn] [Giữ đơn]
- ✅ Đăng xuất khỏi thiết bị này? / [Đăng xuất] [Hủy]
- ✅ Xóa thẻ •••• 4821? / Bạn có thể thêm lại thẻ bất cứ lúc nào. / [Xóa thẻ] [Hủy]
- ❌ Bạn có chắc chắn muốn hủy đơn hàng không? [Có] [Không] — dài; "Có/Không" phải đọc lại câu hỏi mới hiểu, mà "Hủy" lại trùng nghĩa.
- ❌ Cảnh báo! Hành động này không thể hoàn tác. [OK] — không nói hành động nào.

## Trạng thái trống

Màn hình chưa có nội dung. Nói điều gì sẽ xuất hiện ở đây và cho một bước để bắt đầu.

Mẫu: `[Chưa có gì]` + `[Điều gì sẽ hiện ở đây / lợi ích]` + `[Nút hành động]`. Nút dùng từ của lĩnh vực ("Xem thực đơn" cho đồ ăn, "Thêm giao dịch" cho chi tiêu), không dùng "Bắt đầu" chung chung nếu có động từ cụ thể.

- ✅ Chưa có địa chỉ nào / Lưu địa chỉ nhà, công ty để đặt nhanh hơn. / [Thêm địa chỉ]
- ✅ Không tìm thấy "phở cuốn" / Thử từ khóa ngắn hơn hoặc bỏ bớt bộ lọc. / [Xóa bộ lọc]
- ✅ Hộp thư trống / Tin nhắn từ người bán sẽ hiện ở đây.
- ❌ Không có dữ liệu — từ của hệ thống, không có bước tiếp theo.
- ❌ Danh sách hiện đang trống. — nói điều hiển nhiên.

Phân biệt ba trường hợp: lần đầu dùng (chưa có gì), tìm kiếm/lọc không có kết quả, và lỗi tải (dùng mẫu lỗi hệ thống, không dùng trạng thái trống).

## Xin quyền truy cập

Hiện trước hộp thoại quyền của hệ điều hành, đúng lúc người dùng cần tính năng. Lợi ích đi trước, yêu cầu đi sau.

Mẫu: `[Lợi ích cho người dùng]` + `[Nút: Bật/Cho phép + quyền]` + `[Nút phụ: Để sau]`.

- ✅ Quét mã QR để thanh toán nhanh. [Cho phép dùng camera] [Để sau]
- ✅ Tìm bạn bè đã dùng ứng dụng. [Kết nối danh bạ] [Bỏ qua]
- ✅ Nhận diện khuôn mặt để đăng nhập không cần mật khẩu. [Bật Face ID] [Để sau]
- ❌ Ứng dụng cần quyền truy cập camera. [OK] — không có lợi ích, không có lựa chọn.
- ❌ Vui lòng cho phép truy cập để sử dụng đầy đủ tính năng. — "đầy đủ tính năng" là gì?

## Thông báo đẩy

Hiện ngoài ứng dụng, đọc lướt trong 2 giây. Tiêu đề nói việc, nội dung nói chi tiết hoặc bước tiếp.

Mẫu: tiêu đề ≤ 40 ký tự, nội dung ≤ 90 ký tự. Thông tin quan trọng đặt đầu. Không viết hoa toàn bộ, không nhồi biểu tượng cảm xúc.

- ✅ Món sắp đến / Tài xế Minh còn khoảng 3 phút nữa.
- ✅ Còn 2 ngày để dùng voucher 50.000đ / Áp dụng cho đơn từ 150.000đ.
- ✅ (ngân hàng) Tiền vào: +1.200.000 VND / Từ NGUYEN VAN AN, nội dung: tiền nhà tháng 11.
- ❌ 🔥🔥 SIÊU SALE CỰC SỐC!!! Vào ngay kẻo lỡ — la hét, không nói gì cụ thể.
- ❌ Thông báo / Bạn có một thông báo mới. — người dùng phải mở mới biết.

## Nhãn và gợi ý trong form

Nhãn nói ô này là gì; gợi ý nói cách điền. Nhãn luôn hiển thị, không chỉ dùng placeholder.

Mẫu: nhãn là danh từ ngắn; placeholder là ví dụ; gợi ý (dưới ô) là yêu cầu định dạng.

- ✅ Nhãn "Số điện thoại", placeholder "0912 345 678"
- ✅ Nhãn "Mật khẩu", gợi ý "Ít nhất 8 ký tự, có cả chữ và số"
- ✅ Nhãn "Ghi chú cho tài xế (không bắt buộc)"
- ❌ Placeholder "Nhập số điện thoại của bạn vào đây" và không có nhãn — chữ biến mất khi gõ; thừa "nhập", "của bạn", "vào đây".
- ❌ Nhãn "SĐT*" — viết tắt, dấu sao không giải thích.

## Giới thiệu (onboarding)

Vài màn đầu tiên. Mỗi màn một lợi ích, nói việc người dùng làm được, rồi để họ bắt đầu ngay.

Mẫu: tiêu đề là lợi ích (≤ 6 chữ), một câu giải thích, nút đi tiếp là hành động thật ("Đặt món đầu tiên") hoặc "Tiếp", luôn có "Bỏ qua".

- ✅ Đặt lịch khám trong 1 phút / Chọn bác sĩ, chọn giờ, xong. / [Tiếp]
- ✅ Nhắc uống thuốc đúng giờ / Thêm đơn thuốc để được nhắc từng liều. / [Thêm đơn thuốc] [Bỏ qua]
- ✅ Sẵn sàng rồi / [Tìm bác sĩ gần bạn]
- ❌ Chào mừng bạn đến với ứng dụng chăm sóc sức khỏe hàng đầu Việt Nam! — khen mình, không nói người dùng được gì.
- ❌ Ứng dụng giúp bạn quản lý sức khỏe một cách toàn diện và hiệu quả. — "một cách", tính từ rỗng.
