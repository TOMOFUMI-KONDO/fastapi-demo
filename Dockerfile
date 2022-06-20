FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-alpine3.10

RUN pip install boto3

COPY ./app /app

ENV PORT=8000