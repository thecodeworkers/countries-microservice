from mongoengine import Document, ReferenceField, StringField, ListField
from .cities import Cities

class States(Document):
	country = ReferenceField('Countries', dbref=False)
	name = StringField(max_length=100, required=True)
	cities = ListField(ReferenceField(Cities, dbref=False))