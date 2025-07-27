from mongoengine import Document, EmailField, StringField, DateTimeField, BooleanField
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime


class Users(Document):
    username = StringField(required=True, unique=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    full_name = StringField()
    address = StringField()
    phone = StringField()
    is_admin = BooleanField(default=False)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
