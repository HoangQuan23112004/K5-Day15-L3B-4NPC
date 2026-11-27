# DamageCheck — người dùng thử (bonus)

Người chuẩn bị: Lê Viết Khoa · 27/11/2026 · hạn CP4: 14:30 ngày 28/11.
**Trạng thái: đã có kịch bản và mẫu ghi; chưa có người được hẹn, chưa thực hiện phiên thử.** Không có trích dẫn hoặc kết quả quan sát để báo cáo.

## 1. Mục tiêu và người thử

Mời 2–3 người ngoài nhóm có vai trò chủ shop hoặc trực tiếp xử lý khiếu nại. Khoa tự tuyển/hẹn; chỉ ghi vai, không tên hay liên hệ trong repo. Nếu chưa tuyển được đúng vai, ghi rõ vai thay thế và giới hạn, không gọi đó là kiểm chứng với chủ shop thật.

Quan sát người thử có tìm được căn cứ, nhận ra khi thiếu bằng chứng và hiểu rằng đề xuất/tin nhắn chỉ là bản nháp chờ duyệt hay không. Phiên này không thay thế bằng chứng pain ở `evidence/` và không đủ để suy ra tần suất sử dụng cả tháng.

**Điều kiện trước khi thử:** Quân cung cấp bản agent/tools theo DamageCheck chạy được; hồ sơ synthetic `data/orders.json` truy cập được. Nếu chỉ thử mẫu màn hình, phải ghi rõ là prototype, chưa kiểm được hành vi AI thật.

## 2. Kịch bản khoảng 10 phút/người

| Nhịp | Phút dự kiến | Việc người điều phối làm |
|---|---:|---|
| Làm quen | 1 | Nói đang thử sản phẩm; xin phép ghi chú đã ẩn danh, không yêu cầu đưa hồ sơ khách thật |
| Bối cảnh | 1 | Hỏi vai trò và cách xử lý lần gần nhất; không giới thiệu trước đáp án hoặc tính năng |
| Giao việc | 1 | Giao ca A bên dưới và cho người thử tự thao tác, nói suy nghĩ nếu muốn |
| Quan sát | 5 | Làm ca A và B; không chỉ nút hay sửa đáp án hộ; đánh dấu lúc phải trợ giúp |
| Hỏi sau | 2 | Hỏi điểm chưa tin, việc vẫn phải tự kiểm và mức tiếc nếu không dùng nữa |

Đây là phân bổ thời gian dự kiến, không phải thời gian đã đo. Nếu chỉ kịp một ca, ghi đúng ca đã làm.

## 3. Việc giao — chỉ đọc cột đề bài cho người thử

Tất cả hồ sơ dưới đây là giả lập, không phải tranh chấp hay chính sách vận chuyển thật. Cột đối chiếu chỉ dành cho người điều phối; không đưa đáp án/benchmark vào prompt của sản phẩm.

| Ca | Đề bài giao theo kết quả | Điều cần quan sát | Đối chiếu cho người điều phối |
|---|---|---|---|
| A — đủ căn cứ | “Khách đơn DH01 báo bình bị vỡ. Hãy kiểm hồ sơ, quyết định bước tiếp theo và chuẩn bị nội dung bạn muốn gửi cho bên phù hợp.” | Có đọc căn cứ trước khi dùng kết luận? Có nhận ra bản nháp chưa được gửi? Cần sửa gì trước khi duyệt? | Theo B01/B04: dấu hiệu vận chuyển tại VC-DH01-2 và KH-DH01, log DG-DH01; đơn bồi thường nếu có chỉ là bản nháp |
| B — thiếu căn cứ | “Khách đơn DH04 báo lọ tinh dầu bể. Bạn cần quyết định có thể xử lý ngay chưa và cần thêm gì để chốt.” | Có chấp nhận dừng kết luận, hiểu thiếu gì và biết xin bổ sung bằng chứng? Có tưởng hệ thống đã thấy ảnh thật? | Theo K01: chưa đủ bằng chứng, yêu cầu thêm ảnh thùng/video mở hàng và dữ liệu đóng gói |
| C — dự phòng, mâu thuẫn | “Hãy xem DH05 và cho biết bạn có thể chốt bước xử lý chưa.” | Có hiểu mâu thuẫn giữa hồ sơ giao và mô tả ảnh? Có tự kiểm lại? | Theo K02: mâu thuẫn VC-DH05-3 và KH-DH05; chưa đủ bằng chứng |

Không bắt người thử làm đủ cả ba ca trong 10 phút. A và B là hai ca chính; C thay thế khi cần thử thêm chỗ khó.

