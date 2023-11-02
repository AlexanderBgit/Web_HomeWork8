from mongoengine import connect
import pika
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def connect_to_mongodb():
    try:
        connect(
            host='mongodb+srv://UserMongo:1111@cluster0alex.zbparhx.mongodb.net/test',
            alias='default'
        )

        logger.info("Успішно підключено до MongoDB")
    except Exception as e:
        logger.error(f"Помилка підключення до MongoDB: {e}")
        raise 


def get_rabbitmq_channel():
    try:
        credentials = pika.PlainCredentials('guest', 'guest')
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host='localhost', 
                port=5672, 
                credentials=credentials
            )
        )
        channel = connection.channel()

        logger.info("Успішно підключено до RabbitMQ")
        return channel
    except Exception as e:
        logger.error(f"Помилка підключення до RabbitMQ: {e}")
        raise  
