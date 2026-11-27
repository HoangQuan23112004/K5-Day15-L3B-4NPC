# Tổng hợp bằng chứng pain

> Điền ở guide bước 1.2, xong trước **CP3 10:00 Thứ Bảy 28/11**. Chấm ở rubric R1.
> Người làm: Ngô Chí Vĩnh. Chi tiết cách chọn mẫu, cách đếm, giới hạn: `evidence/data-mining.md`. Chạy lại mọi số: `python evidence/count.py`.

## 1. Nguồn đã dùng

| Nguồn | Đạt ngưỡng? | File |
|---|---|---|
| Đào data (x/N, %, cách đếm chạy lại được, ≥5 ví dụ) | ☑ **Bộ A** — đánh giá 1–2 sao công khai trên Shopee: 9 sản phẩm hàng dễ vỡ, **N = 61** đánh giá, cách chọn mẫu và cách đếm commit trước khi đọc, script `evidence/count.py` · ☑ **Bộ B** (nguồn thứ hai, kiểm lại Bộ A) — 20 review 1 sao mới nhất của app GHTK trên Google Play | `evidence/data-mining.md` · `evidence/shopee-products.csv` · `evidence/shopee-reviews.csv` · `evidence/app-reviews.csv` |
| Phỏng vấn (≥3 người ngoài nhóm, đúng người dùng) | ☐ Không làm — nhóm không liên hệ được chủ shop | — |
| Khảo sát (≥20 người ngoài nhóm, đúng người dùng) | ☐ Không làm — cùng lý do | — |

BTC không cấp data cho Track D. Theo guide 1.2 và file Track D, nhóm đào **review công khai**: Bộ A là lời người mua (kèm phản hồi của shop), Bộ B là lời người dùng app giao hàng, phần lớn là người gửi hàng.

## 2. Số chính

**Bộ A · Shopee** — 9 sản phẩm bán chạy của 4 nhóm hàng dễ vỡ (`ly thủy tinh` 3 · `bình gốm` 2 · `serum chai thủy tinh` 2 · `bánh quy hộp` 2), bỏ Shopee Mall; mỗi sản phẩm tối đa 10 đánh giá 1–2 sao có chữ; đánh giá viết từ 07/2022 đến 11/2026; xem ngày 27/11/2026.

| # | Đếm gì | x / N | % |
|---|---|---|---|
| A1 | Đánh giá 1–2 sao nói hàng **đến tay đã vỡ / móp / hỏng** (không tính vỡ khi đang dùng) | **21/61** | **34%** |
| | … theo nhóm hàng: serum chai thủy tinh 9/13 · bánh quy hộp 3/7 · bình gốm 4/11 · ly thủy tinh 5/30 | | |
| A2 | Trong 21 ca vỡ: người mua nói **do shop đóng gói** · do vận chuyển · không nói | 9 · **0** · 12 /21 | 43% · 0% · 57% |
| A3 | Trong 21 ca vỡ: shop đã / đề nghị hoàn tiền, gửi bù · shop không chịu (khách chịu) · không rõ | 4 · **6** · 11 /21 | 19% · 29% · 52% |
| A4 | Trong 10 ca vỡ shop có trả lời: phản hồi **nhắc tới khiếu nại / đòi bồi thường đơn vị vận chuyển** | **0/10** | **0%** |
| A6 | Trong 10 ca đó: phản hồi **đổ lỗi cho vận chuyển** | 5/10 | 50% |
| | … trong đó người mua nói do shop đóng gói, shop nói do vận chuyển (**hai bên đổ lỗi cho nhau**) | **3/10** | |
| A7 | Sản phẩm có mô tả của shop **cam kết tự đổi / hoàn khi hàng vỡ do vận chuyển** | 3/9 | 33% |
| A8 | Sản phẩm có mô tả **khuyên / bắt buộc quay video mở hàng** | 2/9 | 22% |
| A5 | Ước tính đánh giá nói hàng vỡ trên **mọi** đánh giá = 205/18.566 đánh giá 1–2 sao × A1 | — | 0,38% |

