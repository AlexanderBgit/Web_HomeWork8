from mongoengine import connect
import logging

# Налаштування логування
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def connect_to_mongodb():
    try:
        connect(
            host='mongodb+srv://UserMongo:1111@cluster0alex.zbparhx.mongodb.net/test',
            alias='default'
        )
        logger.info("Успішно підключено")
    except Exception as e:
        logger.error(f"Помилка підключення: {e}")

if __name__ == "__main__":
    connect_to_mongodb()
