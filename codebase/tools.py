"""Công cụ của DamageCheck — mỗi công cụ một hàm @tool. Thiết kế: spec.md §4.

Tất cả công cụ CHỈ ĐỌC data/orders.json hoặc tính toán — không gửi tin, không sửa dữ liệu, không hoàn tiền,
không gửi khiếu nại. Bản nháp do model soạn trong agent.py; chủ shop duyệt rồi tự gửi.
Mã căn cứ theo quy ước của data/orders.json: DG-<đơn> · VC-<đơn>-<n> · KH-<đơn>.
"""
import datetime
import json
import os

from tracing import tool, TOOLS  # noqa: F401

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(ROOT, "data", "orders.json"), encoding="utf-8") as _f:
    _DATA = json.load(_f)
ORDERS = {o["order_id"].upper(): o for o in _DATA["orders"]}
CARRIERS = _DATA.get("carriers", {})


def _order(order_id):
    return ORDERS.get((order_id or "").strip().upper())


def _today():
    """Ngày xử lý khiếu nại. Mặc định là hôm nay; đặt DAMAGECHECK_TODAY=YYYY-MM-DD để chạy lại đúng một ngày."""
    s = os.environ.get("DAMAGECHECK_TODAY", "").strip()
    return datetime.date.fromisoformat(s) if s else datetime.date.today()


@tool
def get_order(order_id: str) -> dict:
    """get_order · input: mã đơn (vd "DH01") · output: {"found": True, "order_id", "product", "fragile",
    "value_vnd", "carrier", "carrier_name"} hoặc {"found": False} · không tác động ra ngoài."""
    o = _order(order_id)
    if not o:
        return {"found": False}
    return {"found": True, "order_id": o["order_id"], "product": o["product"], "fragile": o["fragile"],
            "value_vnd": o["value_vnd"], "carrier": o["carrier"],
            "carrier_name": CARRIERS.get(o["carrier"], {}).get("name", o["carrier"])}


@tool
def get_packing_log(order_id: str) -> dict:
    """get_packing_log · input: mã đơn · output: log đóng gói {"id": "DG-…", "time", "packed_by", "materials",
    "video", "check_note"} — {} nếu không có · không tác động ra ngoài."""
    o = _order(order_id)
    return dict(o["packing_log"]) if o else {}


@tool
def get_shipping_log(order_id: str) -> list:
    """get_shipping_log · input: mã đơn · output: danh sách sự kiện {"id": "VC-…-n", "time", "status", "note"}
    — [] nếu không có · không tác động ra ngoài."""
    o = _order(order_id)
    return [dict(e) for e in o["shipping_log"]] if o else []


@tool
def get_customer_claim(order_id: str) -> dict:
    """get_customer_claim · input: mã đơn · output: khiếu nại {"id": "KH-…", "time", "text",
    "photo_description"} — lời khách kể, chưa kiểm chứng; {} nếu không có · không tác động ra ngoài."""
    o = _order(order_id)
    return dict(o["customer_claim"]) if o else {}


@tool
def check_claim_deadline(order_id: str) -> dict:
    """check_claim_deadline · input: mã đơn · output: {"carrier", "delivered", "deadline", "today", "days_left",
    "expired"} — hạn khiếu nại đơn vị vận chuyển = ngày giao thành công + claim_deadline_days (data/orders.json),
    so với ngày xử lý; {"known": False} nếu thiếu ngày giao hoặc thiếu điều kiện của hãng · không tác động ra ngoài."""
    o = _order(order_id)
    if not o:
        return {"known": False}
    rule = CARRIERS.get(o["carrier"], {})
    delivered = next((e["time"][:10] for e in o["shipping_log"] if "giao thành công" in e["status"]), None)
    if not delivered or "claim_deadline_days" not in rule:
        return {"known": False, "carrier": o["carrier"]}
    d = datetime.date.fromisoformat(delivered)
    deadline = d + datetime.timedelta(days=rule["claim_deadline_days"])
    today = _today()
    return {"known": True, "carrier": o["carrier"], "limit_days": rule["claim_deadline_days"],
            "delivered": d.isoformat(), "deadline": deadline.isoformat(), "today": today.isoformat(),
            "days_left": (deadline - today).days, "expired": today > deadline}
