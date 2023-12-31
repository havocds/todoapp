FROM python:3.11.6-slim as base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.7.1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /tmp

RUN pip install poetry==${POETRY_VERSION}

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export --without-hashes --without dev -f requirements.txt --output requirements.txt && \
    rm -rf ${POETRY_CACHE_DIR}

FROM python:3.11.6-slim

WORKDIR /todoapp

COPY --from=base /tmp/requirements.txt /todoapp/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /todoapp/requirements.txt

COPY ./src /todoapp

CMD ["uvicorn", "todoapp.main:app", "--host", "0.0.0.0", "--port", "8000"]