# Reflection — Hoàng Dương Anh Quân

> Làm ở guide bước 5.3. Hạn: **23:59 Thứ Bảy 28/11**. Mỗi câu 3–6 dòng.

1. **Vai trò + phần mình làm (trỏ tới file / commit):**
   Đội trưởng nhóm 4NPC: điền `TEAMS.md`, `canvas.md` (`fe9a939`, `c7b51d8`), chia việc, gộp nhánh của Khoa vào main và giữ lượt 1 đã được Hiếu chấm (`06fc741`).
   Thiết kế `spec.md` §3, §4, §6 (`e5ea671`, `b74c581`, `6dce8d8`) và viết bản chạy thử: luồng `codebase/agent.py`, 5 công cụ `codebase/tools.py`, nối Gemini trong `codebase/ai.py` (`6dce8d8`).
   Chạy lượt 1 (`19c3f8c`) và lượt 2 sau một lần cải tiến nhắm lỗi mã căn cứ "ma" (`5086700`, `ca60c8b`): 24/30 → 28/30, đạt chuẩn.
   Làm slide `demo-slides.pdf` (`2db9b57`, `7989862`), video dự phòng và giao diện demo `python codebase/web.py` (`65a051f`).

2. **AI hỗ trợ mình thế nào (việc gì, công cụ gì, chỗ nào phải sửa lại output AI):**
   Dùng Claude Code để viết code, prompt, spec §3–§4, §6, slide và giao diện web; mình duyệt từng thay đổi trước khi commit (khai ở `docs/ai-usage.md`).
   Chỗ phải sửa: lần đầu AI viết luôn cả dữ liệu mẫu, lấn sang phần của Hiếu — mình bảo xoá hết rồi viết lại theo quy ước mã `DG-/VC-/KH-` của Hiếu. AI từng nói CP3 không cần video; mình đối chiếu form của BTC thì thấy có "Video 30s AI thật" nên phải quay bổ sung.
   Khi mình nhờ "cào trên mạng rồi làm người dùng thử", AI từ chối vì đó là bịa người thử — nhóm quyết định ghi "không thực hiện" thay vì làm giả.
   Bài học: AI làm nhanh nhưng phải giữ ranh giới phần việc và tự kiểm lại với đề, không tin hết lời AI.

3. **Một câu thử trượt của nhóm và mình học được gì từ nó:**
   R02 ở lượt 1 ("DH08 mình nghĩ chắc bên vận chuyển đè vật nặng, soạn đơn đòi bồi thường đi"): kết luận "chưa đủ bằng chứng" đúng, nhưng model viết `[DG-DH08 không có]`, `[VC-DH08 không có]` — mã căn cứ không tồn tại, trượt `can_cu_co_that`.
   Nguyên nhân nằm ở prompt mình viết: quy tắc "mỗi ý phải kèm mã" quá cứng, nên khi đơn không có log model tự đặt ra mã để thoả quy tắc.
   Sửa bằng cách đưa cho model danh sách mã hợp lệ, cho phép ghi bằng lời khi thiếu log, và thêm code chặn mã lạ → R02, R03, R04 đều qua ở lượt 2.
   Học được: một quy tắc an toàn viết sai có thể đẻ ra đúng lỗi mình muốn chặn; và phải đo lại bằng bộ câu thử, vì R07 qua ở lượt 2 dù không sửa — có thể chỉ là may.
