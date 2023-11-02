from model import Quote, Author
# from mongoengine import connect
from conn import connect_to_mongodb
connection = connect_to_mongodb()

def search_quotes_by_author(author_name):
    author = Author.objects(fullname=author_name).first()
    if author:
        quotes = Quote.objects(author=author)
        for quote in quotes:
            print(quote.quote.encode('utf-8').decode('utf-8'))
    else:
        print('Цитати для даного автора не знайдено')

def search_quotes_by_tag(tag):
    quotes = Quote.objects(tags=tag)
    for quote in quotes:
        print(quote.quote.encode('utf-8').decode('utf-8'))

def search_quotes_by_tags(tag_list):
    quotes = Quote.objects(tags__in=tag_list)
    for quote in quotes:
        print(quote.quote.encode('utf-8').decode('utf-8'))

if __name__ == '__main__':
    while True:
        command = input("Введіть команду: ")

        if command == 'exit':
            break

        command_parts = command.split(':')

        if len(command_parts) != 2:
            print('Невірний формат команди.')
            continue

        command_type, value = command_parts

        if command_type == 'name':
            search_quotes_by_author(value)
        elif command_type == 'tag':
            search_quotes_by_tag(value)
        elif command_type == 'tags':
            tag_list = value.split(',')
            search_quotes_by_tags(tag_list)
        else:
            print('Невідома команда. Повторіть введення.')

    print('Завершення роботи.')
