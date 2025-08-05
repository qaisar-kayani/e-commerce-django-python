from mongoengine import Document, StringField, DateTimeField
from datetime import datetime
class Category(Document):
    name = StringField(required=True)
    description = StringField()
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow) 