# encoding: utf-8
from app.utils.log import Logger
from app.utils.exception import JSONDecodeError, ParamsException


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


def _postman_format_validate(case):
    """
    :校验postmanV2.0请求体中raw部分格式
        raw格式:
        {
                "request": "{"url": "http://127.0.0.1:2333/test", "json": {"aaa": "bbb"}, "method": "POST", "headers": {"Content-Type": "application/json"}, "timeout": 10}",
                "testname": "用例99",
                "testtype": "testcass",
                "validate": "[{"Equal": ["r.json()","request["json"]"]},{"Equal": ["r.status_code","200"]}]"
        }
    :param case:
            校验格式
             request:
             1.request不能为空;url不能为空
             2.method不能为空:get/post；
             3.header不能为空，只能为json；
             4.json不能为空；
             5.timeout不能只能为数字，大于0

             testname:
             1.不能为空

             testtype:
             1.不能为空
             2.testcass和testsuite

             validate：
             1.不能为空
             2.[{xxx:[]}]格式
    :return: False失败,True成功

     """
    import json
    if not isinstance(case, dict):
        try:
            case = json.loads(case, encoding="utf-8")
        except JSONDecodeError as e:
            return False

    # request
    try:
        request = json.loads(case["request"], encoding="utf-8")
        # request
        if request is None or \
                not isinstance(request, dict) or request == {}:
            return False

        # url
        if request["url"] is None or \
                not isinstance(request["url"], str) or request["url"] == "":
            return False

        # method
        if request["method"] is None or\
                not isinstance(request["method"], str):
            return False
        if request["method"] not in ("get", "post", "GET", "POST"):
            return False

        # timeout
        if request["timeout"] is None or\
            not isinstance(request["timeout"], int) or request["timeout"] == "":
            return False

        #json
        if request["json"] is None or \
                not isinstance(request["json"], dict) or request["json"] == {}:
            return False

        # headers
        if request["headers"] is None or \
                not isinstance(request["headers"], dict) or request["headers"] == {}:
            return False
        if "Content-Type" not in request["headers"].keys() \
            and "application/json" not in request["headers"].values():
            return False
    except (JSONDecodeError, KeyError, SyntaxError) as e:
        return False

    # testname
    try:
        testname = case["testname"]
        if testname is None or \
                not isinstance(testname,str) or testname == "" :
            return False
    except (JSONDecodeError, KeyError, SyntaxError) as e:
        return False

    # testtype
    try:
        testtype = case["testtype"]
        if testtype is None or \
                not isinstance(testtype, str) or testtype == "" :
            return False
        if testtype not in ("testcass", "testsuite"):
            return False
    except (JSONDecodeError, KeyError, SyntaxError) as e:
        return False

    # validate
    # todo validate str to dict异常，需要解决这个问题！！

    print(type(case["validate"]))
    a = case["validate"]
    print(a)
    print(json.loads(a, encoding="utf-8"))
    try:
        validate = json.loads(case["validate"], encoding="utf-8")
        if validate is None or \
               not isinstance(validate, list) or validate == []:
            return False
        for val in validate:
            if val is None or\
                    not isinstance(val, dict) or val == {}:
                return False
    except (JSONDecodeError, KeyError, SyntaxError) as e:
        return False



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
            for h in r["request"]["body"]:
                if h == "raw":
                    data = r["request"]["body"][h]
                    # 判断通过
                    if _postman_format_validate(data):
                        reqs.append(data)
            #
            # # 判断格式内容
            # if r["request"]["method"] != "POST" or r["request"]["body"]["raw"] is None:
            #     print("解析JSON失败,JSON格式为  --> %s" % r)
            #     continue

            # # 判断
            #
            # req = {}
            # jsons = {}
            # req["timeout"] = 10
            # req["testname"] = r["name"]
            # req["url"] = r["request"]["url"]
            # req["method"] = r["request"]["method"]
            # # 循环header
            # for headers in r["request"]["header"]:
            #     jsons[headers['key']] = headers['value']
            # req["header"] = jsons
            #
            # jsons = {}
            # # 循环body，得到json数据
            # for h in r["request"]["body"]:
            #     if h == "raw":
            #         data = r["request"]["body"][h].replace("\\","")
            #         print(data)
            # req["json"] = jsons
            # reqs.append(req)
        return reqs

    except (JSONDecodeError, ParamsException) as e:
        # logger = Logger()
        # logger.error("JSON校验异常,异常信息为 -->%s" % e)
        print("123")
        raise e
        return False



if __name__ == "__main__":

    json = ""
    file_path = "C:/Users/SNake/PycharmProjects/Nahsor/examples/Nahsor.postman_collection.json"
    for line in open(file_path, encoding="utf-8"):
        json += line

    reqs = validate_req_json(json)
    print(reqs)