A5 dùng cho `spec.md` §2: với giả định mỗi đánh giá ≈ một đơn, một shop 300 đơn / tháng gặp khoảng **1 khiếu nại hàng vỡ / tháng** *(ước tính có giả định, xem giới hạn ở `evidence/data-mining.md` mục 5)*.

**Bộ B · Google Play, app GHTK** — 20 review 1 sao mới nhất có chữ (07–26/11/2026).

| # | Đếm gì | x / N | % |
|---|---|---|---|
| | Review do **người gửi hàng / shop** viết (nói tạo đơn, lấy hàng, COD, "các shop lưu ý"…) | 8/20 | 40% |
| B1 | Phàn nàn của người gửi hàng là về **hàng vỡ / hỏng** | **0/8** | 0% |
| | … phàn nàn của người gửi hàng là về lấy / giao chậm · phí, tiền COD | 5 · 3 /8 | |
| B2, B3 | Khi hàng vỡ / thất lạc có được đền không, vì sao | — | không có ca nào trong mẫu |
| B4 | Review nói **không liên hệ được CSKH / tổng đài** | 4/20 | 20% |

Phỏng vấn / khảo sát: không làm, nên không có bảng P1–P3.

## 3. ≥5 trích dẫn hoặc ví dụ nguyên văn (có nguồn, bỏ tên)

1. *"Nắp cốc bị nứt rất rõ, chẳng biết là do hàng lỗi trước hay do bên vận chuyển."* — người mua, đánh giá 1 sao, 08/2025, dòng `A028` (SP03 · ly thủy tinh)
2. Người mua: *"Nhận hàng cốc vỡ vụn… Shop bọc chống sốc thì mỏng"* · shop trả lời: *"chắc bên vận chuyển đè vật nặng lên ạ… e hỗ trợ gửi lại"* — 08/2024, dòng `A006` (SP01 · ly thủy tinh)
3. Người mua: *"khâu đóng gói ko chấp nhận được luôn, mua 5 hộp thì ko 1 hộp nào lành lặn"* · shop trả lời: *"do quá trình vận chuyển nên hàng mới vậy chứ không phải bên em giao hàng móp đâu ạ"* — 10/2025, dòng `A058` (SP09 · bánh quy hộp)
4. *"Mình mua 2 hộp 60que thì gãy vỡ hết 60que… Shop kêu thông cảm vì quá trình giao. Đúng ra là shop hàng ko nguyên vẹn thì shop pải bù bao nhiêu %…"* — người mua, 12/2025, dòng `A060` (SP09 · bánh quy hộp)
5. Shop trả lời: *"…Có thể trong quá trình vận chuyển, kiện hàng bị va đập hoặc chèn ép dẫn đến vỡ, móp. Anh/chị vui lòng nhắn Shop kèm ảnh hoặc clip, Shop sẽ kiểm tra ngay và đổi bù hoặc hoàn…"* — 01/2026, dòng `A048` (SP06 · serum chai thủy tinh)
6. Shop trả lời: *"…Shop có liên hệ qua phần chat để kiểm tra check cam, gửi bù hoặc hoàn tiền…"* — 10/2024, dòng `A030` (SP03 · ly thủy tinh)
7. Mô tả sản phẩm do shop viết: *"Hoàn tiền 100% nếu sản phẩm bị vỡ khi đến tay (khách quay video khui hàng để được hỗ trợ)… Không có video, shop không thể giải quyết."* — SP02 · ly thủy tinh, xem 27/11/2026
8. Người gửi hàng: *"…có đơn 20 ngày mới giao, có đơn khách không đợi được phải hủy… CSKH thì không cho nt hỗ trợ… các shop lưu ý khi gửi cái đơn vị ghtk"* — review 1 sao app GHTK, 16/11/2026, dòng `B017`

## 4. Các nguồn có khớp nhau không

