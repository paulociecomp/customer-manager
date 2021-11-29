FROM python:3.10

ENV POETRY_VERSION=1.2.0a2

# USER 0
RUN python3 -m pip install --upgrade pip
# USER 1001

# System deps:
RUN pip install "poetry==$POETRY_VERSION"

COPY . /src

WORKDIR /src

RUN poetry config virtualenvs.create false && \
  poetry install --no-dev --no-interaction --no-ansi

ENV ENV_FOR_DYNACONF=production

ARG DATABASE

# CMD ["poetry", "run", "uvicorn", "--host", "0.0.0.0", "--port", $PORT, "--reload", "app.api.main:app"]
CMD poetry run uvicorn --host 0.0.0.0 --port $PORT --reload app.api.main:app