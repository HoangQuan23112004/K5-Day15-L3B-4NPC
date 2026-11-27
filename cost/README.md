# Khoa — bàn giao CP3

Ngày 27/11/2026 · CP3: 10:00 ngày 28/11 · CP4: 14:30 ngày 28/11.

## 1. Trạng thái theo phân công mới

| Việc | Đã làm | Còn thiếu / người bàn giao |
|---|---|---|
| Persona | Đã điền 3 persona theo số đơn/tháng, share cộng 1; uses_per_month suy từ A5 của Vĩnh | Số shop, share, số đơn và tỷ lệ dùng là tự ước tính, chưa có khảo sát xác nhận |
| Giá ≥2 model | Đã đối chiếu bảng BTC: tầng Nhỏ `gemini-3.5-flash-lite`, tầng Lớn `gemini-4-hydrogen`; có link và ngày xem | Khoa đã chọn chạy `gemini-3.5-flash-lite`; model còn lại dùng so giá |
| Spec §5 | Đã có trên main ở `607f8a6`: 13 kịch bản + 2 tấn công, đủ 4 lớp | Quân đã duyệt và cập nhật quy tắc 1, 8 trước khi chạy lượt 1 |
| Chấm độc lập 5 output lượt 1 | Đã trích 5 output (`B01, K02, R01, T02, T04`) của lượt 1 chính thức `run-1@20261127-222917` sang `eval/second-review-outputs.md` (không kèm cột `pass`) và mẫu chấm ở `eval/second-review.md` | Theo phân công của Quân (do Khoa viết §5), nhờ Vĩnh chấm độc lập 5 câu trên `run-1@20261127-222917` để điền độ khớp `__/5` vào `eval/README.md` mục 3 |
| Kiểm chéo 20 dòng của Vĩnh | Đã điền và Khoa xác nhận kiểm tay; Vĩnh đã đối chiếu và thống nhất dòng A035 theo Khoa (`shop`) | Đã hoàn tất: `vo_khi_giao` khớp 20/20, `loi_do` khớp 7/8 (đã ghi vào `evidence/data-mining.md` mục 5 và `evidence/kiem-cheo.md`) |
| Thử mô phỏng 10 phiên | Đã chạy `gemini-3.5-flash-lite`, 10/10 không lỗi, run `simulate-try@20261127-223433` | Lượt thử không tính bản nộp ≥50 phiên; lượt 1 `run-1@20261127-222917` đạt 24/30 (80%), bản ≥50 phiên ở CP4 sẽ chạy với `--rate-from eval/run-2.csv` |
| Hẹn 2–3 người ngoài nhóm | Có lời mời và kịch bản 10 phút ở `validation/log.md` | Khoa xác nhận chưa có người ngày 27/11; chưa gửi lời mời hoặc có lịch hẹn |

## 2. Cách suy ra tần suất

Nguồn: `evidence/summary.md` mục 2 (Vĩnh) và cách đếm `evidence/count.py`:

```text
A5 = (205 đánh giá 1–2 sao / 18.566 tổng đánh giá) × (21 ca vỡ / 61 đánh giá xấu có chữ)
   ≈ 0.0038 ≈ 0.38%
```

Theo phân công, cấu hình dùng tỉ lệ **làm tròn 0.0038**. Số đơn/tháng của ba persona là *(tự ước tính)*: 100, 300, 800; tỷ lệ sử dụng sản phẩm trên mỗi ca vỡ giả định là 1. Suy ra 0.38, 1.14, 3.04 phiên/người/tháng. Giữ số thập phân: đó là kỳ vọng theo tháng, không phải số phiên bắt buộc phải nguyên.

Đây là kịch bản suy từ review, không phải dữ liệu quan sát tỷ lệ khiếu nại hay tỷ lệ dùng sản phẩm trên mọi đơn. Vĩnh đã bổ sung ước tính impact mỗi ca ở `spec.md` §2 (~30 phút + ~50.000đ tiền hàng tranh chấp *(tự ước tính)* → trung bình ~1,14 ca/shop/tháng ≈ 34 phút + 57.000đ/shop/tháng), dùng chung bộ số quy mô 10/50/100 shop và 100/300/800 đơn/tháng với `cost/personas.yaml`.

