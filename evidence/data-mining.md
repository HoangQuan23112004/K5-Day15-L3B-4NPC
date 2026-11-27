# Đào data — cách đếm và kết quả

> Điền ở guide bước 1.2. Ôn lại: ngày 2, ngày 6 · lab ngày 2, lab ngày 6.
> Script đếm: `evidence/count.py` — chạy `python evidence/count.py` ra đúng các số ở mục 3.
> Repo chỉ chứa số đã tổng hợp và bảng mã hoá đã ẩn danh (`evidence/shopee-products.csv`, `evidence/shopee-reviews.csv`, `evidence/app-reviews.csv`): không tên người mua, tên tài khoản, tên người viết review. Link **trang sản phẩm / trang app công khai** và ngày xem được ghi để người khác kiểm lại (guide 1.2: "Ghi link nguồn và ngày xem").
> Người làm: Ngô Chí Vĩnh. Đọc tay, không dùng công cụ cào tự động.
> BTC không cấp data cho Track D, nhóm không liên hệ được chủ shop để phỏng vấn / khảo sát → đào data là nguồn bằng chứng duy nhất.

## 1. Cách đếm — viết TRƯỚC khi chạy

- Bản đầu: 17:45 Thứ Sáu 27/11/2026 (commit `7457ab9`). **Sửa lần 1: 17:50 cùng ngày, trước khi đọc dòng data đầu tiên.** Lý do sửa: chuyển Bộ A (Shopee) thành nguồn chính vì đúng dạng "đếm trên một bộ dữ liệu"; thêm bảng cấp sản phẩm (A0) để ước tính tần suất; Bộ B chỉ còn là nguồn bổ sung.
- **Data dùng:** trang sản phẩm và đánh giá công khai trên Shopee Việt Nam (Bộ A), review Google Play của app giao hàng GHTK, GHN (Bộ B, đổi lúc 18:45 — xem mục Bộ B). Đọc tay ngày 27–28/11/2026.

### Bộ A · Shopee — NGUỒN CHÍNH

**Chọn sản phẩm (cố định trước, không chọn cho khớp):**
- 4 từ khoá hàng dễ vỡ / dễ hỏng: `ly thủy tinh` · `bình gốm` · `serum chai thủy tinh` · `bánh quy hộp`.
- Mỗi từ khoá: tìm trên Shopee, sắp xếp "Bán chạy", lấy **3 sản phẩm đầu tiên**. Bỏ qua sản phẩm Shopee Mall (shop lớn, không phải người dùng của nhóm) và sản phẩm không có đánh giá 1–2 sao → **12 sản phẩm**, mã `SP01`…`SP12` (`ly thủy tinh` SP01–03 · `bình gốm` SP04–06 · `serum chai thủy tinh` SP07–09 · `bánh quy hộp` SP10–12).
- *(Đổi lúc 18:27 Thứ Sáu 27/11, sau khi làm xong SP01–SP03 và trước khi mở sản phẩm tiếp theo: giảm từ 5 xuống 3 sản phẩm mỗi từ khoá (20 → 12) **vì không đủ thời gian** trước CP3, ưu tiên giữ đủ 4 nhóm hàng. Không đổi vì kết quả. SP01–SP03 giữ nguyên.)*

**A0 · Bảng sản phẩm → `evidence/shopee-products.csv`** (mỗi sản phẩm một dòng, chép đúng số Shopee hiện):
- `tong_danh_gia`, `so_1_sao`, `so_2_sao`: số đánh giá theo bộ lọc sao trên trang sản phẩm. `tong_danh_gia` = **cộng 5 nút "5 Sao … 1 Sao"** (số "Đánh Giá" ở đầu trang có khi lệch với các nút, vd SP02 đầu trang 1,5k nhưng cộng các nút ≈ 2.731). *(Làm rõ sau khi đọc SP02.)*
- `da_ban`: số "Đã bán" Shopee hiện (vd `1,2k` → ghi `1200`; `10k+` → ghi `10000`).
- `cam_ket_doi_vo` (1/0): phần **mô tả sản phẩm do shop viết** cam kết đổi / hoàn tiền khi hàng vỡ, hư hỏng **do vận chuyển**.
- `yeu_cau_video` (1/0): mô tả sản phẩm yêu cầu / khuyên người mua quay video mở hàng.
- *(Hai cột này thêm sau khi đọc mô tả SP01: shop viết "đổi trả 1-1 trong 7 ngày… bể vỡ do quá trình vận chuyển" và "nên quay video mở hàng".)*
- A7: `cam_ket_doi_vo = 1` / số sản phẩm · A8: `yeu_cau_video = 1` / số sản phẩm.

