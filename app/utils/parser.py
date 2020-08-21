from json import loads


def parser_all_object(model):
    parser = __commonParser(model)
    parser = [__iterate_object(parse) for parse in parser]
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
    
    if '_id' in object:
        object['id'] = object['_id']
        del object['_id']

    return object

