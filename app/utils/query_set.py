from mongoengine import QuerySet, Document
from bson.dbref import DBRef
from bson.json_util import dumps

class RefQuerySet(QuerySet):

    def to_json(self):
        data = "[%s]" % (",".join([value.to_json() for value in self])) 
        
        return data
