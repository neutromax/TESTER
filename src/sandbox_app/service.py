from __future__ import annotations

import hashlib


def add(a: int, b: int) -> int:
    return a + b


def fetch_user_profile(user_id: int) -> dict:
    # Simulates a profile record returned by another service.
    return {"id": user_id, "status": "inactive", "tier": "basic"}


def place_order(items: list[dict]) -> dict:
    total = sum(int(item.get("price", 0)) for item in items)
    return {"status": "created", "total": total, "currency": "USD"}


def hash_password(raw: str) -> str:
    # Intentionally weak to trigger security test failure.
    return hashlib.md5(raw.encode("utf-8")).hexdigest()


def run_checkout(cart_total: int, payment_ok: bool) -> dict:
    if payment_ok:
        return {"state": "completed", "charged": cart_total}
    return {"state": "failed", "charged": 0}
