# Sử dụng Python base image
FROM python:3.11-slim

# Cài pip và các công cụ cần thiết
RUN pip install --upgrade pip

# Thiết lập thư mục làm việc
WORKDIR /app

# Copy file requirements và cài đặt thư viện
COPY app/requirements.txt .

RUN pip install -r requirements.txt

# Copy toàn bộ mã nguồn vào container
COPY ./app ./app
COPY ./*.csv ./
# Chạy FastAPI với Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]