## 4. Mẫu ghi trong từng phiên — điền sau khi có người thật

- Mã phiên: [chưa có] · ngày giờ: [chưa có] · người điều phối: [chưa có].
- Vai / mức kinh nghiệm / phù hợp người dùng mục tiêu: [chưa thu thập].
- Bản sản phẩm / model / ca đã giao: [chưa ghi].
- Thời điểm bắt đầu và kết thúc; thời gian chờ API; số lượt hỏi: [chưa đo].
- Thao tác đầu tiên / điểm do dự / chỗ hiểu sai / trợ giúp đã đưa: [chưa quan sát].
- Nội dung cần sửa trước khi duyệt; có hiểu chưa gửi/hoàn tiền không: [chưa quan sát].
- Trích nguyên văn sau khi bỏ thông tin nhận dạng: [chưa có].
- Kết quả công việc: hoàn thành / cần trợ giúp / chưa hoàn thành — [chưa đánh giá].

| Người thử (vai, mã phiên) | Việc giao | Quan sát cụ thể | Trích nguyên văn | Mức nghiêm trọng |
|---|---|---|---|---|

Bảng chưa có dòng kết quả. Thêm dòng sau mỗi phiên thực tế; không điền người giả để đủ số lượng.

Quy ước mức độ để phân loại sau khi quan sát:

- **Cao:** hiểu sai bản nháp thành đã gửi/hoàn tiền, hoặc dựa vào kết luận không đủ căn cứ để ra quyết định tiền bạc.
- **Vừa:** không biết xin thêm gì, không tìm được căn cứ hoặc cần người hướng dẫn mới hoàn thành.
- **Thấp:** câu chữ/hiển thị gây vướng nhưng vẫn tự hoàn thành đúng việc.

## 5. Câu hỏi sau và tổng hợp

Hỏi: “Bạn cần kiểm lại điều gì trước khi dùng đề xuất này?”; “Chỗ nào khó hiểu hoặc khiến bạn chưa tin?”; “Nếu mai không được dùng nữa, bạn thấy rất tiếc / hơi tiếc / không sao?”

- Rất tiếc / hơi tiếc / không sao: **chưa thu thập**, không ghi 0/0/0 như kết quả khảo sát.
- Số người đã thử: **chưa có phiên thực tế**.
- Chủ đề lặp nhiều nhất và mã phiên làm căn cứ: [chờ dữ liệu].
- Sửa gì trước demo, ai phụ trách, trỏ `spec.md` §10: [chờ quan sát].
- Giữ gì và vì sao / để dành sau: [chờ quan sát].

Sau phiên, ghi hành vi trước lời khen. Nếu chỉ nhận lời khen chung, giao việc cụ thể hơn để quan sát; không suy ra sản phẩm hữu ích từ lời khen.

## 6. Tuyển người và lời mời nháp — chưa gửi

Khoa xác nhận ngày 27/11 hiện **chưa có người dùng thử**. Chưa có người nhận/kênh liên hệ hoặc lịch nào được xác nhận. Khung dưới đây chỉ là đề xuất để Khoa hỏi người ngoài nhóm, không phải cuộc hẹn đã đặt:

| Vai ưu tiên | Khung đề xuất, giờ Việt Nam | Trạng thái |
|---|---|---|
| Chủ shop bán hàng dễ vỡ | 28/11 08:30–08:40 | Chưa có người nhận / chưa gửi / chưa xác nhận |
| Người trực tiếp xử lý khiếu nại của shop | 28/11 09:00–09:10 | Chưa có người nhận / chưa gửi / chưa xác nhận |
| Chủ shop online khác ngoài nhóm | 28/11 11:30–11:40 | Chưa có người nhận / chưa gửi / chưa xác nhận |

**Lời mời nháp:**

> Chào anh/chị, nhóm em đang làm bản thử DamageCheck hỗ trợ shop đối chiếu hồ sơ khi khách báo hàng vỡ/hỏng. Anh/chị có thể dành khoảng 10 phút sáng hoặc trưa 28/11 để thử 2 tình huống giả lập và góp ý chỗ khó hiểu không ạ? Không cần đưa thông tin khách hay đơn thật. Nhóm chỉ ghi chú thao tác/phản hồi đã ẩn danh nếu anh/chị đồng ý. Anh/chị tiện khung giờ nào ạ?

Chỉ sau khi người thật đồng ý mới ghi vai, mã phiên và giờ đã xác nhận. Thông tin liên hệ giữ ngoài repo. Nếu dùng bản giả/prototype phải nói rõ; không dùng phản hồi để kết luận AI thật đã làm đúng.
