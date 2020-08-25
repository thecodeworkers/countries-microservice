from mongoengine import QuerySet, Document
from bson.dbref import DBRef
from bson.json_util import dumps

class RefQuerySet(QuerySet):

    def set_related(self, data):
        
        if not 'cities' in data:
            new_data = data._data
            new_data = {key: str(new_data[key].id) if isinstance(new_data[key], Document) or isinstance(new_data[key], DBRef) else new_data[key] for key in new_data}
        else:
            new_data = {key: str(data[key].id) if isinstance(data[key], Document) or isinstance(data[key], DBRef) else data[key] for key in data}
                
        new_data['id'] = str(new_data['id'])

        return new_data

    def get_related(self, data):
        
        data = self.set_related(data)
        
        data = {key: [self.set_related(old_data) for old_data in data[key]] if isinstance(data[key], list) else data[key] for key in data}
            
        return data

    def get_relations(self,data):

        data = self.get_related(data)

        related_data = {key: [self.get_related(old_data) for old_data in data[key]] if isinstance(data[key], list) else data[key] for key in data}

        return related_data

    def to_json(self):
        data = [self.get_relations(value) for value in self.select_related(max_depth=2)]
        return dumps(data)
