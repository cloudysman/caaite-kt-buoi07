# Bài lab buổi 7 — Để GitHub tự kiểm thử và build mỗi khi push (CI)

> **Mục tiêu:** Viết một workflow GitHub Actions (`ci.yml`) tự động chạy **pytest** và **build image** mỗi khi push; viết bài kiểm thử; và đạt một lần chạy workflow **XANH**.
> **Thời lượng:** 1 giờ 30 phút · Làm **cá nhân** · **Không cần AI, không cần API key.**

Đọc **`DE-BAI.txt`** trước để hiểu bối cảnh và nhiệm vụ. File này là hướng dẫn **từng bước**.

---

## Từ vựng cần nắm (dùng nhất quán cả buổi)

| Từ | Nghĩa |
|----|-------|
| **workflow** | Toàn bộ quy trình tự động, mô tả trong 1 tập tin (`ci.yml`) |
| **job** | Một nhóm việc trong workflow |
| **step** | Một bước trong job, chạy lần lượt |
| **runner** | Máy do GitHub cấp để chạy job |
| **trigger** | Điều kiện để workflow chạy (ví dụ: `push`, `pull_request`) |
| **đỏ / xanh** | Trạng thái lần chạy: **đỏ** = có lỗi, **xanh** = thành công |

---

## Bảng phân bổ thời gian (tổng 90 phút)

| Bước | Nội dung | Thời gian |
|------|----------|-----------|
| 0 | Chuẩn bị: cài thư viện, xem cấu trúc dự án | 10 phút |
| 1 | Hoàn thiện `ci.yml` (thêm các step còn thiếu) | 20 phút |
| 2 | Viết bài kiểm thử, chạy `pytest` thấy **đỏ → xanh** | 20 phút |
| 3 | Chạy CI cục bộ tự chấm (`chay_ci.py`) | 15 phút |
| 4 | Push lên GitHub, xem tab **Actions** ra màu xanh | 10 phút |
| 5 | **Bài lab lỗi**: đọc log, sửa 2 lỗi cho xanh | 15 phút |

---

## Bước 0 — Chuẩn bị (10 phút)

Cài thư viện (nên dùng môi trường ảo như các buổi trước):

```bash
pip install -r requirements.txt
```

Xem qua cấu trúc: `main.py` (có endpoint `/health`), `tests/test_main.py` (khung bài kiểm thử — đang đỏ), `.github/workflows/ci.yml` (khung workflow — thiếu step), `chay_ci.py` (chạy CI cục bộ để tự chấm).

---

## Bước 1 — Hoàn thiện `ci.yml` (20 phút)

Mở `.github/workflows/ci.yml`. GitHub Actions đọc mọi file trong thư mục `.github/workflows`. File này khai báo một workflow gồm 5 step theo đúng slide 11:

1. **checkout** – lấy mã nguồn về runner *(đã có)*
2. **setup** – cài Python *(đã có)*
3. **cài thư viện** – `pip install -r requirements.txt` *(đã có)*
4. **chạy kiểm thử** – `pytest` → **TODO 2 (bạn thêm)**
5. **build image** – `docker build` → **TODO 3 (bạn thêm)**

Và **TODO 1**: thêm trigger `pull_request:` để workflow cũng chạy khi mở pull request (slide 9 — pull request đã học ở buổi 1).

> **Chú ý thụt lề (indent) trong YAML:** mỗi step bắt đầu bằng `- run:` phải thẳng hàng với các step `- uses:` có sẵn. Sai indent là YAML lỗi cú pháp.

---

## Bước 2 — Viết bài kiểm thử: từ ĐỎ sang XANH (20 phút)

Mở `tests/test_main.py`. Bài kiểm thử `test_health` đang **cố ý sai** (`assert ... == 500`). Chạy thử để tận mắt thấy **đỏ**:

```bash
pytest
```

Bạn sẽ thấy `AssertionError` (200 khác 500). Đây chính là cơ chế **đỏ** ở slide 15: một bài kiểm thử không đạt → job hỏng → workflow đỏ.

Bây giờ **sửa** `500` → `200` (vì `/health` phải trả về mã 200) rồi chạy lại:

```bash
pytest
```

Khi thấy `1 passed` (xanh) là bạn đã hiểu cơ chế **đỏ → xanh**.

> **Vì sao kiểm thử `/health` mà không kiểm thử `/chat`?** `/health` không gọi LLM nên chạy nhanh, ổn định — hợp để chạy tự động trong CI (slide 14). Kiểm thử endpoint gọi LLM cần kỹ thuật thay thế lời gọi, để dành nâng cao.

