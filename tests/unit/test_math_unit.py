from __future__ import annotations

import pytest

from sandbox_app.service import add


@pytest.mark.unit
def test_add_negative_numbers() -> None:
    # Intentional failure: actual value is -5.
    assert add(-2, -3) == -6