**A1–A4 · Bảng đánh giá → `evidence/shopee-reviews.csv`:**
- Mỗi sản phẩm: lọc "1 sao", lấy **tối đa 10 đánh giá có chữ đầu tiên theo thứ tự Shopee hiển thị**; còn thiếu thì lọc "2 sao" lấy tiếp cho đủ 10 → tối đa 120 dòng. *(Làm rõ sau khi đọc 6 đánh giá đầu của SP01: Shopee không cho sắp xếp đánh giá theo ngày, nên đổi "mới nhất" thành "theo thứ tự Shopee hiển thị".)*
- Mã hoá **chỉ theo chữ** người mua và shop viết; không xem, không tải, không lưu ảnh / video của người mua.
- Link từng sản phẩm và ngày xem ghi ở cột `link`, `ngay_xem` của `evidence/shopee-products.csv`. File thô `evidence/raw-shopee-SPxx.txt` (có tên tài khoản người mua) **không commit**. *(Thêm cột link lúc 18:43 theo guide 1.2.)*
- **"Có chữ"** = người mua tự viết nội dung. Đánh giá chỉ có thẻ chọn sẵn của Shopee (vd "Sản phẩm: Hàng lỗi hoặc bị hư hỏng") mà không có chữ tự viết thì **bỏ qua, không ghi**.
- Mã hoá (1 = có · 0 = không · `?` = không rõ):
  - `nhac_vo_hong`: đánh giá nói hàng **lúc đến tay / lúc mở hộp** đã bị vỡ, nứt, móp, chảy, hỏng. Ghi 0 nếu chê vì lý do khác, **kể cả vỡ trong lúc sử dụng** (rót nước nóng, bỏ đá…) hoặc chỉ "sợ dễ vỡ" — đó là chất lượng sản phẩm, không phải khâu giao hàng.
  - `do_van_chuyen` (chỉ khi `nhac_vo_hong` = 1): 1 = người mua nói / ngụ ý do vận chuyển; 0 = do shop đóng gói sơ sài; `?` = không rõ.
  - `shop_phan_hoi`: shop có trả lời đánh giá.
  - `shop_chiu` (chỉ khi `nhac_vo_hong` = 1): người mua hoặc shop cho thấy shop **đã làm hoặc đề nghị** hoàn tiền / gửi bù / đổi hàng mà không đòi người mua chịu. *(Làm rõ sau khi đọc SP01: phản hồi của shop thường là lời đề nghị "phản hồi lại để e gửi lại", hiếm khi cho biết đã làm xong.)*
  - `shop_nhac_van_chuyen` (chỉ khi `nhac_vo_hong` = 1 và `shop_phan_hoi` = 1): phản hồi của shop nhắc tới việc **khiếu nại / đòi bồi thường / làm việc** với đơn vị vận chuyển. Chỉ đổ lỗi thì không tính.
  - `shop_do_loi_van_chuyen` (khi `shop_phan_hoi` = 1, mọi đánh giá): phản hồi của shop **đổ lỗi cho vận chuyển** (vd "chắc bên vận chuyển quăng quật"). *(Thêm sau khi đọc 10 đánh giá của SP01: đã gặp 2 lần shop đổ cho vận chuyển mà không nêu căn cứ.)*

