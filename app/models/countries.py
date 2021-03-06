from mongoengine import Document, StringField, BooleanField, ListField, ReferenceField
from ..utils import RefQuerySet, to_json
from .states import States
from bson.json_util import dumps

class Countries(Document):
    name = StringField(max_length=100, required=True)
    phone_prefix = StringField(max_length=10)
    active = BooleanField(required=True, default=1)
    states = ListField(ReferenceField(States, dbref=False))

    meta = {'queryset_class': RefQuerySet}

    def to_json(self):

        return to_json(self)