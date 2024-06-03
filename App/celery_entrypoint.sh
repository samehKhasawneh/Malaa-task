#!/bin/bash
set -e

# Run database migrations
source start.sh
apply_migrations

# cd  './investor_bulletin/worker'

# sleep 3

# Start the Celery worker in the background
# celery -A celery_app worker --loglevel=info

# should be in a separate image
# # Start the Celery beat scheduler
# celery -A celery_app beat --loglevel=info

# Start the Celery beat scheduler and worker
# for development only
celery -A investor_bulletin.worker.celery_app worker -l info -B