**Mẫu số:**
- A1: `nhac_vo_hong = 1` / **mọi đánh giá 1–2 sao có chữ đã đọc**.
- A2: `do_van_chuyen = 1` / số dòng `nhac_vo_hong = 1`.
- A3: `shop_chiu = 1` / số dòng `nhac_vo_hong = 1`.
- A4: `shop_nhac_van_chuyen = 1` / số dòng `nhac_vo_hong = 1` **và** `shop_phan_hoi = 1`.
- A6: `shop_do_loi_van_chuyen = 1` / số dòng `nhac_vo_hong = 1` **và** `shop_phan_hoi = 1` · kèm số ca **hai bên đổ lỗi khác nhau** (người mua nói do shop đóng gói `do_van_chuyen = 0`, shop nói do vận chuyển).
- A5 (ước tính tần suất, dùng cho `spec.md` §2): tỉ lệ đánh giá 1–2 sao trên tổng đánh giá (cộng các sản phẩm ở A0) × A1 = **tỉ lệ đánh giá nói hàng vỡ / hỏng trên tổng đánh giá**. Coi mỗi đánh giá đại diện một đơn → số khiếu nại hàng vỡ / tháng của một shop ≈ số đơn / tháng × A5 *(giả định của nhóm: người nhận hàng vỡ có xu hướng đánh giá nhiều hơn người nhận hàng tốt, nên con số này có thể cao hơn thực tế; người được hoàn tiền nhanh có thể không đánh giá xấu, nên cũng có thể thấp hơn)*.

### Bộ B · Review Google Play của app giao hàng mà shop dùng — NGUỒN THỨ HAI, KIỂM LẠI BỘ A

*(Đổi lúc 18:45 Thứ Sáu 27/11, khi Bộ B cũ — bài người bán tìm qua Google — **chưa đọc dòng nào**. Lý do: file Track D của đề gợi ý "review công khai trên Google Play, App Store (… app cho người bán …)"; người viết review app giao hàng phần lớn là **người gửi hàng / chủ shop**, bù đúng giới hạn lớn nhất của Bộ A là chỉ có lời người mua; mẫu có cách chọn cố định, chạy lại được, khác kết quả tìm Google thay đổi theo người tìm.)*

- **Nguồn (cố định trước):** trang Google Play của **2 app giao hàng chính thức dành cho người gửi hàng / shop**: GHTK (Giao Hàng Tiết Kiệm) và GHN (Giao Hàng Nhanh). Ghi đúng tên app, link và ngày xem ở mục 2 khi mở.
- **Chọn mẫu:** mỗi app mở "Xem tất cả bài đánh giá" → sắp xếp **"Mới nhất"** → lọc **1 sao** → đọc **30 review có chữ đầu tiên** → N ≤ 60. Nếu bản web không có bộ lọc sao thì dùng app Google Play trên điện thoại, cùng cách chọn. Chỉ lọc 1 sao nên mẫu **nghiêng về phàn nàn** (guide 1.2 cho phép, phải ghi rõ).
- **Mã hoá → `evidence/app-reviews.csv`** (cột: `id, app, so_sao, ngay, nguoi_gui, chu_de, boi_thuong, ly_do, thoi_gian_ke, trich_ngan`):
  - `nguoi_gui`: 1 nếu người viết là **người gửi hàng / shop** (nói "shop mình", "gửi hàng cho khách", "đơn của khách", tiền COD); 0 nếu là người nhận, shipper, người khác; `?` nếu không rõ.
  - `chu_de` (một nhãn chính): `vo_hong` (hàng vỡ, móp, hỏng khi giao) · `that_lac` (mất, thất lạc) · `giao_cham` · `thai_do` (thái độ shipper / tổng đài) · `tien_phi` (tiền COD, phí ship, đối soát) · `loi_app` · `khac`.
  - `boi_thuong` (khi `chu_de` là `vo_hong` / `that_lac`): `khong_den` (bị từ chối / không được đền) · `den_it` (đền thấp hơn giá trị) · `cho_lau` (khiếu nại chưa có kết quả, kéo dài) · `duoc_den` · `?` (không nói).
  - `ly_do` (khi `boi_thuong` là `khong_den` / `den_it` / `cho_lau`): `thieu_bang_chung` · `qua_han` · `da_ky_nhan` (người nhận đã ký / đã nhận) · `quy_dinh_muc_den` (theo mức đền quy định) · `khac` · `?` (không nói).
  - `thoi_gian_ke`: thời gian chờ / xử lý nếu người viết có kể (vd "2 tuần"), không có thì để trống.
  - Không chép tên người viết review. Trích tối đa 2 câu.
