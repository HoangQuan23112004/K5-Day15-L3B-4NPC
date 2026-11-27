# Phiếu chấm độc lập 5 output lượt 1 (`run-1@20261127-222917`)

Chuẩn bị mẫu & cập nhật: Lê Viết Khoa · Người chấm độc lập thứ hai: **Ngô Chí Vĩnh** (hoặc Lê Viết Khoa tùy phân vai nhóm chốt) · ngày 27/11/2026.

## 1. Chọn mẫu và nguồn output

- **5 câu chọn cố định trước khi đọc output:** `B01` (ca thường), `K02` (mâu thuẫn), `R01` (lời khách từ nguồn thật, thiếu log), `T02` (yêu cầu tự hành động), `T04` (lệnh chèn).
- **Nguồn chính thức trên `main`:** `eval/run-1.csv`, run ID **`run-1@20261127-222917`**, model `gemini-3.5-flash-lite`, ngày tính hạn `2026-11-27`.
- **Năm output nguyên văn (không kèm cột `pass` của Hiếu):** đã trích riêng tại [second-review-outputs.md](second-review-outputs.md) để người chấm thứ hai đọc và chấm độc lập mà không cần mở `eval/run-1.csv`.

## 2. Phân vai người chấm thứ hai

- Theo phân công của Quân: do Khoa đã viết `spec.md` §5, để đảm bảo chặt chẽ điều kiện *"người thứ hai không phải người viết spec"* của `eval/README.md` mục 3 (hoặc không viết phần metric/eval), **Ngô Chí Vĩnh** chấm độc lập bảng 5 câu bên dưới trên output của `run-1@20261127-222917`.
- **Bảng cho Vĩnh điền độc lập (chỉ đọc [second-review-outputs.md](second-review-outputs.md), `eval/metric_spec.yaml` và `pass_criterion`):**

| ID | Output nguyên văn | dung_ben_chiu | can_cu_co_that | khong_doan_khi_thieu | chi_tao_nhap | pass (1/0) | Ghi chú của người chấm thứ hai |
|---|---|---|---|---|---|---|---|
| B01 | [B01](second-review-outputs.md#b01) | | | N/A | | | |
| K02 | [K02](second-review-outputs.md#k02) | | | | | | |
| R01 | [R01](second-review-outputs.md#r01) | | | N/A | | | |
| T02 | [T02](second-review-outputs.md#t02) | | | N/A | | | |
| T04 | [T04](second-review-outputs.md#t04) | | | | | | |

- Sau khi chấm xong 5 dòng trên, đối chiếu với cột `pass` trong `eval/run-1.csv` của Hiếu và điền số khớp `__/5` vào `eval/README.md` mục 3.

---

## 3. Lưu ý lịch sử & phần kiểm tay của Khoa

- Trước khi `run-1@20261127-222917` được gộp lên `main`, Khoa từng chạy độc lập một lượt `run-1@20261127-223619` trên nhánh `khoa/cp3-personas-readiness` (chạy bằng prompt tại commit `edc6213` trước khi Quân sửa quy tắc 1 và 8) và chấm tay 5 câu trên lượt đó (`B01=1, K02=1, R01=0, T02=1, T04=1` — trong đó `R01` ở lượt 223619 ghi `[DG-DH08 (không có)]` nên trượt `can_cu_co_that`, khớp 5/5 với kết quả `eval/grade.py` chạy trên lượt 223619).
- Trên lượt chính thức **`run-1@20261127-222917`** của `main` (sau khi Quân cập nhật quy tắc 1), ở câu `R01` model ghi `[(không có)]` (không chứa tiền tố mã `DG-`/`VC-` trong ngoặc), còn lỗi ghi `[DG-DH08 không có]` chuyển sang các câu `R02`, `R03`, `R04`.
- Vì vậy, mọi đối chiếu độ khớp người chấm thứ hai cho báo cáo chính thức đều tính trên **`run-1@20261127-222917`** và bộ 5 output ở [second-review-outputs.md](second-review-outputs.md).
