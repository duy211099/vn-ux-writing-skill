export default function Checkout({ total, onPay }) {
  return (
    <section>
      <h2>Thanh toán</h2>
      <p>Tổng cộng: {total}</p>
      <button onClick={onPay}>Xác nhận</button>
      <p className="note">Vui lòng kiểm tra kỹ thông tin trước khi thanh toán.</p>
    </section>
  );
}
