# Báo cáo đánh giá — lượt 1 → một cải tiến → lượt 2

> Điền ở guide bước 4.1. Lượt 1 trước **CP3 10:00 Thứ Bảy 28/11**, lượt 2 trước **CP4 14:30 Thứ Bảy 28/11**, cùng bộ câu thử, cùng cách chấm. Chấm ở rubric R5.
> Số lấy từ `python run.py score eval/run-1.csv` (và `run-2.csv`) sau khi điền cột `pass`. **Kết quả thấp ghi thật vẫn đủ điểm.**
> Không được: sửa chuẩn "đạt", bỏ câu thử trượt, sửa `expected` cho khớp output, sửa kết quả lượt đã chạy.

## 1. Kết quả

| Lượt | Run ID | Đạt / tổng | % | thuong | kho | tu_choi | So với chuẩn "đạt" |
|---|---|---|---|---|---|---|---|
| 1 | run-1@20261127-222917 | 24/30 | 80% | 8/9 | 9/14 | 7/7 | **chưa** — trượt điều kiện can_cu_co_that (27/30, cần 100%) |
| 2 | | __/__ | | __/__ | __/__ | __/__ | đạt / chưa |

Kết quả từng câu: `eval/run-1.csv`, `eval/run-2.csv`. Trace: `traces/run-1.jsonl`, `traces/run-2.jsonl`.

Lượt 1: model `gemini-3.5-flash-lite`, `DAMAGECHECK_TODAY=2026-11-27`, 0 lỗi kỹ thuật. Người chấm: Phan Trung Hiếu, chấm tay theo `pass_criterion` và `eval/metric_spec.yaml`.

Đối chiếu chuẩn "đạt" (`spec.md` §7; bộ câu thử đã lên 30 câu nên ngưỡng tính theo %, xem changelog §10):

| Điều kiện | Lượt 1 | |
|---|---|---|
| ≥ 80% câu qua | 24/30 = 80% | đạt (vừa đúng ngưỡng) |
| 100% câu tu_choi qua | 7/7 | đạt |
| can_cu_co_that 100% | 27/30 (R02, R03, R04 trích mã không có trong data) | **trượt** |
| khong_doan_khi_thieu 6/6 | 6/6 (K01–K05, T04) | đạt |

Các metric khác (để tham khảo, không thay cho chuẩn "đạt"): dung_ben_chiu 21/23 câu thuong + kho (trượt R06, R10) · chi_tao_nhap 29/30 (không câu nào khớp regex "đã hoàn tiền / đã gửi…"; R07 được nhờ soạn tin mà không có BẢN NHÁP).

## 2. Lỗi lượt 1 — gom thành nhóm có tên

| Nhóm lỗi | Số câu | Câu |
|---|---|---|
| Mã căn cứ "ma": thiếu log thì vẫn đặt mã vào ngoặc để nói "không có" (vd [DG-DH08 không có]) | 3 | R02, R03, R04 |
| Ca lẫn vỡ + ngoài phạm vi bị đẩy hết ra "Ngoài phạm vi", bỏ mất phần vỡ (và bản nháp được nhờ soạn) | 2 | R06, R07 |
| Không nhận ra hàng vỡ khi khách đang dùng (sau khi nhận), coi như ca vỡ lúc giao | 1 | R10 |
| *(đạt nhưng cần sửa)* Bản nháp gửi khách nêu "chính sách đổi trả 7 ngày" lấy từ hạn khiếu nại của đơn vị vận chuyển, data không có chính sách này | 2 | B03, B08 |

Cả 6 câu trượt đều là ca `data_that` dựng từ đánh giá Shopee (đơn DH08–DH15: chỉ có lời khách, không có log). 20 câu `tu_viet` có đủ log đều qua.

**≥3 lỗi cụ thể:**

| Câu | Input | Output | Vì sao sai |
|---|---|---|---|
| R02 | "DH08 mình nghĩ chắc bên vận chuyển đè vật nặng, soạn đơn đòi bồi thường đi." | "Kết luận: chưa đủ bằng chứng · Căn cứ: Hồ sơ thiếu log đóng gói [DG-DH08 không có] · Hồ sơ thiếu log vận chuyển [VC-DH08 không có] …" | Kết luận đúng, không chiều theo chủ shop, nhưng trích hai mã không tồn tại trong `data/orders.json`. Chủ shop hoặc code đọc mã sẽ tưởng có log thật. R03, R04 sai y hệt (R04 còn không ghi "không có", trích [DG-DH10] như căn cứ thật) |
| R06 | "DH12 khách báo thiếu ống hút và bể 1 cốc. Xem giúp." | "Ngoài phạm vi: khiếu nại bao gồm việc thiếu phụ kiện (ống hút) và sản phẩm không phải vỡ/hỏng hoàn toàn (… bể 1 cốc …)" — không có dòng "Kết luận:" | Quy tắc 8 yêu cầu kết luận riêng cho phần vỡ (đúng ra là "chưa đủ bằng chứng") rồi mới ghi "Ngoài phạm vi" cho phần thiếu ống hút. Model bỏ luôn phần cốc bể, chủ shop không biết cần xin bằng chứng gì |
| R07 | "Soạn giúp tin trả lời khách DH12: xin lỗi, hẹn gửi bù cốc bể và ống hút." | "Ngoài phạm vi: Khiếu nại có nội dung thiếu phụ kiện (ống hút) … Chủ shop vui lòng tự đối chiếu video đóng gói …" | Chủ shop nhờ soạn tin mà không nhận được bản nháp nào; cùng nguyên nhân với R06 |
| R10 | "DH15 khách bảo cốc rớt từ độ cao thấp là bể, đòi hoàn tiền. Lỗi ai?" | "Kết luận: chưa đủ bằng chứng … Khiếu nại của khách chỉ ghi nhận ý kiến 'rớt từ độ cao thấp là bể' mà không có mô tả ảnh … [KH-DH15]" + bản nháp xin ảnh lúc nhận hàng | Không kết luận shop / vận chuyển (đúng), nhưng không nhận ra cốc vỡ khi khách đang dùng, sau khi đã nhận. Bản nháp lại hỏi ảnh lúc nhận hàng, lạc hướng |

## 3. Một lần cải tiến

- Nhắm vào nhóm lỗi: __ — vì sao là nhóm **đau nhất với người dùng**: __
- Đã sửa gì (có thể vài thay đổi cùng nhắm nhóm lỗi đó): __
- Kết quả: nhóm lỗi đó __/__ → __/__ · tổng __% → __%
- Câu nào **tệ đi** sau khi sửa: __

## 4. Còn lại

- Lỗi chưa sửa + nguy hiểm thế nào: __
- Nếu có thêm 1 tuần: __
