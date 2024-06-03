import os
from pika import BlockingConnection, PlainCredentials, ConnectionParameters

RABBITMQ_HOST = os.environ['RABBITMQ_HOST']
RABBITMQ_USER = os.environ['RABBITMQ_USER']
RABBITMQ_PASSWORD = os.environ['RABBITMQ_PASSWORD']

def init_subscriber():
  credentials = PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)
  connection = BlockingConnection(ConnectionParameters(host=RABBITMQ_HOST, credentials=credentials))

  return connection

def on_event(ch, method, properties, body):
    message = body.decode()
    print(f"Creating event record for message: {message}")

if __name__ == "__main__":
    connection = init_subscriber()
    channel = connection.channel()
    channel.exchange_declare(exchange='alerts_exchange', exchange_type='topic')
    queue_result = channel.queue_declare(queue='', exclusive=True)
    queue_name = queue_result.method.queue

    channel.queue_bind(exchange='alerts_exchange', queue=queue_name, routing_key='threshold.alert')

    channel.basic_consume(queue=queue_name, on_message_callback=on_event, auto_ack=True)
    channel.start_consuming()
