from celery import Celery

celery_app = Celery(
    'investor_bulletin',
    broker='amqp://guest:guest@broker:5672/',
    backend='rpc://',
    include=['worker.tasks']
)

celery_app.conf.beat_schedule = {
    'fetch-market-data': {
        'task': 'worker.tasks.fetch_market_data',
        'schedule': 300.0,
    },
}

celery_app.conf.timezone = 'UTC'
