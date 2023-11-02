from mongoengine import Document, StringField, BooleanField
# from mongoengine import connect

class Contact(Document):
    full_name = StringField(required=True)
    email = StringField(required=True)
    phone_number = StringField(required=True)
    choice_for_message = StringField(default='email')
    send_email = BooleanField(default=False)
    send_sms = BooleanField(default=False)