- **Mẫu số:**
  - B1: `chu_de = vo_hong` / số review `nguoi_gui = 1` (trong phàn nàn của người gửi hàng, bao nhiêu là về hàng vỡ / hỏng).
  - B2: `boi_thuong` là `khong_den` / `den_it` / `cho_lau` / số review `nguoi_gui = 1` có `chu_de` là `vo_hong` hoặc `that_lac`.
  - B3: phân bố `ly_do` trên các review ở tử số B2 → kiểm cách giải thích khác trong `evidence/hypothesis.md` (`thieu_bang_chung` / `qua_han` / `da_ky_nhan` ủng hộ lát cắt; `quy_dinh_muc_den` gần với cách giải thích khác 1).
- **Kiểm lại Bộ A thế nào:** Bộ A cho thấy shop gần như không nhắc tới đòi bồi thường vận chuyển (A4) và tự hoàn / gửi bù (A3). Bộ B cho biết, **khi shop có đòi**, kết quả ra sao và vướng ở đâu. Hai nguồn khớp nếu B2 cao (đòi thường không được) và lý do là bằng chứng / hạn; lệch thì ghi và giải thích ở `evidence/summary.md` mục 4.

**Script:** `python evidence/count.py` in mọi số A1–A8, B1–B3.
**Kiểm chéo:** một thành viên khác mã hoá lại 20 dòng ngẫu nhiên của `shopee-reviews.csv` (và 10 dòng `app-reviews.csv` nếu kịp), ghi số dòng khớp ở mục 5.

### Tài liệu tham khảo (không phải bằng chứng pain)

Chính sách chính thức của Shopee (cùng nguồn với Bộ A), dùng cho `spec.md` §0 (luồng hiện tại) và §2 (mỗi ca mất bao nhiêu):
- Bảo hiểm Thiệt hại sản phẩm (trang bảo hiểm chính thức của Shopee, mở từ trang SP01, xem 27/11/2026): https://insurance.shopee.vn/ec/ec-pdp.html?from=pdp&locale=VI&product_id=1967808564094407209 · quy tắc đầy đủ của MSIG: https://tructuyen.msig.com.vn/assets/documents/shopee/merchandise/Damage_Insurance_Wording.pdf
  - Do MSIG cung cấp qua môi giới Fuse; **người mua** tự chọn mua kèm ở trang Thanh toán (ví dụ trên trang: ₫50 cho món ₫2.000.000), hiệu lực 6 tháng, chỉ đền 1 lần.
  - Đền khi hàng **thiệt hại toàn bộ (≥75% giá trị)** do sự cố bất ngờ (rơi / nghiền nát sau tai nạn, cháy, nổ…), do chất lỏng, hoặc mất cắp / cướp giật.
  - **Loại trừ (trích nguyên văn):** *"Sản phẩm có tình trạng bị thiệt hại hoặc hư hỏng từ trước khi bắt đầu hiệu lực bảo hiểm hoặc thất lạc, mất, thiệt hại trong quá trình giao hàng của nhà vận chuyển."* Cũng loại trừ thực phẩm, đồ uống.
  - → **Bảo hiểm này không đền hàng vỡ khi giao.** Ca hàng vỡ khi giao vẫn phải xử lý giữa người mua, shop và đơn vị vận chuyển, qua quy trình Trả hàng / Hoàn tiền. Dùng cho `spec.md` §0, §3 và để kiểm cách giải thích khác 2 trong `evidence/hypothesis.md`.
