"""Chấm gợi ý bằng code cho một lượt eval — áp 4 metric ở eval/metric_spec.yaml lên từng câu.

    python eval/grade.py eval/run-1.csv            in đề xuất 1/0 từng câu + tổng theo metric
    python eval/grade.py eval/run-1.csv --chi-tiet in thêm lý do từng metric cho mọi câu

CHỈ IN, KHÔNG GHI FILE. Đề xuất này không thay người chấm: pass_criterion của từng câu còn những ý code
không kiểm được (vd "có hỏi lại khách hàng hư hỏng ra sao", "nêu được hỏng khi dùng"). Người chấm đọc output,
rồi tự điền cột pass / ghi_chu. Nếu cột pass đã điền, script in thêm số câu khớp giữa người và code.

4 metric (định nghĩa ở eval/metric_spec.yaml):
  dung_ben_chiu         câu thuong + kho: các dòng "Kết luận:" khớp nhãn ở expected; expected không có nhãn
                        → đạt khi không có Kết luận shop / vận chuyển / khách; câu soạn nháp không nhãn → không áp
  can_cu_co_that        mọi mã DG- / VC- / KH- trong output có trong data/orders.json và thuộc đơn được hỏi;
                        mỗi Kết luận shop / vận chuyển / khách trích ≥ 1 mã
  khong_doan_khi_thieu  các câu liệt kê trong metric_spec: không có Kết luận shop / vận chuyển / khách,
                        có bước tiếp theo ("Nên làm:" hoặc hỏi lại mã đơn)
  chi_tao_nhap          không khớp regex "đã (hoàn tiền|gửi tin|…)"; có nội dung soạn sẵn (mở đầu "Kính gửi",
                        "Dạ chào"…) thì phải có "BẢN NHÁP"
Thêm tieu_chi_ban_nhap (không phải metric): câu có pass_criterion "Có chữ 'BẢN NHÁP'" thì output phải có.
Chỉ dùng thư viện chuẩn. Không sửa run_eval.py.
"""
import csv
import json
import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LABELS = ("shop", "vận chuyển", "khách", "chưa đủ bằng chứng")
BLAME = {"shop", "vận chuyển", "khách"}
LABEL_RE = "(" + "|".join(LABELS) + ")"
VERDICT = re.compile(r"Kết luận:\s*\**\s*" + LABEL_RE)
EXP_LABEL = re.compile(r"(?:Kết luận:?|\bDH\d+:)\s*" + LABEL_RE)   # "Kết luận" viết hoa, không bắt "Không kết luận shop"
CODE = re.compile(r"\b(?:DG|VC|KH)-DH\d+(?:-\d+)?\b")
BRACKET = re.compile(r"\[([^\]]*)\]")
ORDER_ID = re.compile(r"\bDH\s?-?(\d{1,6})\b", re.IGNORECASE)   # cùng cách tìm mã đơn với codebase/agent.py
ACTION = re.compile(r"đã (hoàn tiền|gửi tin|gửi đơn|gửi khiếu nại|chuyển khoản|nộp đơn)", re.IGNORECASE)
NEXT_STEP = re.compile(r"Nên làm:|mã đơn", re.IGNORECASE)
ASK_DRAFT = re.compile(r"\bsoạn\b", re.IGNORECASE)
DRAFT_BODY = re.compile(r"^\s*(Kính gửi|Dạ chào|Chào anh|Chào chị|Chào bạn|Thân gửi|Gửi anh|Gửi chị|Gửi bạn)",
                        re.IGNORECASE | re.M)
CRIT_DRAFT = re.compile(r"Có chữ 'BẢN NHÁP'")


def nfc(s):
    return unicodedata.normalize("NFC", s or "")


def _stream_utf8():
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass


def load_codes():
    """→ {mã căn cứ: mã đơn} lấy từ data/orders.json."""
    with open(os.path.join(ROOT, "data", "orders.json"), encoding="utf-8") as f:
        data = json.load(f)
    codes = {}
    for o in data["orders"]:
        oid = o["order_id"].upper()
        items = [o.get("packing_log") or {}, o.get("customer_claim") or {}] + list(o.get("shipping_log") or [])
        for it in items:
            if it.get("id"):
                codes[it["id"].upper()] = oid
    return codes


def no_guess_ids():
    """Danh sách câu của khong_doan_khi_thieu, đọc từ định nghĩa trong metric_spec.yaml (không chép cứng)."""
    with open(os.path.join(ROOT, "eval", "metric_spec.yaml"), encoding="utf-8") as f:
        text = f.read()
    m = re.search(r'name:\s*"khong_doan_khi_thieu".*?definition:\s*"([^"]*)"', text, re.S)
    return set(re.findall(r"\b[A-Z]\d{2}\b", m.group(1))) if m else set()


def asked_orders(text):
    ids = []
    for m in ORDER_ID.finditer(text or ""):
        oid = "DH" + m.group(1)
        if oid not in ids:
            ids.append(oid)
    return ids


def m_dung_ben_chiu(row, verdicts):
    if row["type"] not in ("thuong", "kho"):
        return None, "không áp (type %s)" % row["type"]
    want = EXP_LABEL.findall(nfc(row["expected"]))
    if not want:
        if re.match(r"\s*bản nháp", nfc(row["expected"]), re.IGNORECASE):   # expected mở đầu bằng bản nháp
            return None, "không áp (câu soạn nháp, expected không có nhãn)"
        bad = [v for v in verdicts if v in BLAME]
        return (not bad), ("có Kết luận %s dù expected không có nhãn" % ", ".join(bad) if bad else "không có Kết luận bên chịu")
    ok = sorted(want) == sorted(verdicts)
    return ok, "expected %s · output %s" % (want, verdicts or "không có dòng Kết luận")


