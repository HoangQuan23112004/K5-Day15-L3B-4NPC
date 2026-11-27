# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | | | | |
| Prompt / thiết kế lời gọi mô hình | | | | |
| Đào data (viết script đếm, gợi ý nhãn) | Claude Code | Đề xuất cách đếm (`evidence/data-mining.md` mục 1), viết `evidence/count.py`, chuyển đoạn đánh giá Vĩnh copy từ Shopee thành dòng CSV đã ẩn danh và **gợi ý nhãn** | Vĩnh tự chọn sản phẩm theo cách đếm, tự copy đánh giá, duyệt cách đếm trước khi đọc data; kiểm tay __ dòng nhãn, khớp __ *(điền sau khi kiểm)* | Ngô Chí Vĩnh |
| Rà câu hỏi phỏng vấn / khảo sát | Claude Code | Soạn kịch bản phỏng vấn, form khảo sát (cuối cùng không dùng vì không liên hệ được chủ shop) | Vĩnh đọc lại | Ngô Chí Vĩnh |
| Viết câu thử (benchmark) | | | Mỗi câu thử có `source`; câu thử AI viết được ghi rõ | |
| Sinh data `synthetic` (nếu có) | | | Seed __ · kiểm tay __ dòng | |
| Chấm cột `pass` bằng LLM (nếu có) | | | Kiểm tra thủ công __ câu thử, khớp __/__ | |
| Slide, văn bản | | | | |
| Kiểm chéo nhãn bằng chứng Bộ A | Codex | Đọc định nghĩa và 20 nội dung trong `evidence/kiem-cheo.md`, điền hai cột nhãn theo yêu cầu của Khoa; không mở CSV nhãn gốc trong lượt này | Chưa ghi nhận Khoa kiểm tay; Vĩnh chưa đối chiếu độ khớp. Codex đã thấy một số trích đoạn A006/A028 trong các lượt trước nên không coi là kiểm mù hoàn toàn | Lê Viết Khoa |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
