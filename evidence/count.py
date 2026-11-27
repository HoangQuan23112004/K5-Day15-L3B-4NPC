"""Đếm số liệu đào data — cách đếm ở evidence/data-mining.md mục 1.

Chạy: python evidence/count.py
Đọc 3 file mã hoá tay:
  evidence/shopee-products.csv (Bộ A0, mỗi dòng một sản phẩm) cột: san_pham, tu_khoa,
      tong_danh_gia, so_1_sao, so_2_sao, da_ban
  evidence/shopee-reviews.csv  (Bộ A, mỗi dòng một đánh giá) cột: id, tu_khoa, san_pham, so_sao,
      thang_danh_gia, nhac_vo_hong, do_van_chuyen, shop_phan_hoi, shop_chiu, shop_nhac_van_chuyen,
      shop_do_loi_van_chuyen, trich_ngan
  evidence/seller-posts.csv    (Bộ B, mỗi dòng một bài) cột: id, tu_khoa, noi_tim, thang_dang,
      nguoi_ban_ke, ket_qua, ly_do, thoi_gian_ke, trich_ngan
Giá trị: 1 = có · 0 = không · ? = không rõ. Chỉ dùng thư viện chuẩn.
"""
import csv
import os
import sys
from collections import Counter

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

HERE = os.path.dirname(os.path.abspath(__file__))
FILE_P = os.path.join(HERE, "shopee-products.csv")
FILE_A = os.path.join(HERE, "shopee-reviews.csv")
FILE_B = os.path.join(HERE, "seller-posts.csv")

KET_QUA = ("tu_chiu", "doi_duoc", "bi_tu_choi", "?")
LY_DO = ("thieu_bang_chung", "gia_tri_nho", "qua_han", "thu_tuc_phuc_tap", "san_xu_ly", "khac", "?")


def pct(x, n):
    return "%d/%d (%.0f%%)" % (x, n, 100.0 * x / n) if n else "%d/0" % x


def v(row, key):
    return (row.get(key) or "").strip()


def load(path, key="id"):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8-sig", newline="") as f:
        return [r for r in csv.DictReader(f) if v(r, key)]


def check_a(rows):
    bad = []
    for r in rows:
        i = v(r, "id")
        if v(r, "nhac_vo_hong") not in ("0", "1"):
            bad.append("%s: nhac_vo_hong phải là 0 hoặc 1" % i)
        if v(r, "shop_phan_hoi") not in ("0", "1"):
            bad.append("%s: shop_phan_hoi phải là 0 hoặc 1" % i)
        if v(r, "shop_phan_hoi") == "1" and v(r, "shop_do_loi_van_chuyen") not in ("0", "1"):
            bad.append("%s: shop_do_loi_van_chuyen phải là 0 hoặc 1" % i)
        if v(r, "nhac_vo_hong") == "1":
            for k in ("do_van_chuyen", "shop_chiu"):
                if v(r, k) not in ("0", "1", "?"):
                    bad.append("%s: %s phải là 0, 1 hoặc ?" % (i, k))
            if v(r, "shop_phan_hoi") == "1" and v(r, "shop_nhac_van_chuyen") not in ("0", "1"):
                bad.append("%s: shop_nhac_van_chuyen phải là 0 hoặc 1" % i)
    return bad


def check_b(rows):
    bad = []
    for r in rows:
        i = v(r, "id")
        if v(r, "nguoi_ban_ke") not in ("0", "1"):
            bad.append("%s: nguoi_ban_ke phải là 0 hoặc 1" % i)
        if v(r, "nguoi_ban_ke") == "1":
            if v(r, "ket_qua") not in KET_QUA:
                bad.append("%s: ket_qua phải là một trong %s" % (i, ", ".join(KET_QUA)))
            if v(r, "ket_qua") in ("tu_chiu", "bi_tu_choi") and v(r, "ly_do") not in LY_DO:
                bad.append("%s: ly_do phải là một trong %s" % (i, ", ".join(LY_DO)))
    return bad


def check_p(rows):
    bad = []
    for r in rows:
        for k in ("tong_danh_gia", "so_1_sao", "so_2_sao", "da_ban"):
            if not v(r, k).isdigit():
                bad.append("%s: %s phải là số nguyên (vd 1,2k → 1200)" % (v(r, "san_pham"), k))
        for k in ("cam_ket_doi_vo", "yeu_cau_video"):
            if v(r, k) not in ("0", "1"):
                bad.append("%s: %s phải là 0 hoặc 1" % (v(r, "san_pham"), k))
    return bad


