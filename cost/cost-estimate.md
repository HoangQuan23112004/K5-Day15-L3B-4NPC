# DamageCheck — chi phí khi dùng thật

Người phụ trách: Lê Viết Khoa · cập nhật 27/11/2026. CP3 thử 10 phiên trước 10:00 ngày 28/11; CP4 mô phỏng ≥50 phiên và báo cáo trước 14:30 ngày 28/11.

**Đã chạy mô phỏng đầy đủ 50 phiên bằng API thật**, model `gemini-3.5-flash-lite` (`DAMAGECHECK_TODAY=2026-11-27`, `--rate-from eval/run-2.csv`, `--wait 4`), **0/50 phiên lỗi**. Run ID `simulate-1@20261127-234357`; chi tiết `cost/simulate-1.csv`, `cost/simulate-1-summary.md`, `traces/simulate-1.jsonl`. Tỉ lệ đạt lấy từ lượt 2 chính thức (`run-2@20261127-230337`): **28/30 (93%)**, đạt chuẩn §7. Trước đó ở CP3 đã chạy thử 10 phiên (`simulate-try@20261127-223433`, 10/10 không lỗi, giữ làm lịch sử). Chi tiết giả định và bàn giao: [README.md](README.md).

## 1. Đầu vào

| Đầu vào | Giá trị | Nguồn / trạng thái |
|---|---|---|
| Quy mô thấp/cơ sở/cao | 10 / 50 / 100 chủ shop | *(tự ước tính)* phạm vi triển khai thử; chưa có shop cam kết dùng |
| Shop ít đơn | share 0.5 · 100 đơn/tháng · 0.38 phiên/tháng | Số đơn và share tự ước tính; tần suất = 100 × 0.0038 |
| Shop vừa đơn | share 0.3 · 300 đơn/tháng · 1.14 phiên/tháng | Số đơn và share tự ước tính; tần suất = 300 × 0.0038 |
| Shop nhiều đơn | share 0.2 · 800 đơn/tháng · 3.04 phiên/tháng | Số đơn và share tự ước tính; tần suất = 800 × 0.0038 |
| Tỉ lệ dùng suy ra | 0.38% làm tròn | Vĩnh: `evidence/summary.md` mục 2 A5; là ước tính từ đánh giá, chưa phải tỉ lệ khiếu nại trên đơn thực |
| Phiên / lượt | 1 ca khiếu nại giả định = 1 phiên = 1 yêu cầu | *(tự ước tính)* mọi ca đều dùng DamageCheck; chưa mô phỏng trao đổi nhiều vòng |
| Mẫu chạy | 50 phiên, seed 42, input thuong/kho (23 câu trong bộ 30) | Cấu hình mô phỏng (`shop_it_don` 26 · `shop_vua_don` 14 · `shop_nhieu_don` 10), không phải quy mô người đã thử; chưa biết tỉ trọng từ chối ngoài thực tế |
| Token thực lượt chính thức (50 phiên) | 74.200 vào, 11.840 ra; 45 lần gọi model, 227 lần gọi công cụ (5 phiên `S014, S016, S018, S024, S045` rơi vào câu thiếu mã đơn / mã đơn không tồn tại nên code dừng sớm không gọi model) | `cost/simulate-1.csv`, usage API (lượt try 10 phiên trước đó: 13.826 vào, 2.955 ra) |
| Tỉ lệ đạt | Lượt 2 (`run-2@20261127-230337`): **28/30 (93%)**, đạt chuẩn §7 (lượt 1 `run-1@20261127-222917`: 24/30 = 80%) | `eval/run-2.csv`, `eval/report.md` (Hiếu chấm; `--rate-from eval/run-2.csv`) |

