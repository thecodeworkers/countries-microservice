from mongoengine import Document, StringField, ReferenceField

class Cities(Document):
    state = ReferenceField('States', dbref=False)
    name = StringField(max_length=100, required=True)