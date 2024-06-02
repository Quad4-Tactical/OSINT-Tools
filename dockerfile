FROM python:3.12-slim

WORKDIR /usr/src/app

RUN pip install --no-cache-dir poetry
ENV POETRY_VIRTUALENVS_CREATE=false

COPY pyproject.toml poetry.lock* /usr/src/app/

RUN poetry install --no-root --no-dev

COPY . /usr/src/app/