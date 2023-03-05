import pika
def callback(ch, method, properties, body):
    print(f"Got message: {body.decode('utf-8')}")   

connection_parameters = pika.ConnectionParameters(host='localhost')
with pika.BlockingConnection(connection_parameters) as connection:
    channel = connection.channel()
    channel.basic_consume(queue='person-data',on_message_callback=callback,auto_ack=True)
    channel.start_consuming()