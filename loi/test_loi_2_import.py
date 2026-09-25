"""BÀI LAB LỖI 2/2 — THIẾU THƯ VIỆN (workflow ĐỎ ở bước cài đặt / import).

Chạy:  pytest loi/test_loi_2_import.py
ĐỌC log: bạn sẽ thấy "ModuleNotFoundError: No module named 'thu_vien_khong_co'".

Trong CI thật, lỗi này thường có nghĩa: thư viện chưa được khai báo trong
requirements.txt nên bước "pip install" không cài nó → khi chạy pytest thì
import thất bại → workflow ĐỎ. Cách sửa trong CI là THÊM thư viện vào
requirements.txt.

Ở bài tập cục bộ này, hãy sửa dòng import cho trỏ tới một thư viện CÓ THẬT
trong Python (ví dụ: json). Sau khi sửa, chạy lại pytest phải XANH.
"""
import thu_vien_khong_co  # <-- dòng này gây lỗi: không có thư viện tên này


def test_dung_thu_vien():
    assert thu_vien_khong_co is not None
