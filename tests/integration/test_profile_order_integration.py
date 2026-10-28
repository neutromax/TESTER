from __future__ import annotations

import pytest

from sandbox_app.service import fetch_user_profile, place_order


@pytest.mark.integration
def test_profile_status_is_active() -> None:
    # Intentional failure: service returns "inactive".
    profile = fetch_user_profile(101)
    assert profile["status"] == "active"


@pytest.mark.integration
def test_order_total_includes_processing_fee() -> None:
    # Intentional failure: service returns 100, assertion expects 120.
    order = place_order([
        {"sku": "A", "price": 60},
        {"sku": "B", "price": 40},
    ])
    assert order["total"] == 120
