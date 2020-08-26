from mongoengine import Document
from .parser import parser_one_object
from bson.json_util import dumps


def to_json(data):

    data = data.select_related()

    data = {key: [parser_one_object(old_data) for old_data in data[key]] if isinstance(
        data[key], list) else data[key].id if isinstance(data[key], Document) else data[key] for key in data}

    #mod_data = {key: data[key].id for key in data if isinstance(data[key], Document)}

    # data.update(mod_data)

    return dumps(data)
