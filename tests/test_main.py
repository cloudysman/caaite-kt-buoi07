"""Bai kiem thu cho ung dung, con de assert 500 nen pytest do."""
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 500
