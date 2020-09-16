from mongoengine import Document, StringField, ListField, ReferenceField
from ..utils import RefQuerySet, to_json
from .cities import Cities


class States(Document):
    country = ReferenceField('Countries', dbref=False)
    name = StringField(max_length=100, required=True)
    cities = ListField(ReferenceField(Cities, dbref=False))

    meta = {'queryset_class': RefQuerySet}

    def to_json(self):

        return to_json(self)
