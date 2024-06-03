FROM python:3.11-slim-buster

RUN pip install --upgrade pip

# Install Poetry for dependency management
RUN pip install poetry==1.6.1

# Set environment variables for Poetry
ENV POETRY_NO_INTERACTION=1 \
    POETRY_HOME=/opt/poetry \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR=/tmp/poetry_cache \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /celery_app

COPY . .
RUN touch README.md

# Installing dependencies
RUN poetry install --no-root && rm -rf $POETRY_CACHE_DIR

ENV PYTHONPATH=/celery_app/investor_bulletin
