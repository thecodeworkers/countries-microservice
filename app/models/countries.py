from mongoengine import Document, StringField, BooleanField, ListField, ReferenceField
from ..utils import RefQuerySet
from .states import States
from bson.json_util import dumps

class Countries(Document):
    name = StringField(max_length=100, required=True)
    phone_prefix = StringField(max_length=10)
    active = BooleanField(required=True, default=1)
    states = ListField(ReferenceField(States, dbref=False))
    meta = {'queryset_class': RefQuerySet}

    def to_json(self):
        data = RefQuerySet.set_related(RefQuerySet, self.select_related())
        for key in data:
            if isinstance(data[key], list):
                data[key] = map(lambda datas: RefQuerySet.set_related(RefQuerySet, datas), data[key])

        return dumps(data)