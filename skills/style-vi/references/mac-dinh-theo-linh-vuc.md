# Mặc định theo lĩnh vực

Dùng khi tạo file giọng văn (`docs/giong-van.md`) lần đầu. Đoán lĩnh vực từ tên dự án, `package.json`, README và màn hình hiện có, rồi lấy cả hàng tương ứng. Không hỏi người dùng chọn: ghi vào file, báo một dòng, để họ sửa.

## Giao diện và văn bản dài

Cột giao diện giống bảng trong `ux-writing-vi` (`references/xung-ho-va-giong-dieu.md`). Cột văn bản dài điền vào phần `## Văn bản dài` của file giọng văn.

| Lĩnh vực | Gọi người dùng | Giọng giao diện | Trợ từ | Người viết tự xưng | Độ dài câu | Mức cá nhân |
|---|---|---|---|---|---|---|
| Ngân hàng, ví điện tử, bảo hiểm, chứng khoán (fintech) | *quý khách* hoặc bỏ đại từ | Trang trọng, chính xác | Không *nhé*; *vui lòng* được dùng khi yêu cầu | *chúng tôi* | ngắn | trung tính |
| Y tế, dịch vụ công, pháp lý | Bỏ đại từ, hoặc *quý khách* / *bạn* tùy đối tượng | Trang trọng, điềm tĩnh | Không *nhé* | *chúng tôi* hoặc tên tổ chức | ngắn | trung tính |
| Thương mại điện tử, giao đồ ăn, gọi xe, du lịch | *bạn* | Thân thiện, gọn | *nhé* thưa thớt | tên sản phẩm | xen kẽ | trò chuyện |
| Mạng xã hội, giải trí, học tập cho người trẻ | *bạn* | Thân thiện, có thể vui | *nhé* được dùng | *mình* | xen kẽ | trò chuyện |
| Công cụ làm việc, B2B, sản phẩm của công ty cho lập trình viên | Bỏ đại từ, hoặc *bạn* | Trung tính, ngắn | Hầu như không dùng | *chúng tôi* | xen kẽ | trung tính |
| Công cụ indie, dự án cá nhân, mã nguồn mở của một người | Bỏ đại từ, hoặc *bạn* | Trung tính, ngắn | Hầu như không dùng | *mình* | xen kẽ | có quan điểm |

Mọi lĩnh vực: `Tránh dùng: bên cạnh đó, không chỉ… mà còn, hãy cùng, tóm lại, vô cùng`. `Đoạn văn mẫu` để nguyên placeholder, trừ khi người dùng đưa đoạn văn.

Phân biệt công cụ của công ty với công cụ indie qua dấu hiệu nhìn thấy được: README viết "tôi"/"mình", `author` trong `package.json` là một người, `git log` chỉ có một tác giả → indie. Có tên công ty, trang "Về chúng tôi", nhiều tác giả → công ty.

Không chắc lĩnh vực nào: giao diện dùng *bạn*, trung tính thân thiện; văn bản dài dùng tên sản phẩm, xen kẽ, trung tính.

## Khi dự án đã có chữ

Mặc định chỉ dùng khi dự án chưa có lựa chọn rõ ràng.

- **Chuỗi giao diện** (`vi.json`, `*_vi.arb`, `vi.lproj`, chữ viết thẳng trong component): nếu đa số đã dùng một cách gọi (*quý khách*, *anh/chị*, *bạn*) hoặc một kiểu dấu thanh (*xóa* hay *xoá*), ghi theo đó, kể cả khi khác bảng trên.
- **Bài viết đã có** (README, `blog/`, `docs/`, `content/`, file `.md`/`.mdx` tiếng Việt): nếu người viết đã tự xưng nhất quán (*mình*, *tôi*, *chúng tôi*), ghi theo đó.
- Đang trộn nhiều cách: chọn cách chiếm đa số, ghi vào file, và báo một dòng về chỗ lệch.

## Ví dụ văn bản dài theo hàng

✅ (fintech, *chúng tôi*, ngắn, trung tính) Từ ngày 1/12, phí chuyển tiền liên ngân hàng là 0đ. Chúng tôi áp dụng cho mọi tài khoản, không cần đăng ký.
❌ (fintech) Mình vui lắm khi báo tin này nè: chuyển tiền giờ miễn phí luôn!

✅ (giao đồ ăn, tên sản phẩm, xen kẽ, trò chuyện) Tháng này Bếp Nhà có thêm 40 đầu bếp ở Gò Vấp. Phần lớn nấu món miền Trung, nên ai thèm bún bò thì có thêm lựa chọn.
❌ (giao đồ ăn) Bên cạnh đó, Bếp Nhà không chỉ mang lại bữa ăn ngon mà còn mang lại trải nghiệm vô cùng tuyệt vời.

✅ (công cụ indie, *mình*, xen kẽ, có quan điểm) Mình bỏ tính năng đồng bộ đám mây. Nó làm app chậm, mà gần như không ai dùng.
❌ (công cụ indie) Chúng tôi xin trân trọng thông báo về việc điều chỉnh tính năng đồng bộ.