---

## Bước 3 — Chạy CI cục bộ để tự chấm (15 phút)

Trước khi push, hãy chạy CI **ngay trên máy** để chắc chắn sẽ xanh:

```bash
python chay_ci.py
```

Script bắt chước đúng các bước trong `ci.yml`:
- **Bước 0**: kiểm tra `ci.yml` hợp lệ và đã có đủ step `pytest` + `docker build`.
- **Bước 1**: chạy `pytest` và báo **ĐỎ/XANH**.

Khi thấy **`KẾT QUẢ: XANH`** là phần chính đã xong. ✅

---

## Bước 4 — Push lên GitHub và xem tab Actions (10 phút)

Đây là bước "thật" — trải nghiệm CI đúng nghĩa:

```bash
git add .
git commit -m "Them CI: pytest + build image"
git push
```

Lên GitHub → tab **Actions** → chọn lần chạy vừa xong. Bạn sẽ thấy workflow tự chạy và (nếu cục bộ đã xanh) kết quả **màu xanh**.

> Nếu chưa có repo trên GitHub: tạo một repository trống rồi làm theo hướng dẫn "push an existing repository". Nếu không kịp/không có mạng, **`chay_ci.py` xanh là đủ để coi như đạt phần chính**, bước push có thể làm ở nhà.

---

## Bước 5 — Bài lab lỗi: đọc log để đưa ĐỎ về XANH (15 phút)

Trong thư mục `loi/` có **2 tình huống làm workflow đỏ** (mục "Bài lab lỗi"). Với mỗi file: chạy → **đọc kỹ** log → tìm nguyên nhân → sửa → chạy lại đến khi xanh.

```bash
pytest loi/test_loi_1_assert.py   # log: AssertionError  (bài kiểm thử không đạt)
pytest loi/test_loi_2_import.py   # log: ModuleNotFoundError  (thiếu thư viện)
```

Xem `loi/README-loi.md` để biết mỗi log tương ứng với lỗi CI nào và hướng sửa. **Trọng tâm: đọc đúng từng dòng log, đừng đoán mò** — đây là kỹ năng quan trọng nhất của buổi 7 và là nền cho cổng kiểm định 2 (buổi 8).

---

## Checkpoint cuối buổi (điều kiện ĐẠT)

- [ ] `ci.yml` chạy `pytest` và `docker build` mỗi khi push (và khi mở pull request).
- [ ] Có ít nhất một bài kiểm thử và nó **đạt**.
- [ ] Đạt một lần chạy workflow **xanh** (`chay_ci.py` xanh, và/hoặc tab Actions xanh).
- [ ] Sửa xong cả 2 lỗi trong `loi/`.

> Buổi 7 mới là phần **CI**. Phần **CD** (tự động triển khai) và **cổng kiểm định 2** nằm ở **buổi 8**.

---

## Cấu trúc thư mục

```
lab-7/
├── DE-BAI.txt                     # Bối cảnh + đề bài (đọc trước tiên)
├── README.md                      # Hướng dẫn từng bước (file này)
├── requirements.txt
├── pytest.ini                     # chỉ chạy tests/ khi gõ "pytest"
├── Dockerfile                     # để bước build image có cái mà build
├── main.py                        # FastAPI: /health, /chat (không cần sửa)
├── llm.py                         # LLM giả lập (không cần sửa)
├── chay_ci.py                     # CHẠY CI CỤC BỘ + tự chấm (đỏ/xanh)
├── tests/
│   └── test_main.py               # TODO: viết test_health (đang cố ý đỏ)
├── .github/workflows/
│   └── ci.yml                     # TODO: thêm step pytest + build + trigger
├── loi/                           # Bài lab lỗi — 2 tình huống làm đỏ
│   ├── README-loi.md
│   ├── test_loi_1_assert.py
│   └── test_loi_2_import.py
└── giai/                          # ĐÁP ÁN — chỉ mở khi đã tự làm xong
    ├── DAP-AN.txt
    ├── ci_giai.yml
    └── test_main_giai.py
```

## Nếu bị kẹt

- Đọc lại đúng dòng log — 90% câu trả lời nằm ở đó.
- `python chay_ci.py` chỉ ra bước nào đỏ và vì sao.
- Cùng đường thì mở `giai/DAP-AN.txt` để đối chiếu — nhưng hãy tự làm trước.
