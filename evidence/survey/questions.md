# Khảo sát — chủ shop online xử lý khiếu nại hàng vỡ / hỏng

> Người soạn: Ngô Chí Vĩnh. Chép sang Google Form. Hỏi về hành vi **đã xảy ra**, không hỏi "có thích không".
> Ngưỡng: ≥20 người ngoài nhóm, đúng người dùng (tự bán online, tự xử lý khiếu nại). Không thu tên, email, SĐT, tên shop (trừ câu 10 nếu người trả lời tự để lại).

- Kênh gửi: ____ (tên group / kênh, không ghi link cá nhân)
- Giờ mở: ____ · giờ chốt: ____
- Kết quả: `results.csv` (đã xoá mọi cột nhận ra người trả lời; bản gốc không commit)

## Câu hỏi

| # | Câu hỏi | Kiểu trả lời |
|---|---|---|
| 1 | Bạn có tự bán hàng online và tự trả lời khách khi khách báo hàng có vấn đề không? | Có, tôi là chủ shop · Có, tôi là nhân viên trực chat của shop · Không *(chọn "Không" thì kết thúc form)* |
| 2 | Shop bán chủ yếu qua kênh nào? | Chọn nhiều: Facebook · Zalo · Shopee · TikTok Shop · Lazada · Website riêng · Khác |
| 3 | Mỗi tháng shop gửi khoảng bao nhiêu đơn? | Dưới 100 · 100–500 · 500–1.000 · Trên 1.000 |
| 4 | Lần gần nhất khách báo hàng đến tay bị vỡ / hỏng là khi nào? | Trong tuần này · Trong tháng này · 1–3 tháng trước · Lâu hơn 3 tháng · Chưa bao giờ *(chọn "Chưa bao giờ" thì nhảy tới câu 10)* |
| 5 | Trong 1 tháng qua, shop nhận khoảng bao nhiêu khiếu nại hàng vỡ / hỏng? | Số (không nhớ thì ghi "không nhớ") |
| 6 | Lần gần nhất đó, bạn đã xem gì để biết lỗi do ai? | Chọn nhiều: Video / ảnh đóng gói của shop · Ảnh / video khách gửi · Trạng thái, ghi chú của đơn vị vận chuyển · Hỏi shipper · Không xem gì, xử lý luôn · Khác |
| 7 | Lần đó xử lý mất bao lâu (từ lúc khách báo đến lúc chốt cách xử lý)? | Dưới 15 phút · 15–30 phút · 30–60 phút · Hơn 1 giờ · Kéo dài nhiều ngày |
| 8 | Cuối cùng ai chịu tiền ở lần đó? | Shop tự chịu (hoàn tiền / gửi bù) · Đơn vị vận chuyển bồi thường · Khách chịu · Chia nhau · Đang chờ / chưa xong |
| 9 | Lần đó bạn có gửi yêu cầu bồi thường cho đơn vị vận chuyển không? Nếu không, vì sao? | Có, được bồi thường · Có, bị từ chối / chưa có kết quả · Không, vì giá trị nhỏ không đáng · Không, vì thiếu bằng chứng · Không, vì không kịp hạn / không biết thủ tục · Không, vì sàn tự xử lý · Khác (ghi rõ) |
| 10 | Điều gì khó chịu nhất ở lần xử lý đó? | Đoạn văn |
| 11 | (Tuỳ chọn) Bạn có sẵn lòng cho nhóm hỏi thêm 10 phút không? | Có, cách liên hệ (không bắt buộc) · Không |

## Cách đọc kết quả (viết trước khi có kết quả)

- Mẫu số chính = số người trả lời **"Có" ở câu 1** (đúng người dùng). Người chọn "Không" không tính.
- Số 1: người có ≥1 khiếu nại trong 1 tháng qua (câu 4 = "tuần này" hoặc "tháng này") / mẫu số chính.
- Số 2: người **không** gửi yêu cầu bồi thường ở lần gần nhất (câu 9 bắt đầu bằng "Không") / người có ít nhất một lần (câu 4 ≠ "Chưa bao giờ").
- Số 3: phân bố lý do ở câu 9, dùng để kiểm 3 cách giải thích khác trong `evidence/hypothesis.md`.
- Số 4: trung vị số lần / tháng (câu 5) và thời gian xử lý (câu 7), dùng cho bảng impact ở `spec.md` §2 và persona ở `cost/personas.yaml`.
- Dưới khoảng 10 người thì chỉ ghi x/n, không ghi %.
