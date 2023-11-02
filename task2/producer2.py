from faker import Faker
from random import choice
from conn2 import connect_to_mongodb, get_rabbitmq_channel
from model2 import Contact

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

fake = Faker('uk_UA')

# Підключення до MongoDB
connect_to_mongodb()

# Отримання каналу RabbitMQ
connection_r = get_rabbitmq_channel()
connection_r.queue_declare(queue='Go2')

contacts = []  # Створюємо список для збереження контактів

for _ in range(5):  # Цей цикл створить 5 контактів
    fake_contact = {
        'full_name': fake.name(),
        'email': fake.email(),
        'phone_number': fake.phone_number(),
        'choice_for_message': choice(['email', 'sms']),
        'send_email': False,
        'send_sms': False
    }

    contact = Contact(**fake_contact)
    contacts.append(contact)  # Додаємо контакт до списку замість збереження в базі даних в циклі

for contact in contacts:
    try:
        contact.save()  # Зберігаємо фейковий контакт у базі даних
        logger.info("Фейковий контакт збережено в базі даних")
    except Exception as e:
        logger.error(f"Помилка збереження контакту: {e}")

    try:
        connection_r.basic_publish(exchange='', routing_key='Go2', body='Hello World!'.encode())  # Відправляємо усі контакти до черги 'Go2'
        logger.info("Повідомлення відправлено в чергу 'Go2'")
    except Exception as e:
        logger.error(f"Помилка відправки повідомлення: {e}")

connection_r.close()
