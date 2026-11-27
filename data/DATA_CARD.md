# Data card — dữ liệu bản chạy thử dùng

> Điền ở guide bước 2.4 (bản đầu ở CP2, đủ ở CP3). Ôn lại: ngày 6 · lab ngày 6. Chấm ở rubric R4.
> Một trang. Mỗi dataset một mục. Dữ liệu chạy thử (bài mẫu, thông báo mẫu, đoạn transcript…) để trong thư mục `data/` này.
> Không commit nguyên tài liệu khoá, dữ liệu cá nhân thật hay nguyên file data BTC cấp — chỉ đoạn trích ngắn, bản viết lại, hoặc số đã tổng hợp.

## Dataset 1 · Hồ sơ 7 đơn khiếu nại hàng vỡ (`data/orders.json`)

| | |
|---|---|
| Dùng để làm gì | nguồn cho công cụ tra hồ sơ đơn trong `codebase/tools.py` (log đóng gói, log vận chuyển, khiếu nại + mô tả ảnh của khách) · nền cho 18 trong 20 câu thử `tu_viet` ở `eval/benchmark.csv` (B01–B08, K01–K07, T01–T05; K03 và K04 cố ý không có đơn trong data: thiếu mã đơn, mã DH99 không tồn tại) |
| Từ đâu | nhóm tự viết (Phan Trung Hiếu, 27/11/2026), mô phỏng hồ sơ một shop online nhỏ bán đồ dễ vỡ. Tên shop, khách, đơn vị vận chuyển (`VC-A`, `VC-B`) đều giả |
| Xử lý những bước gì | viết tay, không lấy từ nguồn thật nên không cần ẩn danh · đã gỡ mọi trường đáp án (bên chịu, ghi chú mâu thuẫn) khỏi file để công cụ không lộ đáp án cho model · đáp án chỉ nằm ở `eval/benchmark.csv` |
| Số dòng / số đoạn | 7 đơn · 7 log đóng gói · 18 sự kiện vận chuyển · 7 khiếu nại · 2 đơn vị vận chuyển |
| Phiên bản / ngày lấy | v1 · 27/11/2026 |
| Nhãn | `synthetic` |
| Giới hạn | mỗi đơn cố ý rơi vào một tình huống: lỗi vận chuyển (DH01), lỗi đóng gói (DH02), lỗi phía khách (DH03), thiếu bằng chứng (DH04), bằng chứng mâu thuẫn (DH05), lỗi vận chuyển nhưng quá hạn khiếu nại (DH06), ngoài phạm vi vì sai màu (DH07). Bộ này sạch và rõ hơn hồ sơ thật: ảnh chỉ có mô tả chữ, không có ảnh thật. Hạn khiếu nại 7 và 5 ngày là giả lập *(tự ước tính)*, không phải chính sách của hãng thật |

**Data `synthetic`:** viết tay, không dùng prompt hay seed. Người kiểm: Phan Trung Hiếu · đã kiểm tay 7/7 đơn (đối chiếu log mỗi đơn với đáp án ở benchmark: đều dẫn đúng). Data tự dựng **không phải bằng chứng pain**.

## Dataset 2 · 8 đơn dựng từ đánh giá Shopee thật (`data/orders.json` DH08–DH15)

| | |
|---|---|
| Dùng để làm gì | nguồn cho cùng các công cụ trong `codebase/tools.py` · nền cho 10 câu thử R01–R10 (`data_that`) ở `eval/benchmark.csv` |
| Từ đâu | `evidence/shopee-reviews.csv` (Vĩnh đọc tay các đánh giá 1–2 sao công khai trên Shopee, 27/11/2026): A006, A021, A023, A028, A030 (hàng vỡ/hỏng) · A015, A009 (ngoài phạm vi: sai màu nắp, thiếu phụ kiện) · A014 (vỡ khi dùng) |
| Xử lý những bước gì | `customer_claim.text` lấy từ cột `trich_ngan`, chỉ giữ phần của người mua · bỏ ghi chú mã hoá của Vĩnh (vd "(vỡ khi dùng)", "[cần Vĩnh xem lại…]") và phản hồi của shop · không có tên người mua nên không cần ẩn danh thêm · **không bịa** log đóng gói, log vận chuyển, giá trị, đơn vị vận chuyển: các trường này để trống (`{}`, `[]`, `null`) |
| Số dòng / số đoạn | 8 đơn · 8 khiếu nại · 0 log đóng gói · 0 sự kiện vận chuyển |
| Phiên bản / ngày lấy | v1 · 27/11/2026 |
| Nhãn | thật (lời người mua), dựng thành dạng đơn |
| Giới hạn | đánh giá công khai chỉ có lời một phía, không có log, nên hầu hết ca hàng vỡ có đáp án đúng là "chưa đủ bằng chứng"; bộ này kiểm việc AI không kết luận theo lời khách. `trich_ngan` là đoạn trích ngắn, có thể đã rút gọn. A021 đang được Vĩnh đánh dấu "cần xem lại" (không rõ có phải hàng vỡ). Cùng một loại hàng (ly thủy tinh, 3 sản phẩm) |
