FROM python:3.7.5-slim

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT behave /app/src/features