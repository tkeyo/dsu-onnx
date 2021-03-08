FROM tiangolo/uvicorn-gunicorn:python3.8-slim

LABEL version="1.0.0"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir fastapi onnxruntime uvicorn

COPY ./ .

ENTRYPOINT ["sh"]

# docker run -it --rm -p 8001:8001 dsu-onnx:latest -c "uvicorn main:app --host 0.0.0.0 --port 8001 --reload"