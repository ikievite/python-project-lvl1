FROM python:3.8

RUN pip3 install poetry

COPY . /app

WORKDIR /app

RUN poetry build

RUN pip install dist/*.whl
