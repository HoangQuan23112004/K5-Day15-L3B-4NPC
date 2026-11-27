# Kiểm chéo nhãn — Bộ A (đánh giá Shopee)

> Người gắn nhãn gốc: Ngô Chí Vĩnh (AI gợi ý, Vĩnh kiểm tay). Người kiểm chéo: **Lê Viết Khoa**. Không mở `evidence/shopee-reviews.csv` trong lượt gắn nhãn này.
> 20 dòng chọn ngẫu nhiên từ 61 dòng bằng `random.Random(42).sample` (chạy lại ra đúng 20 dòng này). Cách đếm đầy đủ: `evidence/data-mining.md` mục 1.
> Cách làm: sửa file này ngay trên GitHub (biểu tượng bút chì), điền 2 cột cuối, Commit. Mất khoảng 10 phút.

## Định nghĩa (chỉ dựa vào chữ trong cột "Nội dung")

- **Cột `vo_khi_giao`** — ghi `1` nếu người mua nói hàng **lúc đến tay / lúc mở hộp** đã vỡ, nứt, móp, hỏng. Ghi `0` nếu chê lý do khác (sai màu, sai cỡ, thiếu đồ, chất lượng, mùi vị…), **kể cả vỡ khi đang dùng** (rót nước nóng, bỏ đá, làm rơi).
- **Cột `loi_do`** — chỉ điền khi `vo_khi_giao = 1`: `shop` nếu người mua nói do shop đóng gói / shop gửi hàng hỏng · `vc` nếu người mua nói do vận chuyển · `?` nếu người mua không nói nguyên nhân. (Lời của shop ở sau dấu "· shop:" **không** tính là ý người mua.)

## Bảng điền

| Dòng | Nhóm hàng | Nội dung (tóm tắt đánh giá + phản hồi shop) | vo_khi_giao | loi_do |
|---|---|---|---|---|
| A002 | ly thủy tinh | pha cà phê nước nóng thì bể (vỡ khi dùng) | 0 | |
| A003 | ly thủy tinh | cốc nhựa bảo thủy tinh | 0 | |
| A006 | ly thủy tinh | nhận hàng cốc vỡ vụn, shop bọc chống sốc mỏng · shop: chắc bên vận chuyển đè vật nặng, sẽ gửi lại | 1 | shop |
| A007 | ly thủy tinh | đặt cốc 400ml mà dung tích chỉ như 330ml | 0 | |
| A008 | ly thủy tinh | 550ml mà giao như 300ml | 0 | |
| A009 | ly thủy tinh | shop gửi thiếu cái cọ | 0 | |
| A014 | ly thủy tinh | rớt từ độ cao thấp là bể (vỡ khi dùng) | 0 | |
| A015 | ly thủy tinh | đặt nắp tím giao nắp trắng | 0 | |
| A016 | ly thủy tinh | ảnh minh hoạ nắp tím mà nhận nắp hồng | 0 | |
| A018 | ly thủy tinh | mỏng dễ bể · shop: cốc thủy tinh làm rơi vỡ là bình thường | 0 | |
| A028 | ly thủy tinh | nắp cốc nứt rõ, chẳng biết do hàng lỗi trước hay do bên vận chuyển · shop: hỗ trợ hoàn tiền / bù tiền / voucher | 1 | ? |
| A035 | bình gốm | gửi hàng bể, sản phẩm như vậy cũng đem bán cho khách | 1 | shop |
| A038 | bình gốm | quảng cáo set 3 bình nhưng giao 1 bình | 0 | |
| A041 | bình gốm | hàng bị vỡ | 1 | ? |
| A044 | serum chai thủy tinh | gửi thiếu 2 nắp chai | 0 | |
| A048 | serum chai thủy tinh | nhận hàng bể nát chai serum · shop: có thể do vận chuyển va đập, nhắn kèm ảnh hoặc clip để đổi bù / hoàn | 1 | ? |
| A050 | serum chai thủy tinh | chai còn lại bị vỡ · shop: có thể do vận chuyển dù shop đã đóng gói kỹ | 1 | ? |
| A053 | serum chai thủy tinh | sao không đóng lẻ ra, giờ tính sao (không nói rõ vỡ) | 0 | |
| A058 | bánh quy hộp | mua 5 hộp không hộp nào lành lặn, đóng gói không chấp nhận được · shop: do quá trình vận chuyển, không phải bên em giao hàng móp | 1 | shop |
| A059 | bánh quy hộp | giao hàng bánh bể hết, không cây nào còn nguyên | 1 | ? |

## Ghi chú lượt kiểm chéo

- Nhãn điền theo chữ ở cột Nội dung; để trống `loi_do` khi `vo_khi_giao = 0`, đúng định nghĩa. Đây là nhãn lời đánh giá, không phải kết luận trách nhiệm thực tế.
- A028: người mua nêu hai khả năng và không xác định nguyên nhân nên ghi `?`. A048/A050: chỉ shop nhắc vận chuyển, không lấy lời đó làm ý người mua.
- A035: cách nói “sản phẩm như vậy cũng đem bán” được hiểu là người mua trách shop gửi sản phẩm hỏng. A041/A050 nói hàng/chai đã vỡ, không có dấu hiệu vỡ khi đang dùng nên ghi `1`; nội dung tóm tắt không nêu rõ thời điểm, cần trao đổi nếu hai bên hiểu khác.
- A018 chỉ nói dễ bể; A053 không nói rõ có hư hỏng nên ghi `0`, không suy từ lời shop hoặc thiếu thông tin ra hàng vỡ khi giao.
- Codex hỗ trợ soạn nhãn theo yêu cầu của Khoa,  Khoa kiểm tay. Trong các lượt làm việc trước, Codex đã thấy một số trích đoạn và diễn giải A006/A028 qua tài liệu/benchmark dự án; do đó lượt này **không phải kiểm mù hoàn toàn**, dù không mở file nhãn gốc trong lượt này. Chưa tính độ khớp với Vĩnh.

## Kết quả (Vĩnh điền sau khi so)

- `vo_khi_giao` khớp: __/20 · `loi_do` khớp: __/__
- Dòng lệch và cách xử lý: __
