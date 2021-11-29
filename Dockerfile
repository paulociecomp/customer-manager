FROM python:3.10

ENV POETRY_VERSION=1.2.0a2

# USER 0
RUN python3 -m pip install --upgrade pip
# USER 1001

# System deps:
RUN pip install "poetry==$POETRY_VERSION"

COPY . /src

WORKDIR /src

RUN poetry install

ARG ENV_FOR_DYNACONF

ARG DATABASE

CMD ["poetry", "run", "uvicorn", "--host", "0.0.0.0", "--port", "6100", "--reload", "app.api.main:app"]

EXPOSE 6100