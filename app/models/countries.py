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
        data = RefQuerySet.set_related(RefQuerySet, self)
        for key in data:
            if isinstance(data[key], list):
                data[key] = list(map(lambda datas: RefQuerySet.set_related(RefQuerySet, datas), data[key]))
                for list_data in data[key]:
                        for key2 in list_data:
                            if isinstance(list_data[key2], list):
                                list_data[key2] = list(map(lambda datas: RefQuerySet.set_related(RefQuerySet, datas), list_data[key2]))

        return dumps(data)