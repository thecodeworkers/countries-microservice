from mongoengine import Document, StringField, BooleanField, ListField, ReferenceField
from .states import States

class Countries(Document):
	name = StringField(max_length=100, required=True)
	phone_prefix = StringField(max_length=10)
	active = BooleanField(required=True, default=1)
	states = ListField(ReferenceField(States, dbref=False))