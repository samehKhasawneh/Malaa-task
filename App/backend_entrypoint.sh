#!/bin/bash
set -e

# Run database migrations
source start.sh
apply_migrations

sleep 3

exec gunicorn -w 4 -k uvicorn.workers.UvicornWorker investor_bulletin.api.main:app --bind 0.0.0.0 --reload

# uvicorn investor_bulletin.api.main:app --host 0.0.0.0 --reload
