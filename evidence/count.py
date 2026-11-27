"""Đếm số liệu đào data — cách đếm ở evidence/data-mining.md mục 1.

Chạy: python evidence/count.py
Đọc 2 file mã hoá tay (mỗi dòng một đánh giá / một bài):
  evidence/shopee-reviews.csv  (Bộ A) cột: id, tu_khoa, san_pham, so_sao, thang_danh_gia,
      nhac_vo_hong, do_van_chuyen, shop_phan_hoi, shop_chiu, shop_nhac_van_chuyen, trich_ngan
  evidence/seller-posts.csv    (Bộ B) cột: id, tu_khoa, noi_tim, thang_dang,
      nguoi_ban_ke, ket_qua, ly_do, trich_ngan
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
FILE_A = os.path.join(HERE, "shopee-reviews.csv")
FILE_B = os.path.join(HERE, "seller-posts.csv")

KET_QUA = ("tu_chiu", "doi_duoc", "bi_tu_choi", "?")
LY_DO = ("thieu_bang_chung", "gia_tri_nho", "qua_han", "thu_tuc_phuc_tap", "san_xu_ly", "khac", "?")


def pct(x, n):
    return "%d/%d (%.0f%%)" % (x, n, 100.0 * x / n) if n else "%d/0" % x


def v(row, key):
    return (row.get(key) or "").strip()


def load(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8-sig", newline="") as f:
        return [r for r in csv.DictReader(f) if v(r, "id")]


def check_a(rows):
    bad = []
    for r in rows:
        i = v(r, "id")
        if v(r, "nhac_vo_hong") not in ("0", "1"):
            bad.append("%s: nhac_vo_hong phải là 0 hoặc 1" % i)
        if v(r, "shop_phan_hoi") not in ("0", "1"):
            bad.append("%s: shop_phan_hoi phải là 0 hoặc 1" % i)
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


def report_a(rows):
    print("=== Bộ A · Đánh giá 1–2 sao Shopee (%s)" % os.path.basename(FILE_A))
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
    print("Theo từ khoá (A1):")
    for kw in sorted({v(r, "tu_khoa") for r in rows}):
        sub = [r for r in rows if v(r, "tu_khoa") == kw]
        print("  %-25s %s" % (kw, pct(sum(v(r, "nhac_vo_hong") == "1" for r in sub), len(sub))))


def report_b(rows):
    print("=== Bộ B · Bài người bán tự kể (%s)" % os.path.basename(FILE_B))
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


def main():
    a, b = load(FILE_A), load(FILE_B)
    bad = check_a(a) + check_b(b)
    if bad:
        print("Dòng cần sửa trước khi đếm:")
        for p in bad:
            print("  - " + p)
        return 1
    report_a(a)
    print()
    report_b(b)
    return 0


if __name__ == "__main__":
    sys.exit(main())
