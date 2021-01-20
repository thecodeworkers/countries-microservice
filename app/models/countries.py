from mongoengine import Document, StringField, BooleanField, ListField, ReferenceField
from ..utils import RefQuerySet, to_json
from .states import States
from bson.json_util import dumps

class Countries(Document):
    name = StringField(min_length=2, max_length=100, required=True, unique=True)
    phone_prefix = StringField(min_length=2, max_length=10, required=True)
    active = BooleanField(required=True, default=1)
    states = ListField(ReferenceField(States, dbref=False))

    meta = {
        'queryset_class': RefQuerySet
    }

    def to_json(self):
        return to_json(self)
