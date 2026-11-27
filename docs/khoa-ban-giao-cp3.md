# Bàn giao của Khoa — chờ Quân/Hiếu duyệt

Ngày 27/11/2026. **Nội dung nhờ duyệt được soạn sẵn; chưa có xác nhận đã gửi Quân hoặc đã được duyệt.** Không tự tạo bình luận/nhắn tin dưới tên người khác.

## Bản nhờ Quân duyệt

Quân xem giúp spec §5 đã có ở commit `607f8a6`: 13 kịch bản khó + T04/T05, đủ 4 lớp, mỗi dòng dẫn ID benchmark. Đây là hành vi mong muốn, chưa phải kết quả model đạt. Nhờ Quân xác nhận nội dung khớp luồng/prompt §4 và các đường đi §6.

Persona đã đổi theo A5 của Vĩnh ≈0,38%: 100/300/800 đơn mỗi tháng (tự ước tính) → 0,38/1,14/3,04 phiên; share 0,5/0,3/0,2. Số shop 10/50/100 và tỷ lệ mọi ca vỡ đều dùng sản phẩm là tự ước tính. Khoa đã gửi [repo đề](https://github.com/VinUni-AI20k/K5-L3-Day15-AI-Product-Hackathon), giá hai tầng Nhỏ/Lớn trong YAML đã khớp bảng chung BTC. Khoa chọn `gemini-3.5-flash-lite`, đã chạy 10 phiên thử API thật không lỗi, run `simulate-try@20261127-223433`; tổng token 13.826 vào / 2.955 ra, chi phí trung bình thử $0.0012/phiên. Quân cần thống nhất model/ngày cố định cho lượt 2. Không gửi key qua tài liệu.

## Bàn giao cần nhận từ Hiếu

Đã tạo `eval/run-1.csv` và `traces/run-1.jsonl`, run `run-1@20261127-223619`, model `gemini-3.5-flash-lite`, `DAMAGECHECK_TODAY=2026-11-27`. Đủ 30 output, lỗi kỹ thuật 0; 30 ô pass để trống. Nhờ Hiếu chấm chính thức cả bộ và cập nhật score/report. Khoa đã kiểm tay và chốt phiếu 5 câu B01, K02, R01, T02, T04 ở `eval/second-review.md` (`B01=1, K02=1, R01=0, T02=1, T04=1`). Hiếu tự chốt nhãn trước khi mở phiếu để giữ độc lập. Chưa có số khớp hai người hoặc tỉ lệ đạt cả bộ.

Khoa có đóng góp §5; nhờ nhóm xác nhận điều kiện “không phải người viết spec” đối với người chấm thứ hai. Giữ nguyên metric, expected và chuẩn đạt đã chốt.

## Kiểm chéo bằng chứng

Hai cột nhãn 20 dòng đã được điền và Khoa xác nhận kiểm tay ở `edc6213`. Sau đó mới mở CSV nhãn gốc để tính đối chiếu: vỡ khi giao khớp 20/20; nguyên nhân khớp 7/8 trên các dòng cả hai cùng ghi có vỡ. A035: Khoa ghi shop, Vĩnh ghi ?, cần Vĩnh trao đổi; chưa sửa nhãn để tăng khớp. Lượt này có giới hạn kiểm mù đã khai báo trong bảng, không phải bằng chứng một lượt độc lập hoàn toàn.

## Người dùng thử

Khoa xác nhận hiện chưa có người thử. `validation/log.md` có lời mời nháp và kịch bản 10 phút; giờ đề xuất không phải lịch đã hẹn. Cần 2–3 người ngoài nhóm, ưu tiên đang bán online hoặc trực tiếp xử lý khiếu nại.

## Phần còn chờ sau lần chạy này

- Hiếu chấm lượt 1 rồi đối chiếu với phiếu 5 câu Khoa đã khóa ở `eval/second-review.md` để ghi độ khớp `__/5` vào `eval/README.md` mục 3.
- Quân duyệt §5; sau chấm lượt 1, nhận nhóm lỗi để cải tiến và chạy lượt 2 cùng model/ngày. Nhãn nháp có ví dụ mã căn cứ không tồn tại, chưa tự sửa prompt để tránh làm mất mốc lượt 1.
- Hiếu bàn giao lượt 2 đã chấm; lúc đó Khoa chạy ≥50 phiên với `--rate-from` đúng lượt để có chi phí/task thành công cho CP4. Không dùng nhãn nháp 5 câu làm tỉ lệ đạt cả bộ.
- Vĩnh/Khoa thống nhất A035 và bổ sung impact/ca nếu có nguồn; team giới thiệu 2–3 người dùng thử.

Tin nhắn ngắn để Khoa gửi team: `docs/tin-nhan-team-cp3.txt`. Chưa tự gửi tin cho ai.