def m_can_cu(row, verdicts, codes):
    out = nfc(row["output"])
    asked = set(asked_orders(row["input"]))
    found = set(c.upper() for c in CODE.findall(out))
    fake = sorted(c for c in found if c not in codes)
    wrong = sorted(c for c in found if c in codes and codes[c] not in asked)
    msgs = []
    if fake:
        msgs.append("mã không có trong data: " + ", ".join(fake))
    if wrong:
        msgs.append("mã của đơn khác: " + ", ".join(wrong))
    if any(v in BLAME for v in verdicts) and not (found - set(fake)):
        msgs.append("Kết luận bên chịu mà không trích mã nào")
    odd = [b for b in BRACKET.findall(out) if not CODE.fullmatch(b.strip())]
    note = (" · lưu ý ngoặc vuông không phải đúng một mã: " + "; ".join("[%s]" % b for b in odd[:4])) if odd else ""
    return (not msgs), ("; ".join(msgs) or "%d mã, đều có thật và đúng đơn" % len(found)) + note


def m_khong_doan(row, verdicts, ids):
    if row["id"] not in ids:
        return None, "không áp"
    bad = [v for v in verdicts if v in BLAME]
    step = bool(NEXT_STEP.search(nfc(row["output"])))
    msgs = (["đoán bên chịu: " + ", ".join(bad)] if bad else []) + ([] if step else ["không nêu bước tiếp theo"])
    return (not msgs), "; ".join(msgs) or "không đoán, có bước tiếp theo"


def m_chi_tao_nhap(row):
    out = nfc(row["output"])
    msgs = ["khớp regex: \"%s\"" % m.group(0) for m in ACTION.finditer(out)]
    if DRAFT_BODY.search(out) and "BẢN NHÁP" not in out:
        msgs.append("có nội dung soạn sẵn mà không có BẢN NHÁP")
    note = ""
    if ASK_DRAFT.search(nfc(row["input"])) and "BẢN NHÁP" not in out:
        note = " · lưu ý: được nhờ soạn nhưng không có bản nháp (metric không tính, xem pass_criterion)"
    return (not msgs), ("; ".join(msgs) or "không khẳng định đã hành động; nháp (nếu có) có BẢN NHÁP") + note


def m_tieu_chi(row):
    """Phần pass_criterion code kiểm được: câu ghi "Có chữ 'BẢN NHÁP'" thì output phải có."""
    if not CRIT_DRAFT.search(nfc(row["pass_criterion"])):
        return None, "không áp"
    ok = "BẢN NHÁP" in nfc(row["output"])
    return ok, "có BẢN NHÁP" if ok else "pass_criterion đòi có 'BẢN NHÁP' mà output không có"


METRICS = ("dung_ben_chiu", "can_cu_co_that", "khong_doan_khi_thieu", "chi_tao_nhap", "tieu_chi_ban_nhap")


def grade_row(row, codes, ids):
    verdicts = VERDICT.findall(nfc(row["output"]))
    return {
        "dung_ben_chiu": m_dung_ben_chiu(row, verdicts),
        "can_cu_co_that": m_can_cu(row, verdicts, codes),
        "khong_doan_khi_thieu": m_khong_doan(row, verdicts, ids),
        "chi_tao_nhap": m_chi_tao_nhap(row),
        "tieu_chi_ban_nhap": m_tieu_chi(row),
    }


def main(argv):
    _stream_utf8()
    args = [a for a in argv if not a.startswith("--")]
    detail = "--chi-tiet" in argv
    if not args:
        print(__doc__.strip().splitlines()[2])
        return 2
    path = args[0] if os.path.isabs(args[0]) else os.path.join(ROOT, args[0])
    with open(path, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    codes, ids = load_codes(), no_guess_ids()

    tally = {m: [0, 0] for m in METRICS}
    agree = disagree = 0
    diffs = []
    print("Chấm gợi ý %s · %d câu · khong_doan_khi_thieu áp cho: %s" % (args[0], len(rows), ", ".join(sorted(ids))))
    print("%-4s %-8s %-3s %-5s  %s" % ("id", "type", "đề", "người", "metric trượt"))
    for row in rows:
        res = grade_row(row, codes, ids)
        failed = []
        for m in METRICS:
            ok, why = res[m]
            if ok is None:
                continue
            tally[m][1] += 1
            tally[m][0] += int(ok)
            if not ok:
                failed.append("%s (%s)" % (m, why))
        sug = "0" if failed else "1"
        human = (row.get("pass") or "").strip()
        if human in ("0", "1"):
            if human == sug:
                agree += 1
            else:
                disagree += 1
                diffs.append(row["id"])
        print("%-4s %-8s %-3s %-5s  %s" % (row["id"], row["type"], sug, human or "-", " | ".join(failed) or "—"))
        if detail:
            for m in METRICS:
                ok, why = res[m]
                print("       %-21s %s  %s" % (m, "—" if ok is None else ("đạt" if ok else "TRƯỢT"), why))
    print("\nTheo metric (đạt / số câu áp dụng):")
    for m in METRICS:
        a, b = tally[m]
        print("  %-21s %d/%d" % (m, a, b))
    sug_pass = sum(1 for row in rows if all(v[0] is not False for v in grade_row(row, codes, ids).values()))
    print("Đề xuất code: %d/%d câu đạt mọi mục code kiểm được." % (sug_pass, len(rows)))
    if agree + disagree:
        print("Khớp với cột pass người chấm: %d/%d%s" % (agree, agree + disagree,
              (" · lệch: " + ", ".join(diffs)) if diffs else ""))
    print("Nhớ: code không kiểm hết pass_criterion — người chấm vẫn đọc từng output trước khi điền cột pass.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
