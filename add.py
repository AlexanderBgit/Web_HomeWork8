import json
from model import Author, Quote
from mongoengine import connect
import os

# Підключення до бази даних MongoDB
# connect('db_name', host='host', port=port, db='test')
connect(
    host=f'mongodb+srv://UserMongo:1111@cluster0alex.zbparhx.mongodb.net/test'
    )


# Завантаження даних з файлу "authors.json"
with open('authors.json', 'r', encoding='utf-8') as file:
    authors_data = json.load(file)


# Збереження даних у колекції "authors"
for author_info in authors_data:
    author = Author(
        fullname=author_info['fullname'],
        born_date=author_info['born_date'],
        born_location=author_info['born_location'],
        description=author_info['description']
    )
    author.save()




# Завантаження даних з файлу "quotes.json"
# with open('quotes.json', 'r', encoding='utf-8') as file:
#     quotes_data = json.load(file)



current_directory = os.getcwd()
file_path = os.path.join(current_directory, 'quotes.json')

with open(file_path, 'r', encoding='utf-8') as file:
    quotes_data = json.load(file)

    # Збереження даних у колекції "quotes"
    for quote_info in quotes_data:
        author = Author.objects(fullname=quote_info['author']).first()
        if not author:
            author = Author(fullname=quote_info['author'])
            author.save()

        quote = Quote(
            tags=quote_info['tags'],
            author=author,  # Зберігаємо посилання на об'єкт автора
            quote=quote_info['quote']
        )
        quote.save()