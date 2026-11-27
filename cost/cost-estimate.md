# DamageCheck — chi phí khi dùng thật

Người phụ trách: Lê Viết Khoa · cập nhật 27/11/2026. CP3 thử 10 phiên trước 10:00 ngày 28/11; CP4 mô phỏng ≥50 phiên và báo cáo trước 14:30 ngày 28/11.

**Đã chạy thử 10 phiên bằng API thật**, model `gemini-3.5-flash-lite`, không lỗi. Run ID `simulate-try@20261127-223433`; chi tiết `cost/simulate-try.csv`, `cost/simulate-try-summary.md`, `traces/simulate-try.jsonl`. Lượt này kiểm khung/token, **không tính bản nộp ≥50 phiên**. Chưa có eval đã chấm để tính /task thành công. Chi tiết giả định và bàn giao: [README.md](README.md).

## 1. Đầu vào

| Đầu vào | Giá trị | Nguồn / trạng thái |
|---|---|---|
| Quy mô thấp/cơ sở/cao | 10 / 50 / 100 chủ shop | *(tự ước tính)* phạm vi triển khai thử; chưa có shop cam kết dùng |
| Shop ít đơn | share 0.5 · 100 đơn/tháng · 0.38 phiên/tháng | Số đơn và share tự ước tính; tần suất = 100 × 0.0038 |
| Shop vừa đơn | share 0.3 · 300 đơn/tháng · 1.14 phiên/tháng | Số đơn và share tự ước tính; tần suất = 300 × 0.0038 |
| Shop nhiều đơn | share 0.2 · 800 đơn/tháng · 3.04 phiên/tháng | Số đơn và share tự ước tính; tần suất = 800 × 0.0038 |
| Tỉ lệ dùng suy ra | 0.38% làm tròn | Vĩnh: `evidence/summary.md` mục 2 A5; là ước tính từ đánh giá, chưa phải tỉ lệ khiếu nại trên đơn thực |
| Phiên / lượt | 1 ca khiếu nại giả định = 1 phiên = 1 yêu cầu | *(tự ước tính)* mọi ca đều dùng DamageCheck; chưa mô phỏng trao đổi nhiều vòng |
| Mẫu chạy | 50 phiên, seed 42, input thuong/kho (23 câu trong bộ 30) | Cấu hình mô phỏng, không phải quy mô người đã thử; chưa biết tỉ trọng từ chối ngoài thực tế |
| Token thực lượt try | 13.826 vào, 2.955 ra; 10 lần gọi model, 50 lần gọi công cụ | `cost/simulate-try.csv`, usage API |
| Tỉ lệ đạt | Eval đã chấm cùng model, ưu tiên lượt 2 khi nộp CP4 | Chờ Hiếu |

