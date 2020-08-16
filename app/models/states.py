from mongoengine import Document, StringField, ListField, ReferenceField, QuerySet
from .cities import Cities
from bson.json_util import dumps

class RefQuerySet(QuerySet):


    def __set_cities(self, datas):
        new_related_datas = list()
        
        for related_data in datas:
            new_related_data = related_data._data
            new_related_data['id'] = str(new_related_data['id'])
            del new_related_data['state']
            new_related_datas.append(new_related_data)
        
        return new_related_datas

    def __set_states(self, datas):
        new_datas = list()
        
        for data in datas:
            new_data = data._data
            new_data['id'] = str(new_data['id'])
            new_data['country'] = str(data.country.id)
            new_data['cities'] = self.__set_cities(data.cities)
            new_datas.append(new_data)
        
        return new_datas


    def __get_related(self, datas):
        
        states = self.__set_states(datas)

        return states

    def to_json(self):
        data = self.__get_related(self.select_related())
        return dumps(data)


class States(Document):
    country = ReferenceField('Countries', dbref=False)
    name = StringField(max_length=100, required=True)
    cities = ListField(ReferenceField(Cities, dbref=False))

    meta = {'queryset_class': RefQuerySet}

    