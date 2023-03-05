import pika
from faker import Faker

fake = Faker('iw_IL')
connection_parameters = pika.ConnectionParameters(host='localhost')
with pika.BlockingConnection(connection_parameters) as connection:
    channel = connection.channel()
    channel.exchange_declare(exchange='MyExchange' , exchange_type='direct')
    for x in range(1000):
        person = fake.name()
        location = fake.city()
        message = f"{person} is in city {location}"
        channel.basic_publish(exchange='MyExchange',routing_key=location ,body=message.encode('utf-8'))

