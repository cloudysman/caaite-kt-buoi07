"""Chạy CI CỤC BỘ + tự chấm cho bài lab buổi 7.

Script này bắt chước đúng các bước trong .github/workflows/ci.yml để bạn thấy
cơ chế "đỏ / xanh" NGAY TRÊN MÁY, chưa cần push lên GitHub. Khi mọi bước đều
XANH ở đây thì đẩy lên GitHub gần như chắc chắn cũng XANH.

Chạy:  python chay_ci.py
"""
import os
import sys
import subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
CI_PATH = os.path.join(ROOT, ".github", "workflows", "ci.yml")

XANH, DO = "XANH", "ĐỎ"


def in_buoc(ten, ok, chi_tiet=""):
    print(f"[{XANH if ok else DO:>4}] {ten}")
    if chi_tiet:
        for dong in chi_tiet.strip().splitlines():
            print("        " + dong)
    return ok


def kiem_tra_ci_yml():
    """Bước 0 — ci.yml tồn tại, hợp lệ, và có đủ step bắt buộc."""
    if not os.path.exists(CI_PATH):
        return in_buoc("Bước 0 — có .github/workflows/ci.yml", False,
                       "Chưa thấy file. Xem README - Bước 1.")
    noi_dung = open(CI_PATH, encoding="utf-8").read()

    yaml_msg = ""
    try:
        import yaml
        yaml.safe_load(noi_dung)
    except ImportError:
        yaml_msg = "(bỏ qua kiểm tra cú pháp YAML vì chưa cài pyyaml)"
    except Exception as e:
        return in_buoc("Bước 0 — ci.yml đúng cú pháp YAML", False, f"YAML lỗi: {e}")

    # Bỏ phần chú thích (từ dấu # trở đi) trên mỗi dòng, để không bị nhầm
    # các chữ 'pytest'/'docker build' nằm trong lời hướng dẫn TODO là đã làm.
    code = "\n".join(dong.split("#", 1)[0] for dong in noi_dung.splitlines())
    thieu = []
    if "pytest" not in code:
        thieu.append("Thiếu step chạy 'pytest' (TODO 2 trong ci.yml).")
    if "docker build" not in code:
        thieu.append("Thiếu step 'docker build' (TODO 3 trong ci.yml).")

    ok = not thieu
    return in_buoc("Bước 0 — ci.yml có đủ step bắt buộc", ok,
                   (yaml_msg + "\n" + "\n".join(thieu)).strip())


def chay_pytest():
    """Bước 1 — chạy pytest (đây chính là cơ chế đỏ/xanh, slide 15)."""
    try:
        kq = subprocess.run(
            [sys.executable, "-m", "pytest", "-q"],
            cwd=ROOT, capture_output=True, text=True,
            encoding="utf-8", errors="replace",
        )
    except FileNotFoundError:
        return in_buoc("Bước 1 — chạy kiểm thử (pytest)", False,
                       "Chưa cài pytest? Chạy: pip install -r requirements.txt")
    ok = kq.returncode == 0
    log = ((kq.stdout or "") + (kq.stderr or "")).strip().splitlines()
    tom_tat = "\n".join(log[-15:]) if log else "(không có output)"
    return in_buoc("Bước 1 — chạy kiểm thử (pytest)", ok, tom_tat)


def main():
    print("=" * 60)
    print("  CHẠY CI CỤC BỘ — BÀI LAB BUỔI 7")
    print("=" * 60)
    b0 = kiem_tra_ci_yml()
    b1 = chay_pytest()
    print("-" * 60)
    if b0 and b1:
        print(f"  KẾT QUẢ: {XANH} — mọi bước đạt!")
        print("  Tiếp theo: push lên GitHub và xem tab Actions (README - Bước 4),")
        print("  rồi làm BÀI LAB LỖI trong thư mục loi/ (README - Bước 5).")
    else:
        print(f"  KẾT QUẢ: {DO} — đọc log ở trên, tìm nguyên nhân, sửa rồi chạy lại.")
    print("=" * 60)


if __name__ == "__main__":
    main()
