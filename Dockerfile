FROM python:3.12-slim

WORKDIR /app/

RUN pip install --no-cache-dir poetry

ENV POETRY_VIRTUALENVS_CREATE=false

COPY pyproject.toml poetry.lock* /app/

RUN poetry install --no-root

RUN mkdir /app/videos /app/temp

COPY . /app/

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]