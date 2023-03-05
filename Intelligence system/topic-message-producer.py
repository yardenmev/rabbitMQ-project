import pika
from faker import Faker

fake = Faker('iw_IL')
connection_parameters = pika.ConnectionParameters(host='localhost')
with pika.BlockingConnection(connection_parameters) as connection:
    channel = connection.channel()
    channel.exchange_declare(exchange='MyExchange' , exchange_type='topic')
    for x in range(1000):
        phone = fake.phone_number()
        content = fake.paragraph(nb_sentens=1)
        message = f"Message: Number {phone} messaged:{content}"
        key = f'Message.{phone}.{location}'
        channel.basic_publish(exchange='MyExchange',routing_key=key ,body=message.encode('utf-8'))