Giá chép và đối chiếu [bảng chung BTC](https://github.com/VinUni-AI20k/K5-L3-Day15-AI-Product-Hackathon/blob/main/further-reading/model-prices.md), mục Google Gemini: BTC tra ngày **25/11/2026**, nhóm đọc/đối chiếu **27/11/2026**. Đơn vị USD/1 triệu token, Standard/Paid Tier, input văn bản, output gồm thinking. Hai tầng Nhỏ/Lớn là cách BTC nhóm theo giá, không khẳng định model nào tốt hơn:

| Model | Input | Output | Nguồn |
|---|---:|---:|---|
| gemini-3.5-flash-lite | 0.30 | 2.50 | [Google](https://aistudio.google.com/docs/pricing#gemini-3.5-flash-lite) |
| gemini-4-hydrogen | 1.50 | 7.50 | [Google](https://aistudio.google.com/docs/pricing#gemini-4-hydrogen) |

**Đã đối chiếu đúng `further-reading/model-prices.md`:** cả hai mức giá khớp bảng đề, có link nguồn chính thức để kiểm lại. Khoa đã chọn `gemini-3.5-flash-lite` để chạy; hai mức giá không có nghĩa đã đo chất lượng của cả hai model. Chưa quy đổi VND vì chưa có nguồn tỷ giá.

## 2. Kết quả

- Lượt 10 phiên: **đã chạy API thật, 10/10 không lỗi**; lượt này không tính nộp.
- Lượt đầy đủ ≥50 phiên / model thực đo / run ID: **chưa có**.
- Eval cùng model / run ID / số đạt/tổng: **chưa có**.
- Chi phí/phiên lượt thử có số đo; /tác vụ thành công chưa tính vì thiếu tỉ lệ đạt. Dự phóng tháng dưới đây chỉ từ lượt thử, chưa phải kết quả CP4.

Bảng chép từ `cost/simulate-try-summary.md` (lượt thử 10 phiên):

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (10 người) | Chi phí / tháng — cơ sở (50 người) | Chi phí / tháng — cao (100 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gemini-3.5-flash-lite (vào 0.3 · ra 2.5 $/1M) | $0.0012 | — | — | $0.0132 | $0.0658 | $0.1316 | $0.0013 |
| gemini-4-hydrogen (vào 1.5 · ra 7.5 $/1M) | $0.0043 | — | — | $0.0490 | $0.2448 | $0.4895 | $0.0049 |

**Đo token trên `gemini-3.5-flash-lite`, tính giá theo `gemini-3.5-flash-lite` và `gemini-4-hydrogen`.** Chưa chạy/đánh giá chất lượng Hydrogen. Mẫu ngẫu nhiên 10 phiên chỉ có 5 shop ít đơn và 5 shop vừa đơn, không có shop nhiều đơn; dự phóng của khung cho persona chưa có mẫu dùng chi phí chung, cần đọc cùng giới hạn này. Không đổi seed hoặc sửa kết quả để làm đẹp độ phủ. Sau lượt đầy đủ ≥50 phiên, bổ sung bảng mới và run ID, giữ lượt thử làm lịch sử.

## 3. Phương pháp và giới hạn

```text
phiên/người/tháng = đơn/người/tháng × 0.0038 × tỉ lệ dùng sản phẩm (giả định 1)
USD/phiên = (token vào × giá vào + token ra × giá ra) / 1.000.000
USD/task thành công theo khung = USD trung bình/phiên ÷ tỉ lệ đạt eval
USD/tháng = Σ (người dùng × share persona × phiên/người/tháng × USD/phiên persona)
```

A5 kết hợp tỉ lệ đánh giá xấu cấp sản phẩm với mẫu đánh giá xấu được chọn; review không đại diện mọi đơn hàng, các mặt hàng/từ khoá không đều nhau. Không diễn giải 0.38% là tỉ lệ hàng vỡ đã xác minh hay mọi ca đều thành người dùng trả phí. Kịch bản hiện dùng trọn ca vỡ để ước tính nhu cầu, chưa có dữ liệu tỷ lệ chấp nhận sản phẩm hoặc hỏi lại nhiều lượt.

Một input như K07 có thể hỏi hai đơn. Vì vậy không đồng nhất một câu hỏi đạt với đúng một đơn tranh chấp xử lý xong. Tỉ lệ đạt là theo câu thử; khung không đo trực tiếp kết quả tiền hoàn/bồi thường.

Giá hai model trên một lượng token chỉ là so sánh giá; ghi rõ model đo và model tính giá. Tóm tắt khung loại phiên lỗi khỏi trung bình: phải ghi số phiên lỗi, nêu phần phí retry/lỗi có thể chưa đủ. Chưa tính hosting, lưu trữ, xử lý ảnh/video hoặc thời gian người duyệt.

## 4. So với impact và hoàn tất CP4

Vĩnh chưa đo được thời gian/tiền xử lý trực tiếp mỗi ca. Chưa thể kết luận đáng triển khai từ số giá trị đơn giả lập hoặc tiền bồi thường đề xuất.

- [x] Đối chiếu giá hai tầng với repo đề, có link và ngày xem.
- [x] Khoa chọn `gemini-3.5-flash-lite`, cấu hình API thật đã gọi thành công.
- [x] Có 10 phiên thử bằng API thật cho CP3 (`simulate-try@20261127-223433`).
- [ ] Có ≥50 phiên đầy đủ và bảng summary cho CP4; ghi phiên lỗi.
- [ ] Có eval đã chấm cùng model và run ID để tính /task thành công.
- [ ] So sánh impact cùng đơn vị hoặc nêu thiếu dữ liệu.
- [ ] Đồng bộ kết quả sang spec §8 và slide, ghi changelog §10.
