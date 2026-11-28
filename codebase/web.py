"""Giao diện web demo DamageCheck — chỉ thư viện chuẩn.

Chạy:  python codebase/web.py            → mở http://localhost:8000
       python codebase/web.py --port 8080

Gọi ĐÚNG luồng của bản chạy thử: answer(text) trong codebase/agent.py, ghi trace qua tracing như codebase/app.py.
Không có nút gửi tin / hoàn tiền: giao diện chỉ hiện kết luận, căn cứ và BẢN NHÁP để chủ shop tự sao chép.
`python run.py` (khung) vẫn là lệnh chạy bản chạy thử chính thức; file này chỉ thêm giao diện để demo.
"""
import csv
import json
import os
import re
import sys
import threading
import time
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import ai  # noqa: E402
import tools  # noqa: E402
import tracing  # noqa: E402
from agent import ORDER_ID, answer  # noqa: E402

PAGE = os.path.join(HERE, "web", "index.html")
LOCK = threading.Lock()  # tracing ghi theo một "câu" toàn cục → mỗi lúc chỉ xử lý một câu hỏi


# ---------- dữ liệu cho giao diện ----------

def order_summary(oid):
    o = tools.ORDERS[oid]
    claim = o.get("customer_claim") or {}
    has_logs = bool(o.get("packing_log")) or bool(o.get("shipping_log"))
    return {
        "id": oid, "product": o.get("product"), "value_vnd": o.get("value_vnd"),
        "carrier": o.get("carrier"),
        "carrier_name": tools.CARRIERS.get(o.get("carrier") or "", {}).get("name") if o.get("carrier") else None,
        "has_packing": bool(o.get("packing_log")), "n_shipping": len(o.get("shipping_log") or []),
        "source": "synthetic" if has_logs else "review",
        "claim": claim.get("text", ""),
    }


def order_detail(oid):
    oid = (oid or "").strip().upper()
    if oid not in tools.ORDERS:
        return None
    o = tools.ORDERS[oid]
    d = order_summary(oid)
    d.update(packing=o.get("packing_log") or None, shipping=o.get("shipping_log") or [],
             claim_full=o.get("customer_claim") or None,
             deadline=tools.check_claim_deadline.__wrapped__(oid) if hasattr(tools.check_claim_deadline, "__wrapped__")
             else tools.check_claim_deadline(oid))
    return d


def read_run(n):
    path = os.path.join(ROOT, "eval", "run-%d.csv" % n)
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        return None
    graded = [r for r in rows if (r.get("pass") or "").strip() in ("0", "1")]
    by_type = {}
    for r in rows:
        t = by_type.setdefault(r.get("type", ""), {"pass": 0, "total": 0})
        t["total"] += 1
        t["pass"] += 1 if (r.get("pass") or "").strip() == "1" else 0
    return {
        "run_id": rows[0].get("run_id"), "model": rows[0].get("model"), "total": len(rows),
        "graded": len(graded), "pass": sum(1 for r in rows if (r.get("pass") or "").strip() == "1"),
        "by_type": by_type, "failed": [r["id"] for r in rows if (r.get("pass") or "").strip() == "0"],
    }


def read_cost():
    path = os.path.join(ROOT, "cost", "simulate-1-summary.md")
    if not os.path.exists(path):
        return None
    out = {"rows": [], "run_id": None, "rate": None}
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.startswith("# "):
                m = re.search(r"(simulate-\d+@\S+)", line)
                out["run_id"] = m.group(1) if m else None
            if line.startswith("Tỉ lệ đạt"):
                out["rate"] = line.split(":", 1)[1].strip()
            if line.startswith("| gemini") or line.startswith("| claude") or line.startswith("| gpt"):
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                if len(cells) >= 8:
                    out["rows"].append({"model": cells[0], "per_session": cells[1], "per_success": cells[2],
                                        "month_low": cells[4], "month_base": cells[5], "month_high": cells[6],
                                        "per_user_month": cells[7]})
    return out


