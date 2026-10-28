from __future__ import annotations

import pytest

from sandbox_app.service import hash_password


@pytest.mark.security
def test_password_hash_is_not_md5() -> None:
    # Intentional failure: current implementation uses md5.
    hashed = hash_password("Secret@123")
    assert len(hashed) > 32
