# encoding: utf-8
from app.utils.log import Logger
from app.utils.exception import JSONDecodeError,ParamsException


def json_to_dict(json_str):
    '''
    将json转换为dict
    '''
    # print(json)
    import json
    json = json_str.loads(json_str)
    return json


def dict_to_json(dict):
    '''
    将dict转换为json
    '''
    import json
    json = json.dumps(json)
    return json


def validate_req_json(json_str):
    """
    :ex:校验并格式化PostMan的Json字符串
    :param json_str:
    :return:   成功:[{json1},{json1},{json1}]
                失败: False
    """
    import json
    reqs = []
    try:
        json_str = json_str.replace("\n", "").replace("\t", "")
        req_info = json.loads(json_str)["item"]
        for r in req_info:
            req = {}
            jsons = {}
            req["timeout"] = 10
            req["url"] = r["name"]
            req["method"] = r["request"]["method"]
            req["header"] = {r["request"]["header"][0]["key"]:r["request"]["header"][0]["value"]}
            for k,v in eval(r["request"]["body"]["raw"]).items():
                jsons[k] = v
            req["json"] = jsons
            reqs.append(req)
        return reqs

    except (JSONDecodeError, ParamsException) as e:
        # logger = Logger()
        # logger.error("JSON校验异常,异常信息为 -->%s" % e)
        print(e)
        return False



if __name__ == "__main__":
    json = ""
    file_path = "C:/Users/SNake/PycharmProjects/Nahsor/examples/Nahsor.postman_collection.json"
    for line in open(file_path):
        json += line

    reqs = validate_req_json(json)
    print(reqs)
