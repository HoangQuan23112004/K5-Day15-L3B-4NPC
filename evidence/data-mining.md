# Đào data — cách đếm và kết quả

> Điền ở guide bước 1.2. Ôn lại: ngày 2, ngày 6 · lab ngày 2, lab ngày 6.
> Script đếm: `evidence/count.py` — chạy `python evidence/count.py` ra đúng các số ở mục 3.
> Repo chỉ chứa số đã tổng hợp và bảng mã hoá đã ẩn danh (`evidence/shopee-reviews.csv`, `evidence/seller-posts.csv`): không tên người mua, tên shop, tên tài khoản, link cá nhân.
> Người làm: Ngô Chí Vĩnh. Đọc tay, không dùng công cụ cào tự động.

## 1. Cách đếm — viết TRƯỚC khi chạy (viết lúc 17:45 Thứ Sáu 27/11/2026, trước khi đọc dòng data đầu tiên)

Hai bộ data bổ sung cho nhau. **Bộ A** (người mua + phản hồi của shop) cho biết hàng vỡ xảy ra và ai chịu tiền. **Bộ B** (người bán tự kể) cho biết shop có đòi bồi thường từ đơn vị vận chuyển không, và vì sao không đòi.

### Bộ A · Đánh giá 1–2 sao trên Shopee → `evidence/shopee-reviews.csv`

- **Chọn sản phẩm (cố định trước):**
  - 4 từ khoá: `ly thủy tinh` · `bình gốm` · `serum chai thủy tinh` · `bánh quy hộp`.
  - Mỗi từ khoá: tìm trên Shopee, sắp xếp "Bán chạy", lấy **5 sản phẩm đầu tiên** (bỏ qua Shopee Mall và sản phẩm không có đánh giá 1–2 sao) → 20 sản phẩm.
  - Mỗi sản phẩm: lọc "1 sao" rồi "2 sao", đọc **tối đa 10 đánh giá có chữ mới nhất** → tối đa 200 đánh giá.
- **Mã hoá mỗi đánh giá** (1 = có · 0 = không · `?` = không rõ):
  - `nhac_vo_hong`: đánh giá nói hàng đến tay bị vỡ, nứt, móp, chảy, hỏng (0 nếu chê vì lý do khác).
  - `do_van_chuyen` (chỉ khi `nhac_vo_hong` = 1): 1 = người mua nói / ngụ ý do vận chuyển (hộp móp, shipper quăng…); 0 = do shop đóng gói sơ sài; `?` = không rõ.
  - `shop_phan_hoi`: shop có trả lời đánh giá.
  - `shop_chiu` (chỉ khi `nhac_vo_hong` = 1): người mua hoặc shop cho thấy shop đã hoàn tiền / gửi bù / đổi hàng.
  - `shop_nhac_van_chuyen` (chỉ khi `nhac_vo_hong` = 1 và `shop_phan_hoi` = 1): phản hồi của shop nhắc tới việc khiếu nại / làm việc với đơn vị vận chuyển.
- **Mẫu số:**
  - A1: `nhac_vo_hong = 1` / **mọi đánh giá 1–2 sao có chữ đã đọc**.
  - A2: `do_van_chuyen = 1` / số đánh giá có `nhac_vo_hong = 1`.
  - A3: `shop_chiu = 1` / số đánh giá có `nhac_vo_hong = 1`.
  - A4: `shop_nhac_van_chuyen = 1` / số đánh giá có `nhac_vo_hong = 1` **và** `shop_phan_hoi = 1`.

### Bộ B · Bài người bán tự kể chuyện hàng vỡ / bồi thường → `evidence/seller-posts.csv`

- **Nguồn và cách tìm (cố định trước):**
  - Từ khoá: `shipper làm vỡ hàng` · `đòi bồi thường hàng vỡ` · `đơn vị vận chuyển không bồi thường` · `hàng vỡ shop chịu`.
  - Nơi tìm: Google (mỗi từ khoá đọc **30 kết quả đầu**) và ô tìm kiếm của các group / diễn đàn người bán công khai mà nhóm vào được (mỗi từ khoá đọc **20 bài đầu**). Ghi tên group / diễn đàn đã dùng vào mục 2.
  - Chỉ lấy bài đăng trong **24 tháng gần nhất** (từ 11/2024). Bài trùng (cùng một câu chuyện đăng lại) chỉ tính một lần.