Đơn vị mô phỏng: 1 phiên = 1 yêu cầu khiếu nại, 1 lượt `answer()`. K07 vẫn có thể hỏi hai đơn trong một yêu cầu; trace đo mọi lời gọi model. Chưa mô phỏng hội thoại nhiều lượt cùng hồ sơ. Tập đầu vào mặc định có 23 câu thường/khó; lưu lượng từ chối thật chưa có tỉ trọng.

## 3. Chạy khi có cấu hình thật

1. Quân xác nhận provider/model, Khoa đặt API key trực tiếp trong `.env` (không commit, không gửi vào chat).
2. Giữ `DAMAGECHECK_TODAY=2026-11-27` để cùng ngày tính hạn với bộ thử; kiểm model không phải `fake`.
3. Kiểm giá trong YAML khớp model thực chạy và bảng đề; nếu giá model khác chỉ dùng để so sánh, ghi rõ.
4. Chạy từ gốc repo:

```powershell
python run.py check
python run.py simulate --try
```

Lượt thử 10 phiên dùng để kiểm luồng/token/lỗi, **không tính bản nộp ≥50 phiên**. Không cần chờ eval đã chấm để đo chi phí/phiên; eval đã chấm cùng model cần để tính /task thành công. Nếu chưa có API thật, không tạo CSV giả hoặc lấy token 0 làm kết quả.

File try chỉ dùng tên cố định: không chạy lại ghi đè lượt đã có; tuân thủ quy định lưu kết quả. Lượt đầy đủ sau đó dùng `python run.py simulate --rate-from eval/run-N.csv`, thay N bằng lượt thực đã chấm.

## 4. Các đầu vào cần người thật

- Quân: đã duyệt §5, chạy lượt 1 chính thức `run-1@20261127-222917` và merge nhánh của Khoa vào `main`; chuẩn bị sửa nhóm lỗi mã căn cứ "ma" (`R02–R04`) và ca lẫn (`R06–R07`) để chạy lượt 2.
- Hiếu: đã chấm chính thức 30 output trong `eval/run-1.csv` (`run-1@20261127-222917`, đạt 24/30 = 80%) và viết `eval/grade.py` (khớp 30/30).
- Vĩnh: đã thống nhất dòng `A035` (`vo_khi_giao` 20/20, `loi_do` 7/8) và đồng bộ bộ số impact `spec.md` §2 với `cost/personas.yaml`. Nhờ Vĩnh chấm độc lập 5 câu (`B01, K02, R01, T02, T04`) của `run-1@20261127-222917` trong `eval/second-review.md` để lấy độ khớp `__/5` cho `eval/README.md` mục 3.
- Khoa: tuyển 2–3 người ngoài nhóm đúng vai cho phiên dùng thử sáng/trưa 28/11; chạy mô phỏng ≥50 phiên sau khi có kết quả lượt 2.

## 5. Kiểm tra đã thực hiện

- `python run.py check`: 30 câu, 10/30 data thật, 4 metric; không có cảnh báo.
- `python evidence/count.py`: chạy lại được A5 làm tròn 0.38% từ 9 sản phẩm và 61 đánh giá.
- Bộ đọc YAML của chính khung đọc được cấu hình, không có cảnh báo; 3 persona, share = 1, đủ 2 giá đúng bảng BTC.
- Sinh kế hoạch ngoại tuyến 10/50 phiên, seed 42 tái lập được và đủ 3 persona trong kế hoạch đầy đủ. Đây không phải mô phỏng đã gọi API; không tạo CSV kết quả để thay thế lượt thật.
- Kiểm nhãn 20 dòng không thay đổi so với bản đã lưu trước khi đối chiếu. §5, chuẩn §7, benchmark, metric và code khung giữ nguyên.
- Đã gọi API thật 10 phiên: tổng token vào 13.826 / ra 2.955, lỗi 0/10; file CSV/summary/trace được giữ nguyên. Lượt thử không có mẫu shop nhiều đơn, chưa coi là kết quả mô phỏng đầy đủ.
- Lượt 1 chính thức trên `main` là `run-1@20261127-222917` (Hiếu đã chấm 24/30 = 80%). Đã trích 5 output của `run-1@20261127-222917` sang `eval/second-review-outputs.md` để người chấm thứ hai chấm đúng lượt chính thức.