Giá chép và đối chiếu [bảng chung BTC](https://github.com/VinUni-AI20k/K5-L3-Day15-AI-Product-Hackathon/blob/main/further-reading/model-prices.md), mục Google Gemini: BTC tra ngày **25/11/2026**, nhóm đọc/đối chiếu **27/11/2026**. Đơn vị USD/1 triệu token, Standard/Paid Tier, input văn bản, output gồm thinking. Hai tầng Nhỏ/Lớn là cách BTC nhóm theo giá, không khẳng định model nào tốt hơn:

| Model | Input | Output | Nguồn |
|---|---:|---:|---|
| gemini-3.5-flash-lite | 0.30 | 2.50 | [Google](https://aistudio.google.com/docs/pricing#gemini-3.5-flash-lite) |
| gemini-4-hydrogen | 1.50 | 7.50 | [Google](https://aistudio.google.com/docs/pricing#gemini-4-hydrogen) |

**Đã đối chiếu đúng `further-reading/model-prices.md`:** cả hai mức giá khớp bảng đề, có link nguồn chính thức để kiểm lại. Khoa đã chọn `gemini-3.5-flash-lite` để chạy; hai mức giá không có nghĩa đã đo chất lượng của cả hai model. Chưa quy đổi VND vì chưa có nguồn tỷ giá.

## 2. Kết quả

- Lượt chính thức ≥50 phiên: **50/50 phiên API thật không lỗi** (`simulate-1@20261127-234357`, model thực đo `gemini-3.5-flash-lite`, `DAMAGECHECK_TODAY=2026-11-27`, `--rate-from eval/run-2.csv --wait 4`).
- Eval cùng model / run ID / số đạt/tổng: **Lượt 2 `run-2@20261127-230337` đạt 28/30 (93%)** (thuong 9/9 · kho 12/14 · tu_choi 7/7 · `can_cu_co_that` 30/30 · `khong_doan_khi_thieu` 6/6 — đạt chuẩn §7; lượt 1 `run-1@20261127-222917` trước đó đạt 24/30 = 80%).
- **Phiên lỗi (không tính vào trung bình): 0/50.** (5 phiên có `tokens_in = 0, tokens_out = 0` là các lượt rơi vào câu thiếu mã đơn hoặc mã đơn không có trong dữ liệu như K03/K04 nên `agent.py` chặn sớm bằng code, không phải lỗi API.)

Bảng theo persona chép từ `cost/simulate-1-summary.md` (50 phiên, seed 42):

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| shop_it_don | 26 | 1 | 1587 | 254 | 1.0 | 4.8 |
| shop_vua_don | 14 | 1 | 1535 | 254 | 0.9 | 4.6 |
| shop_nhieu_don | 10 | 1 | 1144 | 166 | 0.7 | 3.6 |

Bảng chi phí chép nguyên từ `cost/simulate-1-summary.md` (tỉ lệ đạt 28/30 = 93% từ `eval/run-2.csv`):

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (10 người) | Chi phí / tháng — cơ sở (50 người) | Chi phí / tháng — cao (100 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gemini-3.5-flash-lite (vào 0.3 · ra 2.5 $/1M) | $0.0010 | $0.0011 | $0.0011 | $0.0105 | $0.0524 | $0.1048 | $0.0010 |
| gemini-4-hydrogen (vào 1.5 · ra 7.5 $/1M) | $0.0040 | $0.0043 | $0.0043 | $0.0406 | $0.2029 | $0.4057 | $0.0041 |

**Đo token trên `gemini-3.5-flash-lite`, tính giá theo `gemini-3.5-flash-lite` và `gemini-4-hydrogen`.** Chưa chạy/đánh giá chất lượng `gemini-4-hydrogen` (model khác bộ tách token hoặc mức suy luận thì số token thực tế có thể lệch). Mẫu 50 phiên với seed 42 đã phủ đủ cả 3 persona (26 / 14 / 10 phiên, gần sát tỉ lệ 50% / 30% / 20%).

*Lịch sử CP3 (lượt thử 10 phiên `simulate-try@20261127-223433`, 10/10 không lỗi, chạy trước khi khóa điểm eval nên không tính nộp):* `gemini-3.5-flash-lite` $0.0012/phiên, tháng thấp/cơ sở/cao $0.0132 / $0.0658 / $0.1316 ($0.0013/người/tháng); `gemini-4-hydrogen` $0.0043/phiên, tháng $0.0490 / $0.2448 / $0.4895 ($0.0049/người/tháng). Chi tiết giữ nguyên tại `cost/simulate-try-summary.md`.

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

Theo `spec.md` §2 (Vĩnh cập nhật dùng chung bộ số với `cost/personas.yaml`): trung bình mỗi shop có **1,14 ca/tháng**, mỗi ca tốn khoảng **30 phút + 50.000đ** tiền hàng tranh chấp *(tự ước tính)* → impact mỗi shop khoảng **34 phút + 57.000đ / shop / tháng** (kịch bản cơ sở 50 shop ≈ **28,5 giờ + 2,85 triệu đồng / tháng**).

So với chi phí AI chính thức (50 phiên `simulate-1@20261127-234357` trên `gemini-3.5-flash-lite`, tỉ lệ đạt lượt 2 = 93%):
- **Chi phí / phiên:** **$0.0010** · **Chi phí / task thành công:** **$0.0011** (tính theo giá tầng Lớn `gemini-4-hydrogen`: $0.0040/phiên · $0.0043/task thành công).
- **Chi phí / người (shop) / tháng (kịch bản cơ sở 50 shop):** **$0.0010/shop/tháng**, tổng cả 50 shop là **$0.0524/tháng** (nếu tính theo giá `gemini-4-hydrogen`: **$0.0041/shop/tháng**, tổng 50 shop là **$0.2029/tháng**).
- **Kết luận một dòng:** Chi phí suy luận AI (~$0.0010/shop/tháng ở `gemini-3.5-flash-lite`, tức chưa tới $0.06/tháng cho cả 50 shop) nhỏ hơn nhiều bậc độ lớn so với ~34 phút đối chiếu thủ công và ~57.000đ tiền hàng tranh chấp mỗi shop mỗi tháng *(tự ước tính)*, nên hoàn toàn khả thi về chi phí token ngay cả khi cộng dự phòng retry — phần chi phí quyết định khi vận hành thật sẽ nằm ở thời gian chủ shop duyệt bản nháp và hạ tầng nối dữ liệu chứ không phải tiền gọi model.

- [x] Đối chiếu giá hai tầng với repo đề, có link và ngày xem.
- [x] Khoa chọn `gemini-3.5-flash-lite`, cấu hình API thật đã gọi thành công.
- [x] Có 10 phiên thử bằng API thật cho CP3 (`simulate-try@20261127-223433`).
- [x] Đồng bộ bộ số quy mô (10/50/100 shop, 100/300/800 đơn, 1,14 ca/shop/tháng) với `spec.md` §2 và lượt 1 `run-1@20261127-222917` (24/30 = 80%).
- [x] Có ≥50 phiên đầy đủ và bảng summary cho CP4 (`simulate-1@20261127-234357`, `--rate-from eval/run-2.csv`, 0/50 phiên lỗi).
- [x] Đồng bộ kết quả ≥50 phiên sang `spec.md` §8 và ghi changelog §10 (còn đưa bảng rút gọn lên slide thuyết trình).