def read_scenarios():
    path = os.path.join(ROOT, "eval", "benchmark.csv")
    with open(path, encoding="utf-8-sig") as f:
        rows = {r["id"]: r for r in csv.DictReader(f)}
    picks = [("B01", "Ca thường — lỗi vận chuyển"), ("B02", "Ca thường — lỗi đóng gói"),
             ("B03", "Khách đã đồng kiểm"), ("K02", "Bằng chứng mâu thuẫn"), ("K01", "Thiếu bằng chứng"),
             ("B06", "Đã quá hạn khiếu nại"), ("K07", "Một tin, hai đơn"), ("K03", "Không có mã đơn"),
             ("K06", "Chủ shop dẫn dắt"), ("T01", "Ngoài phạm vi — sai màu"), ("T04", "Tấn công: lệnh chèn"),
             ("R02", "Đơn thật — chỉ có lời khách")]
    return [{"id": i, "label": lab, "type": rows[i]["type"], "input": rows[i]["input"]} for i, lab in picks if i in rows]


def config():
    return {"provider": ai.MODEL_PROVIDER, "model": ai.MODEL_NAME or ("fake" if ai.MODEL_PROVIDER == "fake" else ""),
            "fake": ai.MODEL_PROVIDER == "fake", "today": tools._today().isoformat()}


def ask(text):
    with LOCK:
        tracing.begin("web")
        t0 = time.perf_counter()
        try:
            result = answer(text)
            err = None
        except Exception as e:  # lỗi gọi model: trả về cho giao diện hiện
            result, err = {"output": ""}, "%s: %s" % (type(e).__name__, e)
        summary, events = tracing.end()
    ids = []
    for m in ORDER_ID.finditer(text or ""):
        oid = "DH" + m.group(1)
        if oid not in ids:
            ids.append(oid)
    steps = []
    for e in events:
        if e["kind"] == "tool":
            steps.append({"kind": "tool", "name": e["name"], "input": e.get("input", ""), "ms": int(1000 * (e.get("latency_s") or 0))})
        elif e["kind"] == "model":
            steps.append({"kind": "model", "name": e.get("model") or "model", "ms": int(1000 * (e.get("latency_s") or 0)),
                          "tokens_in": e.get("tokens_in", 0), "tokens_out": e.get("tokens_out", 0), "error": e.get("error")})
        elif e["kind"] == "note":
            steps.append({"kind": "note", "text": e.get("text", "")})
    return {"output": (result or {}).get("output", ""), "error": err, "summary": summary, "steps": steps,
            "order_ids": ids, "elapsed_ms": int(1000 * (time.perf_counter() - t0))}


# ---------- máy chủ ----------

class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):  # gọn terminal
        sys.stderr.write("  %s\n" % (fmt % args))

    def _send(self, code, body, ctype):
        data = body.encode("utf-8") if isinstance(body, str) else body
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def _json(self, obj, code=200):
        self._send(code, json.dumps(obj, ensure_ascii=False), "application/json; charset=utf-8")

    def do_GET(self):
        u = urlparse(self.path)
        if u.path in ("/", "/index.html"):
            with open(PAGE, encoding="utf-8") as f:
                return self._send(200, f.read(), "text/html; charset=utf-8")
        if u.path == "/api/orders":
            return self._json({"orders": [order_summary(k) for k in sorted(tools.ORDERS)], "config": config(),
                               "scenarios": read_scenarios()})
        if u.path == "/api/order":
            d = order_detail(parse_qs(u.query).get("id", [""])[0])
            return self._json(d) if d else self._json({"error": "không có đơn"}, 404)
        if u.path == "/api/stats":
            return self._json({"runs": [r for r in (read_run(1), read_run(2)) if r], "cost": read_cost(), "config": config()})
        self._json({"error": "không có"}, 404)

    def do_POST(self):
        if urlparse(self.path).path != "/api/ask":
            return self._json({"error": "không có"}, 404)
        n = int(self.headers.get("Content-Length") or 0)
        try:
            text = (json.loads(self.rfile.read(n).decode("utf-8")) or {}).get("text", "")
        except Exception:
            return self._json({"error": "body phải là JSON {\"text\": ...}"}, 400)
        if not text.strip():
            return self._json({"error": "câu hỏi trống"}, 400)
        self._json(ask(text[:2000]))


def main(argv):
    port = 8000
    if "--port" in argv:
        port = int(argv[argv.index("--port") + 1])
    srv = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    url = "http://localhost:%d" % port
    c = config()
    print("DamageCheck — giao diện demo: %s" % url)
    print("Model: %s · ngày xử lý khiếu nại: %s%s" % (c["model"] or c["provider"], c["today"],
          "  (CHẾ ĐỘ GIẢ — điền .env để gọi model thật)" if c["fake"] else ""))
    print("Dừng: Ctrl+C")
    if "--no-browser" not in argv:
        threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
