# Bàn giao của Khoa — đã đồng bộ theo `main`

Cập nhật đêm 27/11/2026 sau khi Quân merge nhánh `khoa/cp3-personas-readiness`, Hiếu chấm xong `run-1@20261127-222917` (24/30) và Vĩnh hoàn tất `spec.md` §1–§2 + kiểm chéo `A035`.

## 1. Đã xử lý xong các điểm Quân, Hiếu, Vĩnh nhắn
- **Đồng bộ Run ID lượt 1 chính thức (`run-1@20261127-222917`):** Đã cập nhật toàn bộ `eval/second-review.md`, `eval/second-review-outputs.md`, `cost/README.md`, `cost/cost-estimate.md`, `spec.md` §8 và `docs/ai-usage.md` sang `run-1@20261127-222917` (bỏ tham chiếu `223619` làm lượt chính).
- **Trích 5 output (`B01, K02, R01, T02, T04`) của `run-1@20261127-222917` không kèm cột `pass`:** Đã đặt tại `eval/second-review-outputs.md` và để sẵn bảng trống trong `eval/second-review.md` để **Vĩnh** chấm độc lập (vì Khoa là người viết `spec.md` §5).
- **Đồng bộ số impact §2 & chi phí §8:** Đã cập nhật `cost/cost-estimate.md` mục 4 và `spec.md` §8 theo đúng bộ số chung với Vĩnh (10/50/100 shop; 100/300/800 đơn → 0,38 / 1,14 / 3,04 phiên/tháng; trung bình 1,14 ca/shop/tháng ≈ 34 phút + 57.000đ/shop/tháng so với chi phí AI thử nghiệm ~$0.0013/shop/tháng).
- **Kiểm chéo 20 dòng Bộ A (`evidence/kiem-cheo.md`):** Đã khớp với bản Vĩnh cập nhật (`vo_khi_giao` 20/20, `loi_do` 7/8, thống nhất `A035 = shop`).

## 2. Việc tiếp theo
- **Vĩnh:** Điền 5 dòng chấm độc lập (`B01, K02, R01, T02, T04`) trong `eval/second-review.md` (chỉ đọc output ở `eval/second-review-outputs.md`), sau đó đối chiếu với Hiếu để ghi `__/5` vào `eval/README.md` mục 3.
- **Quân & Hiếu (CP4):** Quân sửa prompt cho nhóm lỗi mã căn cứ "ma" (`R02–R04`) và ca lẫn (`R06–R07`), chạy lượt 2 (`eval/run-2.csv`), Hiếu chấm lượt 2 rồi báo Khoa chạy `python run.py simulate --rate-from eval/run-2.csv` (≥50 phiên).
- **Khoa:** Tuyển 2–3 người ngoài nhóm dùng thử 10 phút sáng/trưa 28/11 và chạy mô phỏng ≥50 phiên ngay khi có lượt 2.
