import json


def json_to_dict(json):
    '''
    将json转换为dict
    '''
    # print(json)
    json = json.loads(json)
    return json


def dict_to_json(dict):
    '''
    将dict转换为json
    '''
    json = json.dumps(json)
    return json