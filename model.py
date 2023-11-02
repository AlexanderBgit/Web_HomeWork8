# import json
from mongoengine import connect, \
    Document, StringField, ListField, ReferenceField


# Модель для автора
class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField(required=True)
    born_location = StringField(required=True)
    description = StringField(required=True)


# Модель для цитати
class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author, required=True)
    quote = StringField(required=True)



