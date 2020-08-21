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
        data = RefQuerySet.set_related(RefQuerySet, self.select_related())

        for key in data:
            if isinstance(data[key], list):
                data[key] = [RefQuerySet.set_related(RefQuerySet, old_data) for old_data in data[key]]

        return dumps(data)
