# Tóm tắt mô phỏng simulate-1@20261127-234357

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| shop_it_don | 26 | 1 | 1587 | 254 | 1.0 | 4.8 |
| shop_vua_don | 14 | 1 | 1535 | 254 | 0.9 | 4.6 |
| shop_nhieu_don | 10 | 1 | 1144 | 166 | 0.7 | 3.6 |

Tỉ lệ đạt dùng để tính: 28/30 (93%) — lượt run-2@20261127-230337

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-2.csv (--rate-from).

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (10 người) | Chi phí / tháng — cơ sở (50 người) | Chi phí / tháng — cao (100 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gemini-3.5-flash-lite (vào 0.3 · ra 2.5 $/1M) | $0.0010 | $0.0011 | $0.0011 | $0.0105 | $0.0524 | $0.1048 | $0.0010 |
| gemini-4-hydrogen (vào 1.5 · ra 7.5 $/1M) | $0.0040 | $0.0043 | $0.0043 | $0.0406 | $0.2029 | $0.4057 | $0.0041 |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.0) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: gemini-3.5-flash-lite. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 0/50.
