# 1. 构建阶段（含编译）
FROM python:3.12-slim as builder
WORKDIR /app
COPY requirements.lock .
RUN apt-get update && apt-get install -y build-essential \
 && pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.lock

# 2. 运行阶段（最小镜像）
FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
COPY --from=builder /wheels /wheels
RUN pip install --no-cache /wheels/* && rm -rf /wheels
COPY ./start .
CMD ["gunicorn", "start.wsgi:application", "-b", "0.0.0.0:8000", "-w", "4"]