- Trả hàng / Hoàn tiền (link do file Track D của đề dẫn): https://help.shopee.vn/portal/4/article/79191 — __ (ngày xem · hạn khiếu nại · bằng chứng cần có · người bán phản hồi thế nào)

## 2. Đọc trước, đếm sau

Đã đọc 1 trang sản phẩm (SP01) / 6 đánh giá đầu lúc 17:55. Các *kiểu* thấy được (dùng để làm rõ cách mã hoá ở mục 1, không đổi cách chọn mẫu):
- Đánh giá chê **chất lượng** có chữ "vỡ / bể" nhưng là vỡ **khi sử dụng** (rót nước nóng, bỏ đá) → làm rõ: không tính là hàng vỡ khi giao.
- Đánh giá **chỉ có thẻ chọn sẵn** của Shopee, không có chữ tự viết → làm rõ: bỏ qua.
- Shopee **không cho sắp xếp theo ngày** → làm rõ: lấy theo thứ tự Shopee hiển thị.
- Phản hồi của shop có khi **đổ cho vận chuyển mà không có căn cứ** ("Chắc bên vận chuyển họ quăng quật…" cho một ca người mua nói vỡ khi bỏ đá) → giữ làm ví dụ định tính.
- Người mua nói **"lỡ bấm đã nhận hàng thì không trả hàng được"** → đối chiếu với điều kiện Trả hàng / Hoàn tiền của Shopee (xem Tài liệu tham khảo).

## 3. Kết quả

| Đếm gì | x / N | % | Ghi chú |
|---|---|---|---|
| A1 · Đánh giá 1–2 sao nói hàng đến tay bị vỡ / hỏng | __/__ | | mẫu số: mọi đánh giá 1–2 sao có chữ đã đọc |
| A2 · … người mua cho là do vận chuyển | __/__ | | không rõ: __ |
| A3 · … shop đã hoàn tiền / gửi bù / đổi | __/__ | | không rõ: __ |
| A4 · … shop có trả lời và nhắc tới khiếu nại đơn vị vận chuyển | __/__ | | |
| A5 · Ước tính đánh giá nói hàng vỡ / tổng đánh giá | | __% | = tỉ lệ 1–2 sao (__/__) × A1 |
| A6 · … shop trả lời và đổ lỗi cho vận chuyển | __/__ | | hai bên đổ lỗi khác nhau: __ |
| B1 · Người bán kể ca hàng vỡ: tự chịu hoặc bị từ chối | __/__ | | bổ sung, lệch về ca xấu |
| B2 · Lý do hay gặp nhất | __/__ | | |

Ghi dạng "x/N (y%)". "Nhiều bạn…" không phải số.

## 4. ≥5 ví dụ cụ thể (mã dòng, không tên người / shop / tài khoản)

1. __ — dòng `A__`
2.
3.
4.
5.

## 5. Giới hạn của data

- Bộ A là lời **người mua** (cộng phản hồi ngắn của shop), không phải lời chủ shop. Không cho biết shop mất bao lâu xử lý, hiếm khi cho biết shop có đòi bồi thường không.
- Chỉ đọc đánh giá 1–2 sao. A5 là ước tính có giả định (mỗi đánh giá ≈ một đơn), không phải tỉ lệ hàng vỡ đo trên đơn hàng thật.
- Chỉ Shopee, chỉ 4 nhóm hàng dễ vỡ. Shop bán qua Facebook / Zalo không có quy trình Trả hàng / Hoàn tiền của sàn nên có thể khác (cách giải thích khác 2 trong `evidence/hypothesis.md`).
- **Không hỏi được người dùng để kiểm lại**: chưa biết thời gian xử lý mỗi ca, Bộ B (review app giao hàng) cho biết vì sao đòi bồi thường không được, nhưng chỉ lọc 1 sao nên nghiêng về phàn nàn và không cho biết tỉ lệ trên mọi shop.
- Kiểm chéo: __/20 dòng khớp.
