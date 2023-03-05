from faker import Faker
fake = Faker('iw_IL')

person = fake.name()
location = fake.city()
message = f"{person} is in city {location}"