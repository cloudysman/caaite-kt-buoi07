# Dockerfile tối giản — dùng để bước "build image" trong CI có cái mà build.
# (Dockerfile các bạn đã viết ở buổi 5; đây là bản gọn cho bài lab CI.)
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
