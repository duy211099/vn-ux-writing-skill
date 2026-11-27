"""Generate vi.json for the review/analyze large-repo eval.

Run: python3 gen.py  (writes vi.json next to this file; deterministic)

1,200 keys across 40 screens. Most strings are fine. A fixed set of
keys carries known problems so the eval can check which ones `analyze`
surfaces: generic errors, "Bạn có chắc chắn... không?", "của bạn",
passive "đã được... thành công" (also planted in 20 "saved" keys, so the
problems outnumber what one reply can show), "xoá" against the file's "xóa", and
"quý khách" against the file's "bạn".
"""

import json
import unicodedata
from pathlib import Path

SCREENS = [
    "home", "search", "menu", "dish", "cart", "checkout", "payment", "order",
    "tracking", "rating", "profile", "address", "wallet", "voucher", "chef",
    "kitchen", "schedule", "notification", "settings", "language", "help",
    "faq", "chat", "report", "referral", "loyalty", "subscription", "invoice",
    "refund", "delivery", "pickup", "favorite", "history", "review", "photo",
    "allergy", "diet", "family", "gift", "event",
]

FINE = [
    ("title{n}", "Món nổi bật {n}"),
    ("empty{n}", "Chưa có món nào trong mục {n}. Xem thực đơn hôm nay."),
    ("save{n}", "Lưu"),
    ("saved{n}", "Đã lưu thay đổi"),
    ("remove{n}", "Xóa món"),
    ("removed{n}", "Đã xóa món khỏi danh sách"),
    ("retry{n}", "Thử lại"),
    ("open{n}", "Xem chi tiết"),
    ("hint{n}", "Nhập tên món, ví dụ: bún chả"),
    ("count{n}", "{{count}} món"),
    ("time{n}", "Giao lúc {{time}}"),
    ("price{n}", "Giá: {{price}}đ"),
    ("back{n}", "Quay lại"),
    ("next{n}", "Tiếp tục"),
    ("close{n}", "Đóng"),
]

# (screen, key, text): the planted problems.
BAD = [
    ("payment", "error", "Đã xảy ra lỗi. Vui lòng thử lại sau."),
    ("order", "error", "Lỗi: thao tác thất bại"),
    ("refund", "error", "Có lỗi xảy ra, vui lòng thử lại"),
    ("cart", "removeConfirm", "Bạn có chắc chắn muốn xóa món này không?"),
    ("address", "deleteConfirm", "Bạn có chắc chắn muốn xóa địa chỉ này không?"),
    ("profile", "saved", "Thông tin của bạn đã được cập nhật thành công"),
    ("order", "placed", "Đơn hàng của bạn đã được đặt thành công"),
    ("wallet", "topup", "Ví của bạn đã được nạp tiền thành công"),
    ("voucher", "remove", "Xoá mã giảm giá"),
    ("subscription", "cancel", "Huỷ gói đăng ký"),
    ("invoice", "notice", "Quý khách vui lòng kiểm tra hóa đơn trước khi thanh toán."),
    ("refund", "notice", "Quý khách sẽ nhận lại tiền trong 3–5 ngày làm việc."),
]


def build() -> dict:
    data: dict[str, dict[str, str]] = {}
    for i, screen in enumerate(SCREENS):
        block: dict[str, str] = {}
        for j in range(2):
            n = i * 2 + j + 1
            for key, text in FINE:
                block[key.format(n=n)] = text.replace("{n}", str(n))
        data[screen] = block
    # Every other screen: the first "saved" key in the passive translation tic.
    for i, screen in enumerate(SCREENS):
        if i % 2 == 1:
            data[screen][f"saved{i * 2 + 1}"] = "Thay đổi đã được lưu thành công"
    for screen, key, text in BAD:
        data[screen][key] = text
    return data


def main() -> None:
    data = build()
    text = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    text = unicodedata.normalize("NFC", text)
    (Path(__file__).parent / "vi.json").write_text(text, encoding="utf-8")
    print(sum(len(v) for v in data.values()), "keys")


if __name__ == "__main__":
    main()
