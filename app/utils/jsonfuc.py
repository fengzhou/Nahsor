# encoding: utf-8
from app.utils.log import Logger
from app.utils.exception import JSONDecodeError, ParamsException


def json_to_dict(json_str):
    '''
    将json转换为dict
    '''
    json = json_str.loads(json_str)
    return json


def dict_to_json(dict):
    '''
    将dict转换为json
    '''
    import json
    json = json.dumps(json)
    return json


def _basic_format_validate(case):
    """
    :校验标准测试用例格式
        标准格式如下:
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
    :return: False失败,True成功

     """
    if not isinstance(case, dict):
        try:
            import json
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
        if request["method"] is None or \
                not isinstance(request["method"], str):
            return False
        if request["method"] not in ("get", "post", "GET", "POST"):
            return False

        # timeout
        if request["timeout"] is None or \
                not isinstance(request["timeout"], int) or request["timeout"] == "":
            return False

        # json
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
                not isinstance(testname, str) or testname == "":
            return False
    except (JSONDecodeError, KeyError, SyntaxError) as e:
        return False

    # testtype
    try:
        testtype = case["testtype"]
        if testtype is None or \
                not isinstance(testtype, str) or testtype == "":
            return False
        if testtype not in ("testcass", "testsuite"):
            return False
    except (JSONDecodeError, KeyError, SyntaxError) as e:
        return False

    # validate
    # todo validate str to dict异常，需要解决这个问题！！
    try:
        validate = case["validate"]
        if validate is None or \
                not isinstance(validate, str) or validate == "":
            return False

    except (JSONDecodeError, KeyError, SyntaxError) as e:
        return False

    return True


def _postman_format_validate(case):
    """
    :校验postman raw部分的json格式
    :param case: har格式的json字符串
    :return: []:失败; Not []:成功

     """
    reqs = []
    try:
        import json
        postman_items = json.loads(case, encoding="utf-8")["item"]
        if postman_items is None:
            return []

        for item in postman_items:
            postman_items_req = item["request"]
            if postman_items_req is None:
                return []

            postman_items_req_body = postman_items_req["body"]
            if postman_items_req_body is None:
                return []

            data = postman_items_req_body["raw"]
            if _basic_format_validate(data):
                data = data.replace("\n", "").replace("\t", "").replace("\\", "").replace("    ", "")
                reqs.append(data)
    except:
        return []
    finally:
        return reqs


def _har_format_validate(case):
    """
    : 校验har请求体中request部分
    :param case: har格式的json字符串
    :return: []:失败; Not []:成功
    """
    reqs = []
    try:
        import json
        har_entries = json.loads(case, encoding="utf-8")["log"]["entries"]
        if har_entries is None:
            return []

        har_entries_req = har_entries[0]["request"]
        if har_entries_req is None:
            return []

        har_entries_req_postdate = har_entries_req["postData"]
        if har_entries_req_postdate is None:
            return []

        har_entries_req_postdate_params = har_entries_req_postdate["params"]
        if har_entries_req_postdate_params is None:
            return []

        # 获取对应的键值对
        from urllib.parse import unquote_plus
        for param in har_entries_req_postdate_params:
            req = {}
            key, value = param["name"], param["value"]
            if key in ("request", "testname", "testtype", "validate"):
                req[key] = unquote_plus(value)
                reqs.append(req)

    except:
        return []

    return reqs


def validate_req_json(json_str, type='postman'):
    """
    :ex:校验并格式化PostMan的Json字符串
    :param json_str: str; type:postman/har
    :return:   成功:[{json1},{json1},{json1}]
                失败: []
    """
    reqs = []

    try:
        if type == "har":
            reqs = _har_format_validate(json_str)

        if type == "postman":
            reqs = _postman_format_validate(json_str)

    except Exception as e:
        print(e)
    finally:
        return reqs


# todo bug1: post字符串输出，不是json或dict输出
# todo bug2: har基础校验设置，以及多个har兼容问题
# todo 睡觉休息，太累了...

if __name__ == "__main__":

    test_type = "postman"  # 修改我
    if test_type == "postman":
        file_path = "C:/Users/SNake/PycharmProjects/Nahsor/examples/Nahsor.postman_collection.json"
    if test_type == "har":
        file_path = "C:/Users/SNake/PycharmProjects/Nahsor/examples/test.har"

    json = ""
    for line in open(file_path, encoding="utf-8"):
        json += line

    print(validate_req_json(json, type=test_type))
