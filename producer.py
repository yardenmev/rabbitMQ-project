import pika
connection_parameters = pika.ConnectionParameters(host='localhost')
with pika.BlockingConnection(connection_parameters) as connection:
    channel = connection.channel()
    channel.queue_declare(queue='helloWorldQueue')
    channel.basic_publish(exchange='',routing_key='helloWorldQueue',body=b'Hello World!')