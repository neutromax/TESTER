from __future__ import annotations

import pytest

from sandbox_app.service import run_checkout


@pytest.mark.e2e
def test_checkout_succeeds_with_failed_payment() -> None:
    # Intentional failure: payment_ok=False returns failed state.
    result = run_checkout(cart_total=250, payment_ok=False)
    assert result["state"] == "completed"
