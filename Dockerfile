FROM python:3.7.5-slim

COPY . /app
WORKDIR /app

RUN python setup.py install

ENTRYPOINT behave /app/features