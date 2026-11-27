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
| Kiểm chéo nhãn bằng chứng Bộ A | Codex | Đọc định nghĩa và 20 nội dung trong `evidence/kiem-cheo.md`, hỗ trợ soạn nhãn; sau khi lưu nhãn mới mở CSV gốc để tính đối chiếu | Khoa xác nhận kiểm tay trong bản `edc6213`. Tính so nhãn: 20/20 vỡ, 7/8 nguyên nhân, A035 chờ Vĩnh thống nhất; không đổi nhãn sau khi so. Codex đã thấy A006/A028 trong tài liệu trước nên không coi là kiểm mù hoàn toàn | Lê Viết Khoa |
| Hoàn thiện `spec.md` §5 | Codex | Đối chiếu thiết kế, prompt/luồng hiện có và benchmark để mô tả 13 kịch bản khó + 2 tấn công, đủ 4 lớp, kèm ID câu thử; ghi changelog | Đã kiểm ID/độ phủ và giữ nguyên chuẩn đạt; chưa gọi API hoặc xác nhận model xử lý đạt. Khoa cần đọc lại đặc tả | Lê Viết Khoa |
| Persona và giá CP3 | Codex | Suy phiên/tháng từ A5 của Vĩnh và số đơn giả định, ghi nhãn tự ước tính; đối chiếu 2 tầng giá với repo đề, cập nhật model Khoa chọn gemini-3.5-flash-lite | Có token thật từ 10 phiên try, lỗi 0; chưa có eval đã chấm để tính /task thành công, chưa kết luận giá trị kinh tế | Lê Viết Khoa |
| Chạy thử và tạo output lượt 1 | Codex chạy code của nhóm | Chạy 10 phiên thử bằng API và bộ 30 câu, giữ nguyên CSV/trace; ghi run ID, token và lỗi thực | Khoa cần kiểm hồ sơ; Hiếu chấm chính thức pass. Model thật, không dùng output giả, không sửa prompt/benchmark/metric | Lê Viết Khoa |
| Chấm độc lập 5 output và chuẩn bị dùng thử | Codex | Chọn trước 5 ID, đọc output run-1 khi pass còn trống, đề xuất 1/0 riêng trong phiếu; soạn lời mời/kịch bản 10 phút | Khoa đã đọc output thật, kiểm tay và chốt phiếu 5 output (`B01=1, K02=1, R01=0, T02=1, T04=1`); chờ Hiếu chấm xong để tính độ khớp `__/5`. Chưa có người thử/lịch hẹn | Lê Viết Khoa |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
