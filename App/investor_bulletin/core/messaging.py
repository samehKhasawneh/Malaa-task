import os
from amqpstorm import Connection

RABBITMQ_HOST = os.environ['RABBITMQ_HOST']
RABBITMQ_USER = os.environ['RABBITMQ_USER']
RABBITMQ_PASSWORD = os.environ['RABBITMQ_PASSWORD']

def publish_message(exchange, routing_key, message):
    with Connection(RABBITMQ_HOST, RABBITMQ_USER, RABBITMQ_PASSWORD) as connection:
        channel = connection.channel()
        channel.exchange.declare(exchange, 'topic')
        channel.basic.publish(body=message, routing_key=routing_key, exchange=exchange)
        channel.close()

if __name__ == "__main__":
    publish_message('alerts_exchange', 'threshold.alert', 'Threshold alert triggered!')
