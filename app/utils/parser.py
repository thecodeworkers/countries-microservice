from json import loads


def parser_all_object(model):
    parser = __commonParser(model)
    parser = map(__iterate_object, parser)
    return list(parser)


def parser_one_object(model):
    parser = __commonParser(model)
    parser = __iterate_object(parser)
    return dict(parser)


def __commonParser(model):
    model_parser = model.to_json()
    model_parser = loads(model_parser)
    return model_parser


def __iterate_object(object):
    
    object = __change_key(object)

    if '_id' in object:
        object['id'] = object['_id']
        del object['_id']

    return object

def __change_key(object):
    for key in object:
        if '$oid' in object[key]:
            object[key] = object[key]['$oid']
        
        if isinstance(object[key], list):
            object[key] = __iterate_list(object[key])
            
    return object

def __iterate_list(object_list):
    for i in range(len(object_list)):
        if '$oid' in object_list[i]:
            object_list[i]['id'] = object_list[i]['$oid']
            del object_list[i]['$oid']
    
    return object_list