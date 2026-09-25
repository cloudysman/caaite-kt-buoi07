"""BÀI LAB LỖI 1/2 — BÀI KIỂM THỬ KHÔNG ĐẠT (workflow ĐỎ).

Chạy:  pytest loi/test_loi_1_assert.py
ĐỌC log: bạn sẽ thấy dòng "AssertionError" và giá trị thực tế vs mong đợi.
Trong CI thật: một bài kiểm thử fail như thế này làm cả lần chạy chuyển ĐỎ.

Nhiệm vụ: tìm dòng assert SAI dưới đây và sửa cho ĐẠT (rồi pytest sẽ XANH).
"""


def cong(a, b):
    return a + b


def test_cong():
    # Câu này SAI: 2 + 2 = 4, không phải 5. Hãy sửa số mong đợi cho đúng.
    assert cong(2, 2) == 5
