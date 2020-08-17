from mongoengine import Document, StringField, ListField, ReferenceField
from ..utils import RefQuerySet
from .cities import Cities
from bson.json_util import dumps


class States(Document):
    country = ReferenceField('Countries', dbref=False)
    name = StringField(max_length=100, required=True)
    cities = ListField(ReferenceField(Cities, dbref=False))

    meta = {'queryset_class': RefQuerySet}

    def to_json(self):
        data = RefQuerySet.set_related(self, self.select_related())

        for key in data:
            if isinstance(data[key], list):
                data[key] = map(lambda datas: RefQuerySet.set_related(
                    RefQuerySet, datas), data[key])

        return dumps(data)
