# from django.db import models,
from mongoengine import Document, StringField, IntField, ListField, BooleanField, DateTimeField, FloatField
from datetime import datetime

# Create your models here.
class Product (Document):
    name = StringField(required = True)
    description = StringField(required = True)
    category = StringField()
    brand = StringField()
    price = FloatField(default = 0)
    stock =  IntField(default = 0)
    images = ListField(StringField())
    is_active = BooleanField(default = True)
    created_at = DateTimeField(default = datetime.utcnow)
    updated_at = DateTimeField(default = datetime.utcnow)



