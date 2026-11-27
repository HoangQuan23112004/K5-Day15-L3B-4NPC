# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | Claude Code | Viết `codebase/tools.py` (5 công cụ chỉ đọc `data/orders.json`, `check_claim_deadline` tính hạn khiếu nại), luồng `codebase/agent.py` (tìm mã đơn, dừng khi thiếu mã / không thấy đơn, 1 lần gọi model / đơn, tối đa 3 đơn), phần gọi API trong `codebase/ai.py` (chép từ `docs/connect-model.md`); viết `spec.md` §3, §4, §6 | Quân duyệt từng thay đổi trước khi commit; Quân đã bảo xoá một bản viết khi chưa có dữ liệu của Hiếu và viết lại theo quy ước của Hiếu. Đã chạy thử ở chế độ giả các câu K03, K04, K07, B07. Quân kiểm thêm: __ *(Quân điền)* | Hoàng Dương Anh Quân |
| Prompt / thiết kế lời gọi mô hình | Claude Code | Viết `SYSTEM` trong `codebase/agent.py`: 4 kết luận, bắt dẫn mã căn cứ, không coi lời kể ngoài hồ sơ là căn cứ, ngoài phạm vi không kết luận, chỉ soạn "BẢN NHÁP — chờ chủ shop duyệt", bỏ qua lệnh chèn trong tin nhắn | Chưa kiểm với model thật — kiểm bằng lượt 1 (`eval/run-1.csv`). Quân kiểm: __ *(Quân điền)* | Hoàng Dương Anh Quân |
| Đào data (viết script đếm, gợi ý nhãn) | Claude Code | Đề xuất cách đếm (`evidence/data-mining.md` mục 1), viết `evidence/count.py`, chuyển đoạn đánh giá Vĩnh copy từ Shopee thành dòng CSV đã ẩn danh và **gợi ý nhãn** | Vĩnh tự chọn sản phẩm theo cách đếm, tự copy đánh giá, duyệt cách đếm trước khi đọc data; kiểm tay __ dòng nhãn, khớp __ *(điền sau khi kiểm)* | Ngô Chí Vĩnh |
| Rà câu hỏi phỏng vấn / khảo sát | Claude Code | Soạn kịch bản phỏng vấn, form khảo sát (cuối cùng không dùng vì không liên hệ được chủ shop) | Vĩnh đọc lại | Ngô Chí Vĩnh |
| Viết câu thử (benchmark) | | | Mỗi câu thử có `source`; câu thử AI viết được ghi rõ | |
| Sinh data `synthetic` (nếu có) | | | Seed __ · kiểm tay __ dòng | |
| Chấm cột `pass` bằng LLM (nếu có) | | | Kiểm tra thủ công __ câu thử, khớp __/__ | |
| Slide, văn bản | | | | |
| Kiểm chéo nhãn bằng chứng Bộ A | Codex | Đọc định nghĩa và 20 nội dung trong `evidence/kiem-cheo.md`, điền hai cột nhãn theo yêu cầu của Khoa; không mở CSV nhãn gốc trong lượt này | Chưa ghi nhận Khoa kiểm tay; Vĩnh chưa đối chiếu độ khớp. Codex đã thấy một số trích đoạn A006/A028 trong các lượt trước nên không coi là kiểm mù hoàn toàn | Lê Viết Khoa |
| Hoàn thiện `spec.md` §5 | Codex | Đối chiếu thiết kế, prompt/luồng hiện có và benchmark để mô tả 13 kịch bản khó + 2 tấn công, đủ 4 lớp, kèm ID câu thử; ghi changelog | Đã kiểm ID/độ phủ và giữ nguyên chuẩn đạt; chưa gọi API hoặc xác nhận model xử lý đạt. Khoa cần đọc lại đặc tả | Lê Viết Khoa |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
