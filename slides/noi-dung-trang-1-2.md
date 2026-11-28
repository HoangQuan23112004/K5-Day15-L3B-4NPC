# Nội dung slide trang 1–2 (Vĩnh soạn, Khoa ghép vào `demo-slides.pdf`)

> Luật slide: mỗi trang ≥1 con số / trích dẫn có nguồn. Mọi số dưới đây truy được về `evidence/summary.md`, `spec.md` §1–§2, chạy lại bằng `python evidence/count.py`.
> Người nói trang 1–2: **Ngô Chí Vĩnh** (~1 phút / trang).

---

## Trang 1 · Người dùng & pain

**Tiêu đề:** Hàng vỡ đến tay khách — không ai biết lỗi ở đâu

**Ai · việc gì:** Chủ shop online nhỏ bán hàng dễ vỡ (ly thủy tinh, bình gốm, chai serum, bánh hộp) phải quyết **ai chịu** khi khách báo hàng vỡ.

**3 con số** (đánh giá 1–2 sao công khai trên Shopee, 9 sản phẩm, N = 61):
- **21/61 (34%)** đánh giá xấu nói hàng **đến tay đã vỡ / hỏng**
- **3/10** ca có shop trả lời: **hai bên đổ lỗi cho nhau** — khách nói đóng gói, shop nói vận chuyển, không ai có căn cứ
- **0/10** phản hồi của shop nhắc tới **đòi bồi thường** đơn vị vận chuyển · **6/21** ca **khách phải chịu**

**Trích dẫn (chọn 1, to giữa trang):**
> *"Nắp cốc bị nứt rất rõ, chẳng biết là do hàng lỗi trước hay do bên vận chuyển."* — đánh giá 1 sao, 08/2025 (`A028`)

**Hình gợi ý:** ảnh chụp 1 đánh giá hàng vỡ trên Shopee (đã **che tên người mua** và tên shop) đặt cạnh câu trả lời của shop *"chắc bên vận chuyển đè vật nặng"* (`A006`).

**Chân trang (nguồn):** Bộ A: Shopee, 9 sản phẩm × ≤10 đánh giá 1–2 sao, xem 27/11/2026 · nguồn thứ hai: 20 review 1 sao app GHTK (Google Play) · nhãn kiểm chéo 20/20 · `evidence/summary.md`

**Lời nói (~45 giây):**
"Người dùng của nhóm là chủ shop online nhỏ bán đồ dễ vỡ. Khi khách báo hàng vỡ, họ phải quyết ai chịu tiền. Nhóm đọc 61 đánh giá xấu trên Shopee của 9 sản phẩm dễ vỡ: 34% là hàng đến tay đã vỡ. Và không ai có căn cứ — có ca khách nói do shop đóng gói, shop nói do vận chuyển. Kết cục tùy ai nói to: 6 trên 21 ca khách phải tự chịu, và không shop nào nhắc tới việc đòi bồi thường bên vận chuyển. Chính một khách viết: *'chẳng biết là do hàng lỗi hay do vận chuyển'*."

---

## Trang 2 · Vì sao chọn bài này

**Tiêu đề:** Chọn "phân xử có căn cứ" — không phải hướng to nhất, mà hướng cần AI và làm kịp

**Bảng rút gọn:**

| Hướng | Bằng chứng | Chọn? |
|---|---|---|
| **1. Phân xử ai chịu khi hàng vỡ** | 21/61 đánh giá xấu là hàng vỡ · ~1,14 ca / shop / tháng | **Chọn** — cần phán đoán trên căn cứ, làm kịp |
| 2. Giục đơn lấy / giao chậm | 5/8 phàn nàn của người gửi hàng (GHTK) | Loại — cần dữ liệu hành trình thật của hãng, không có quyết định cho AI |
| 3. Kiểm phí ship, đối soát COD | 3/8 phàn nàn của người gửi hàng | Loại — là phép tính, làm bằng code |
| 4. Soạn trả lời đánh giá xấu | 33/61 đánh giá xấu có shop trả lời | Loại — đổi câu chữ, không đổi được ai chịu tiền |

**Impact / shop / tháng:** ≈ **1,14 ca × (30 phút + 50.000đ) ≈ 34 phút + 57.000đ** *(30 phút và số đơn / tháng: tự ước tính; 50.000đ: trung vị giá 9 sản phẩm trong mẫu; 0,38% ca vỡ / đơn: từ data)*

**Một dòng thật thà (để cuối trang):** Bằng chứng làm nhóm **đổi trọng tâm**: ban đầu nghĩ giá trị là "đòi được bồi thường", data cho thấy shop không đi đòi (0/10) và khách cũng hay chịu thiệt (6/21) → giá trị là **phân xử nhanh, có căn cứ**.

**Chân trang (nguồn):** `spec.md` §2 · `evidence/summary.md` mục 4–5

**Lời nói (~45 giây):**
"Từ chính bằng chứng, nhóm thấy 4 hướng. Shop than nhiều nhất về giao chậm và phí, nhưng hai việc đó hoặc cần dữ liệu của hãng mà nhóm không có, hoặc chỉ là phép tính. Hướng nhóm chọn là phân xử ai chịu khi hàng vỡ — hướng duy nhất cần AI phán đoán trên căn cứ, và làm kịp. Mỗi shop gặp khoảng 1 ca một tháng, mỗi ca tốn khoảng nửa tiếng và 50 nghìn tiền hàng. Bằng chứng cũng làm nhóm đổi trọng tâm: không phải giúp shop đòi tiền, mà giúp phân xử có căn cứ để không ai chịu oan."
