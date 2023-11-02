import sys
import pika 
from conn2 import connect_to_mongodb, get_rabbitmq_channel
from model2 import Contact

# Підключення до MongoDB
connect_to_mongodb()

def send_email(contact_id):
    contact = Contact.objects(id=contact_id).first()
    if contact:
        contact.send_email = True
        contact.save()
    else:
        print(f"Контакт з ID {contact_id} не знайдений.")

def main():
    # Підключення до RabbitMQ
    channel = get_rabbitmq_channel()

    # Створення черги
    channel.queue_declare(queue='email_queue')

    def callback(ch, method, properties, body):
        contact_id = body.decode('utf-8')
        send_email(contact_id)

        # Підтвердження обробленого повідомлення
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print(f"Повідомлення для контакту {contact_id} успішно оброблено")

    channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=False)

    print('Waiting for email messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
