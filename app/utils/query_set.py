from mongoengine import QuerySet, Document
from bson.dbref import DBRef
from bson.json_util import dumps


class RefQuerySet(QuerySet):

    def set_related(self, data):
        print(data)
        print(data._data)
        new_data = data._data
        new_data['id'] = str(new_data['id'])

        for key in new_data:
            if isinstance(new_data[key], Document) or isinstance(new_data[key], DBRef):
                new_data[key] = str(new_data[key].id)

        return new_data

    def get_related(self, datas):

        datas = list(map(self.set_related, datas))
        
        for data in datas:
            for key in data:
                if isinstance(data[key], list):
                    data[key] = list(map(self.set_related, data[key]))
                    for list_data in data[key]:
                        for key2 in list_data:
                            if isinstance(list_data[key2], list):
                                list_data[key2] = list(map(
                                    self.set_related, list_data[key2]))

        return datas

    def to_json(self):
        data = self.get_related(self.select_related())

        return dumps(data)
