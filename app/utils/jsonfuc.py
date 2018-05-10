# -*- coding:utf-8 -*-
from app.utils.log import Logger
from app.utils.exception import JSONDecodeError, ParamsException
import json
import pymysql


def dict_to_dbjson(dict):
    '''
    将dict转换为json，并转义为数据库所需要的格式
    '''
    json = json.dumps(dict)
    value = pymysql.escape_string(json)
    return value


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
    :校验postman json文件格式并格式化字符串
    :param case: raw部分的json格式
    :return: []:失败; Not []:成功

     """
    reqs = []
    try:
        postman_items = json.loads(case, encoding="utf-8")["item"]
        if postman_items is None:
            return []

        for item in postman_items:
            try:
                postman_items_req = item["request"]
                postman_items_req_body = postman_items_req["body"]
                raw_data = postman_items_req_body["raw"]

                if raw_data is None:
                    return []

                if _basic_format_validate(raw_data):
                    reqs.append(json.loads(raw_data, encoding="utf-8"))
            except Exception as e:
                print(e)
                pass
    except Exception as e:
        print(e)
        pass
    finally:
        return reqs


def _har_format_validate(case):
    """
    : 校验并格式化har文件格式的字符串
    :param case: har格式的json字符串
    :return: []:失败; Not []:成功
    """
    FILTER_METHODS_RULES = [
        "get"
    ]

    from urllib.parse import unquote_plus

    reqs = []
    try:
        har_entries_list = json.loads(case, encoding="utf-8")["log"]["entries"]
        if har_entries_list is None:
            return []

        # 遍历每一个entries
        for har_entries in har_entries_list:
            try:
                har_entries_req = har_entries["request"]
                har_entries_req_method = har_entries_req["method"]
                har_entries_req_postdate = har_entries_req["postData"]
                har_entries_req_postdate_params = har_entries_req_postdate["params"]

                # 各个条件为空的情况,前面的条件如果为空会报错
                if har_entries_req_postdate_params is None:
                    return []

                # 过滤指定方法过滤GET方法，GET方法返回大数据量的html/js/css/image，减少计算量
                if har_entries_req_method.lower() in FILTER_METHODS_RULES:
                    continue

                # 获取对应的键值对,遍历request/testname/testtype/validate
                req = {}
                for param in har_entries_req_postdate_params:
                    key, value = param["name"], param["value"]
                    if key in ("request", "testname", "testtype", "validate"):
                        req[key] = unquote_plus(value)

                # 格式校验
                if _basic_format_validate(req):
                    reqs.append(req)
            except Exception as e:
                print(e)
                pass
    except Exception as e:
        print(e)
        pass
    finally:
        return reqs


def validate_req_json(json_str, type='postman'):
    """
    :ex:校验并格式化PostMan和har格式的Json字符串
    :param json_str: str; type:postman/har
    :return:   成功:[{json1},{json1},{json1}]
                失败: []
    """
    reqs = []
    try:
        if type.lower() == "har":
            reqs = _har_format_validate(json_str)

        if type.lower() == "postman":
            reqs = _postman_format_validate(json_str)

    except Exception as e:
        print(e)
    finally:
        return reqs


if __name__ == "__main__":

    test_type = "postman"  # 修改我
    if test_type == "postman":
        file_path = "C:/Users/SNake/PycharmProjects/Nahsor/examples/postman_test.json"
    if test_type == "har":
        file_path = "C:/Users/SNake/PycharmProjects/Nahsor/examples/har_test.har"

    json = ""
    for line in open(file_path, encoding="utf-8"):
        json += line

    print(validate_req_json(json, type=test_type))

