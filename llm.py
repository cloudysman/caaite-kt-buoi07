"""LLM GIẢ LẬP cho bài lab buổi 7.

Giống buổi 4: ta cố ý KHÔNG gọi LLM thật (không cần API key, không cần mạng).
Nhờ vậy bài kiểm thử chạy nhanh và ổn định — đúng khuyến nghị ở slide 14:
bắt đầu bằng bài kiểm thử đơn giản, KHÔNG phụ thuộc lời gọi LLM.

Bạn KHÔNG cần sửa file này.
"""


def goi_llm(cau_hoi: str) -> str:
    cau_hoi = (cau_hoi or "").strip()
    if not cau_hoi:
        return "(LLM giả lập) Bạn chưa nhập gì cả."
    return f"(LLM giả lập) Mình đã nhận được câu hỏi: {cau_hoi}"
