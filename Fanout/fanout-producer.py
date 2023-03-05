import pika
from faker import Faker


connection_parameters = pika.ConnectionParameters(host='localhost')
with pika.BlockingConnection(connection_parameters) as connection:
    channel = connection.channel()
    channel.exchange_declare(exchange='MyExchange', exchange_type='fanout')
    # channel.queue_declare(queue='person-data')
    for x in range(100):
        fake = Faker('iw_IL')
        person = fake.name()
        location = fake.city()
        message = f"{person} is in city {location}"
        channel.basic_publish(exchange='MyExchange',routing_key='',body=message.encode('utf-8'))

