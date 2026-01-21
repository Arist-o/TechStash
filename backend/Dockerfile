FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# 0.0.0.0 обов'язково для контейнерів
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]