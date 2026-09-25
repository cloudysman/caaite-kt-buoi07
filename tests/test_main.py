"""Bài kiểm thử cho ứng dụng — bản DANG DỞ (CỐ Ý ĐỎ để bạn sửa cho XANH).

Chạy kiểm thử:
    pytest
Hoặc chạy CI cục bộ (khuyến nghị):
    python chay_ci.py
"""
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")

    # ┌── TODO (BẠN LÀM) ───────────────────────────────────────────────┐
    # │ Endpoint /health phải trả về mã 200. Dòng dưới ĐANG CỐ Ý SAI     │
    # │ (đặt 500) để bạn tận mắt thấy pytest báo "đỏ".                    │
    # │ Hãy sửa 500 -> 200 rồi chạy lại: pytest phải "xanh".             │
    # │ (Nâng cao — không bắt buộc: kiểm tra thêm response.json().)       │
    # └──────────────────────────────────────────────────────────────┘
    assert response.status_code == 500