def report_a(rows, products):
    print("=== Bộ A · Shopee — nguồn chính")
    total = sum(int(v(r, "tong_danh_gia")) for r in products)
    low = sum(int(v(r, "so_1_sao")) + int(v(r, "so_2_sao")) for r in products)
    print("A0 (%s): %d sản phẩm · tổng đánh giá %d · đánh giá 1–2 sao %s"
          % (os.path.basename(FILE_P), len(products), total, pct(low, total)))
    print("A7 mô tả của shop cam kết đổi / hoàn khi vỡ do vận chuyển: "
          + pct(sum(v(r, "cam_ket_doi_vo") == "1" for r in products), len(products)))
    print("A8 mô tả của shop khuyên / yêu cầu quay video mở hàng:     "
          + pct(sum(v(r, "yeu_cau_video") == "1" for r in products), len(products)))
    print("--- Bảng đánh giá (%s)" % os.path.basename(FILE_A))
    n = len(rows)
    print("Sản phẩm: %d · từ khoá: %d · mẫu số (đánh giá 1–2 sao có chữ đã đọc): %d"
          % (len({v(r, "san_pham") for r in rows}), len({v(r, "tu_khoa") for r in rows}), n))
    broken = [r for r in rows if v(r, "nhac_vo_hong") == "1"]
    nb = len(broken)
    carrier = Counter(v(r, "do_van_chuyen") for r in broken)
    paid = Counter(v(r, "shop_chiu") for r in broken)
    replied = [r for r in broken if v(r, "shop_phan_hoi") == "1"]
    print("A1 nói hàng đến tay bị vỡ / hỏng:                 " + pct(nb, n))
    print("A2 … người mua cho là do vận chuyển:              " + pct(carrier["1"], nb)
          + "  · do shop đóng gói %d · không rõ %d" % (carrier["0"], carrier["?"]))
    print("A3 … shop hoàn tiền / gửi bù / đổi:               " + pct(paid["1"], nb)
          + "  · không %d · không rõ %d" % (paid["0"], paid["?"]))
    print("A4 … shop trả lời và nhắc khiếu nại vận chuyển:   "
          + pct(sum(v(r, "shop_nhac_van_chuyen") == "1" for r in replied), len(replied)))
    blame = [r for r in replied if v(r, "shop_do_loi_van_chuyen") == "1"]
    conflict = [r for r in blame if v(r, "do_van_chuyen") == "0"]
    print("A6 … shop trả lời và đổ lỗi cho vận chuyển:       " + pct(len(blame), len(replied))
          + "  · hai bên đổ lỗi khác nhau: %d (%s)" % (len(conflict), ", ".join(v(r, "id") for r in conflict) or "—"))
    all_replied = [r for r in rows if v(r, "shop_phan_hoi") == "1"]
    print("   (mọi đánh giá có phản hồi: shop đổ cho vận chuyển %s)"
          % pct(sum(v(r, "shop_do_loi_van_chuyen") == "1" for r in all_replied), len(all_replied)))
    if total and n:
        a5 = 100.0 * low / total * nb / n
        print("A5 ước tính đánh giá nói hàng vỡ / tổng đánh giá: %.2f%%  (= 1–2 sao %d/%d × A1 %d/%d)"
              % (a5, low, total, nb, n))
        print("   → shop 300 đơn / tháng ≈ %.1f khiếu nại hàng vỡ / tháng (minh hoạ, giả định mỗi đánh giá ≈ 1 đơn)"
              % (300 * a5 / 100))
    else:
        print("A5: chưa đủ data (cần cả shopee-products.csv và shopee-reviews.csv)")
    print("Theo từ khoá (A1):")
    for kw in sorted({v(r, "tu_khoa") for r in rows}):
        sub = [r for r in rows if v(r, "tu_khoa") == kw]
        print("  %-25s %s" % (kw, pct(sum(v(r, "nhac_vo_hong") == "1" for r in sub), len(sub))))


def report_b(rows):
    print("=== Bộ B · Bài người bán tự kể — nguồn bổ sung, lệch về ca xấu (%s)" % os.path.basename(FILE_B))
    sellers = [r for r in rows if v(r, "nguoi_ban_ke") == "1"]
    ns = len(sellers)
    print("Đã đọc %d bài · người bán kể ca hàng vỡ: %d" % (len(rows), ns))
    kq = Counter(v(r, "ket_qua") for r in sellers)
    lost = [r for r in sellers if v(r, "ket_qua") in ("tu_chiu", "bi_tu_choi")]
    print("B1 tự chịu hoặc bị từ chối bồi thường:            " + pct(len(lost), ns)
          + "  · tự chịu %d · bị từ chối %d · đòi được %d · không kể %d"
          % (kq["tu_chiu"], kq["bi_tu_choi"], kq["doi_duoc"], kq["?"]))
    print("B2 lý do (trên %d bài tự chịu / bị từ chối):" % len(lost))
    ld = Counter(v(r, "ly_do") for r in lost)
    for k, c in ld.most_common():
        print("  %-20s %s" % (k, pct(c, len(lost))))
    times = [(v(r, "id"), v(r, "thoi_gian_ke")) for r in sellers if v(r, "thoi_gian_ke")]
    print("Thời gian xử lý người bán có kể: %d bài" % len(times))
    for i, t in times:
        print("  %s: %s" % (i, t))


def main():
    p, a, b = load(FILE_P, "san_pham"), load(FILE_A), load(FILE_B)
    bad = check_p(p) + check_a(a) + check_b(b)
    if bad:
        print("Dòng cần sửa trước khi đếm:")
        for x in bad:
            print("  - " + x)
        return 1
    report_a(a, p)
    print()
    report_b(b)
    return 0


if __name__ == "__main__":
    sys.exit(main())