- **Mã hoá mỗi bài / bình luận:**
  - `nguoi_ban_ke` = 1 nếu người viết là **người bán** kể một ca hàng của mình bị vỡ / hỏng khi giao; 0 nếu là người mua, quảng cáo, tin tức, hỏi chung chung.
  - `ket_qua` (chỉ khi `nguoi_ban_ke` = 1): `tu_chiu` (shop tự hoàn / gửi bù, không đòi) · `doi_duoc` (được bồi thường toàn bộ / một phần) · `bi_tu_choi` (đòi nhưng bị từ chối / treo) · `?` (không kể kết quả).
  - `ly_do` (chỉ khi `ket_qua` là `tu_chiu` hoặc `bi_tu_choi`): `thieu_bang_chung` · `gia_tri_nho` · `qua_han` · `thu_tuc_phuc_tap` · `san_xu_ly` · `khac` · `?`.
- **Mẫu số:**
  - B1: số bài có `ket_qua` = `tu_chiu` hoặc `bi_tu_choi` / **số bài có `nguoi_ban_ke = 1`**.
  - B2: phân bố `ly_do` / số bài có `ket_qua` = `tu_chiu` hoặc `bi_tu_choi`. Dùng để kiểm 3 cách giải thích khác trong `evidence/hypothesis.md` (`gia_tri_nho` ↔ cách 1, `san_xu_ly` ↔ cách 2, `thieu_bang_chung` ↔ cách 3 / lát cắt của nhóm).
- Ghi chú: Bộ B chọn bài theo từ khoá than phiền, nên **lệch về phía ca xấu**. Không dùng để nói "x% shop gặp", chỉ dùng để nói "khi người bán kể về ca hàng vỡ, x/N là tự chịu hoặc bị từ chối, lý do hay gặp nhất là …".

**Script:** `python evidence/count.py` in mọi số A1–A4, B1–B2 dạng x/N (%).
**Kiểm chéo:** một thành viên khác mã hoá lại 20 dòng ngẫu nhiên mỗi bộ, ghi số dòng khớp ở mục 5.

## 2. Đọc trước, đếm sau

- Group / diễn đàn đã dùng cho Bộ B: __
- Đã đọc __ dòng đầu. Các *kiểu* thấy được (trước khi chốt cách mã hoá):
  - __
  - __

## 3. Kết quả

| Đếm gì | x / N | % | Ghi chú |
|---|---|---|---|
| A1 · Đánh giá 1–2 sao nói hàng đến tay bị vỡ / hỏng | __/__ | | mẫu số: mọi đánh giá 1–2 sao có chữ đã đọc |
| A2 · … người mua cho là do vận chuyển | __/__ | | không rõ: __ |
| A3 · … shop đã hoàn tiền / gửi bù / đổi | __/__ | | không rõ: __ |
| A4 · … shop có trả lời và nhắc tới khiếu nại đơn vị vận chuyển | __/__ | | |
| B1 · Người bán kể ca hàng vỡ: tự chịu hoặc bị từ chối bồi thường | __/__ | | được bồi thường: __ · không kể kết quả: __ |
| B2 · Lý do hay gặp nhất | __/__ | | phân bố đủ: __ |

Ghi dạng "x/N (y%)". "Nhiều bạn…" không phải số.

## 4. ≥5 ví dụ cụ thể (mã dòng, không tên người / shop / tài khoản)

1. __ — dòng `A__` / `B__`
2.
3.
4.
5.

## 5. Giới hạn của data

- Bộ A là lời **người mua** (cộng phản hồi ngắn của shop): không cho biết shop mất bao lâu xử lý, và hiếm khi cho biết shop có đòi bồi thường hay không. Chỉ đọc đánh giá 1–2 sao, nên **không phải** tỉ lệ hàng vỡ trên tổng đơn. Người mua được hoàn tiền nhanh thường không chấm sao thấp, nên số đếm có thể thiếu.
- Bộ B lệch về ca xấu (chọn theo từ khoá than phiền) và về người hay đăng bài.
- Cả hai bộ không cho biết **số lần / tháng của một shop** và **thời gian xử lý mỗi lần**. Hai thừa số này ở `spec.md` §2 sẽ ghi *(tự ước tính)* nếu không có phỏng vấn / khảo sát.
- Shopee có quy trình Trả hàng / Hoàn tiền riêng, nên shop bán qua Facebook / Zalo có thể khác.
- Kiểm chéo: Bộ A __/20 · Bộ B __/20 dòng khớp.

→ Kiểm lại bằng: khảo sát / phỏng vấn người bán nếu tìm được (`evidence/survey/`, `evidence/interviews/`). Chưa có thì ghi vào "Điều vẫn chưa biết" ở `evidence/summary.md`.