- **Khớp — không ai có căn cứ để phân xử ca hàng vỡ.** Bộ A: khi hàng vỡ, người mua thường đổ cho đóng gói (9/21), shop có trả lời thì một nửa đổ cho vận chuyển (5/10), có 3 ca hai bên đổ lỗi cho nhau, và không bên nào đưa căn cứ. Shop phải dựa vào ảnh / video mở hàng của khách hoặc camera đóng gói của mình (`A030`, `A048`, mô tả SP02).
- **Khớp một phần — đòi bồi thường từ đơn vị vận chuyển hầu như không xuất hiện.** Bộ A: 0/10 phản hồi của shop nhắc tới việc khiếu nại vận chuyển, kể cả khi chính shop đổ lỗi cho vận chuyển. Bộ B gợi ý một lý do có thể: 4/20 review nói không liên hệ được CSKH / tổng đài. Đây chỉ là **gợi ý**, chưa kiểm được: Bộ B không có ca nào nói thẳng về đòi bồi thường hàng vỡ.
- **Lệch — với người gửi hàng, hàng vỡ không phải phàn nàn hàng đầu.** Bộ B: 0/8 phàn nàn của người gửi hàng là về hàng vỡ; họ than chủ yếu về lấy / giao chậm (5/8) và phí (3/8). Giải thích: (1) review app GHTK chấm cả dịch vụ và app nói chung, còn chậm và phí xảy ra với **mọi** đơn, hàng vỡ chỉ xảy ra với một phần nhỏ đơn hàng dễ vỡ; (2) Bộ A cho thấy hàng vỡ chỉ chiếm khoảng 0,4% đánh giá (A5) — hiếm, nhưng khi xảy ra thì gây tranh cãi. Hai nguồn vì vậy không mâu thuẫn: hàng vỡ là sự cố **ít khi xảy ra nhưng mỗi lần khó phân xử**, không phải nỗi đau thường ngày.

## 5. Kết luận

Giả thuyết ở `evidence/hypothesis.md`: **đúng một phần, phải đổi trọng tâm.**

- **Đúng:** hàng vỡ khi giao xuất hiện thường xuyên trong phàn nàn về hàng dễ vỡ (A1 = 21/61 = 34%, vượt ngưỡng ≥20% đặt trước), và không bên nào xác định được lỗi ở đâu (A2: 12/21 người mua không nói nguyên nhân; 3 ca hai bên đổ lỗi cho nhau). Shop không đi đòi bồi thường từ đơn vị vận chuyển (A4 = 0/10).
- **Chưa đạt / phải đổi:** ngưỡng "≥50% ca vỡ shop tự chịu" **không đạt**: chỉ 4/21 ca rõ là shop chịu, 6/21 là **khách chịu** (shop né, bảo "thông cảm vì quá trình giao"), 11/21 không rõ. Nên hậu quả không chỉ là "shop mất phần tiền đòi được", mà là **ai chịu thì tuỳ ai nói to hơn** — lúc shop mất tiền, lúc khách mất tiền và shop mất uy tín (đánh giá 1 sao). Bộ B không kiểm được lý do không đòi bồi thường (0 ca hàng vỡ trong mẫu).
- **Hàm ý cho lát cắt:** giữ trọng tâm "xác định bên chịu trách nhiệm dựa trên căn cứ", nhưng giá trị chính là **phân xử có căn cứ và nhanh** (đối chiếu đóng gói, vận chuyển, lời khách), không phải "đòi được nhiều tiền bồi thường hơn". Tần suất thấp (khoảng 1 ca / tháng / 300 đơn, ước tính) nên impact nằm ở **giá trị mỗi ca** hơn là số ca.

**Điều vẫn chưa biết:** mỗi ca mất bao nhiêu phút và bao nhiêu tiền của chủ shop · shop có thực sự khiếu nại đơn vị vận chuyển ngoài những gì viết trong phản hồi không · vì sao không khiếu nại · tình hình của shop bán ngoài sàn (Facebook / Zalo). Cần hỏi trực tiếp chủ shop — nhóm chưa làm được.

## Lịch hẹn (dùng cho CP2 — chỉ ghi vai và giờ, không tên)

Không có lịch hẹn: nhóm không liên hệ được chủ shop để phỏng vấn và BTC không cấp data cho Track D, nên nguồn bằng chứng là **đào data** đánh giá công khai (`evidence/data-mining.md`). Tiến độ lúc CP2: 3 sản phẩm, 30 đánh giá đã mã hoá.

| Vai | Giờ hẹn | Đã xong? |
|---|---|---|
| — (không phỏng vấn) | — | — |
