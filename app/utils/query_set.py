from mongoengine import QuerySet, Document
from bson.dbref import DBRef
from bson.json_util import dumps
import time

class RefQuerySet(QuerySet):

    def set_related(self, data):
        
        if not 'cities' in data:
            new_data = data._data
            for key in new_data:
                if isinstance(new_data[key], Document) or isinstance(new_data[key], DBRef):
                    new_data[key] = str(new_data[key].id)
        else:
            new_data = {key: str(data[key].id) if isinstance(data[key], Document) or isinstance(data[key], DBRef) else data[key] for key in data}
                
        new_data['id'] = str(new_data['id'])

        return new_data

    def get_related(self, data):
        
        data = self.set_related(data)
        
        for key in data:
            if isinstance(data[key], list):
                data[key] = [self.set_related(old_data) for old_data in data[key]]
                for list_data in data[key]:
                    for key2 in list_data:
                        if isinstance(list_data[key2], list):
                            list_data[key2] = [self.set_related(old_data) for old_data in list_data[key2]]
            
        return data

    def to_json(self):
        data = [self.get_related(value) for value in self.select_related(max_depth=2)]
        return dumps(data)
