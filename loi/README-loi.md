# Bài lab lỗi — đọc log để đưa workflow ĐỎ trở lại XANH

Đây là 2 tình huống thường gặp nhất khiến một lần chạy workflow chuyển **ĐỎ**
(mục "Bài lab lỗi" của buổi 7). Với **mỗi** file: chạy nó bằng `pytest`, **đọc kỹ**
thông báo lỗi, tìm nguyên nhân, sửa, rồi chạy lại tới khi **XANH** (pytest báo pass).

```bash
pytest loi/test_loi_1_assert.py    # log sẽ có: AssertionError
pytest loi/test_loi_2_import.py    # log sẽ có: ModuleNotFoundError: No module named '...'
```

| Log báo | Trong CI nghĩa là gì | Hướng sửa |
|---------|----------------------|-----------|
| `AssertionError` (ở bước pytest) | Một **bài kiểm thử không đạt** → job hỏng → workflow ĐỎ | Sửa mã cho đúng để bài kiểm thử đạt |
| `ModuleNotFoundError: No module named 'X'` | Thường do **thiếu thư viện** trong `requirements.txt` nên bước `pip install` không cài nó | Thêm thư viện vào `requirements.txt` (hoặc sửa dòng import cho đúng) |

> **Cách đọc log workflow thật trên GitHub (slide 17):** vào tab **Actions** → chọn
> lần chạy đang **đỏ** → mở **job** bị hỏng → mở **step** báo lỗi → đọc dòng thông
> báo. Đúng như ở đây, thông báo lỗi luôn nói thẳng ra chỗ sai — đừng đoán mò.
