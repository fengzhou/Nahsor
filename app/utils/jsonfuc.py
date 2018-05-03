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
            req["testname"] = r["name"]
            req["url"] = r["request"]["url"]
            req["method"] = r["request"]["method"]
            # 循环header
            for headers in r["request"]["header"]:
                jsons[headers['key']] = headers['value']
            req["header"] = jsons

            jsons = {}
            # 循环body，得到json数据
            for h in r["request"]["body"]:
                if h == "raw":
                    data = r["request"]["body"][h].replace("\\\\","")
                    print(data)
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
    for line in open(file_path, encoding="utf-8"):
        json += line

    reqs = validate_req_json(json)
    #print(reqs)
