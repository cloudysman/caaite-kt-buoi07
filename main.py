"""Ứng dụng chat FastAPI — bản dùng cho bài lab CI buổi 7.

Điểm mới của buổi này là endpoint /health: một endpoint rất đơn giản dùng để
kiểm tra "ứng dụng có còn sống không". Nó KHÔNG gọi LLM nên kiểm thử chạy nhanh
và ổn định — rất hợp để tự động chạy trong CI (slide 14).

Bạn KHÔNG cần sửa file này. Việc của bạn là VIẾT BÀI KIỂM THỬ cho nó
(xem tests/test_main.py).
"""
from fastapi import FastAPI
from pydantic import BaseModel

import llm

app = FastAPI(title="Chat app — Lab CI buổi 7")


class ChatIn(BaseModel):
    message: str


@app.get("/health")
def health():
    """Endpoint kiểm tra tình trạng: luôn trả về mã 200 khi ứng dụng chạy."""
    return {"status": "ok"}


@app.post("/chat")
def chat(body: ChatIn):
    return {"answer": llm.goi_llm(body.message)}
