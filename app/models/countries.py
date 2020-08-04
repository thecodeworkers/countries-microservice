from mongoengine import Document, StringField, BooleanField, EmbeddedDocumentListField


class Cities(EmbeddedDocument):
    name = StringField(max_length=100, required=True)

class States(EmbeddedDocument):
  name = StringField(max_length=100, required=True)
  cities = EmbeddedDocumentListField(Cities)

class Countries(Document):
    name = StringField(max_length=100, required=True)
    phone_prefix = StringField(max_length=10)
    active = BooleanField(required=True, default=0)
    states = EmbeddedDocumentListField(States)