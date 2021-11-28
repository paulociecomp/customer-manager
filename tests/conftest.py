import pytest
from fastapi.testclient import TestClient

from app.api.main import app


@pytest.fixture
def test_client():
    with TestClient(app) as client:
        yield client
