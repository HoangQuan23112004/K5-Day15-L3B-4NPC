# Khoa — bàn giao CP3

Ngày 27/11/2026 · CP3: 10:00 ngày 28/11 · CP4: 14:30 ngày 28/11.

## 1. Trạng thái theo phân công mới

| Việc | Đã làm | Còn thiếu / người bàn giao |
|---|---|---|
| Persona | Đã điền 3 persona theo số đơn/tháng, share cộng 1; uses_per_month suy từ A5 của Vĩnh | Số shop, share, số đơn và tỷ lệ dùng là tự ước tính, chưa có khảo sát xác nhận |
| Giá ≥2 model | Đã đối chiếu bảng BTC: tầng Nhỏ `gemini-3.5-flash-lite`, tầng Lớn `gemini-4-hydrogen`; có link và ngày xem | Khoa đã chọn chạy `gemini-3.5-flash-lite`; model còn lại dùng so giá |
| Spec §5 | Đã có trên main ở `607f8a6`: 13 kịch bản + 2 tấn công, đủ 4 lớp | Quân chưa xác nhận duyệt; nội dung nhờ duyệt ở `docs/khoa-ban-giao-cp3.md`, chưa gửi |
| Chấm độc lập 5 output lượt 1 | Đã có run-1 30 output thật; Khoa đã kiểm tay và chốt 5 câu chọn trước ở `eval/second-review.md` khi toàn bộ pass còn trống | Chờ Hiếu chấm lần đầu cả bộ để đối chiếu lấy số khớp `__/5` |
| Kiểm chéo 20 dòng của Vĩnh | Đã điền và Khoa xác nhận kiểm tay; nhãn được giữ nguyên trước khi so | Tính đối chiếu sau khóa nhãn: 20/20 khớp vỡ khi giao, 7/8 khớp nguyên nhân; A035 chờ Vĩnh thống nhất; có giới hạn kiểm mù ghi rõ |
| Thử mô phỏng 10 phiên | Đã chạy `gemini-3.5-flash-lite`, 10/10 không lỗi, run `simulate-try@20261127-223433` | Lượt thử không tính bản nộp ≥50 phiên; /task thành công chờ eval đã chấm |
| Hẹn 2–3 người ngoài nhóm | Có lời mời và kịch bản 10 phút ở `validation/log.md` | Khoa xác nhận chưa có người ngày 27/11; chưa gửi lời mời hoặc có lịch hẹn |

## 2. Cách suy ra tần suất

Nguồn: `evidence/summary.md` mục 2 (Vĩnh) và cách đếm `evidence/count.py`:

```text
A5 = (205 đánh giá 1–2 sao / 18.566 tổng đánh giá) × (21 ca vỡ / 61 đánh giá xấu có chữ)
   ≈ 0.0038 ≈ 0.38%
```

Theo phân công, cấu hình dùng tỉ lệ **làm tròn 0.0038**. Số đơn/tháng của ba persona là *(tự ước tính)*: 100, 300, 800; tỷ lệ sử dụng sản phẩm trên mỗi ca vỡ giả định là 1. Suy ra 0.38, 1.14, 3.04 phiên/người/tháng. Giữ số thập phân: đó là kỳ vọng theo tháng, không phải số phiên bắt buộc phải nguyên.

Đây là kịch bản suy từ review, không phải dữ liệu quan sát tỷ lệ khiếu nại hay tỷ lệ dùng sản phẩm trên mọi đơn. Vĩnh chưa đo được thời gian/tiền mỗi ca; không tự bổ sung thành số khảo sát.

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

- Quân: duyệt §5 và thống nhất dùng cùng model/cấu hình giữa các lượt eval. Khoa đã chọn và thử được `gemini-3.5-flash-lite`; bản nhờ duyệt chưa có xác nhận gửi/nhận.
- Hiếu: chấm chính thức 30 output trong `eval/run-1.csv`; đối chiếu 5 nhãn với phiếu Khoa đã chốt ở `eval/second-review.md`. Run ID đã có `run-1@20261127-223619`; không mở phiếu của Khoa trước khi tự chốt nhãn.
- Khoa: tuyển 2–3 người ngoài nhóm đúng vai; chưa có ai xác nhận, không ghi người/lịch giả.
- Vĩnh: xem A035 ở bảng đối chiếu; giữ nguyên nhãn mỗi bên đến khi thống nhất, không sửa cho đủ độ khớp.

## 5. Kiểm tra đã thực hiện

- `python run.py check`: 30 câu, 10/30 data thật, 4 metric; không có cảnh báo.
- `python evidence/count.py`: chạy lại được A5 làm tròn 0.38% từ 9 sản phẩm và 61 đánh giá.
- Bộ đọc YAML của chính khung đọc được cấu hình, không có cảnh báo; 3 persona, share = 1, đủ 2 giá đúng bảng BTC.
- Sinh kế hoạch ngoại tuyến 10/50 phiên, seed 42 tái lập được và đủ 3 persona trong kế hoạch đầy đủ. Đây không phải mô phỏng đã gọi API; không tạo CSV kết quả để thay thế lượt thật.
- Kiểm nhãn 20 dòng không thay đổi so với bản đã lưu trước khi đối chiếu. §5, chuẩn §7, benchmark, metric và code khung giữ nguyên.
- Đã gọi API thật 10 phiên: tổng token vào 13.826 / ra 2.955, lỗi 0/10; file CSV/summary/trace được giữ nguyên. Lượt thử không có mẫu shop nhiều đơn, chưa coi là kết quả mô phỏng đầy đủ.
- Đã chạy bộ 30 câu qua API thật: 30/30 output, lỗi kỹ thuật 0, token vào 39.999 / ra 8.206, 29 lần gọi model. Hai nhánh thiếu/không tìm thấy mã không gọi model; một input nhiều đơn gọi 2 lần. Không điền pass chính thức trong CSV, chưa có tỉ lệ đạt cả bộ.
