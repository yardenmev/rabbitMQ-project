import pika
def callback(ch, method, properties, body):
    print(f"Got message: {body.decode('utf-8')}")   

connection_parameters = pika.ConnectionParameters(host='localhost')
with pika.BlockingConnection(connection_parameters) as connection:
    channel = connection.channel()
    channel.exchange_declare(exchange='MyExchange', exchange_type='fanout')
    channel.queue_declare(queue='MyQueue')
    channel.queue_bind(exchange='MyExchange', queue='MyQueue')
    channel.basic_consume(queue='MyQueue',on_message_callback=callback,auto_ack=True)
    channel.start_consuming()