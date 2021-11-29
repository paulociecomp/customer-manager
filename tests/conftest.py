import pytest
from async_asgi_testclient import TestClient

from app.api.main import app


@pytest.fixture
async def test_client():
    async with TestClient(app) as client:
        yield client
