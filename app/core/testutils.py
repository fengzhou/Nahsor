import requests
from app.utils.log import Logger


def run_http_test(testname, request):
    '''
    对HTTP接口发送请求
    '''
    try:
        Logger().info("开始执行测试用例[%s]" % testname)
        Logger().info("接口请求地址为 --> %s" % request["url"])
        Logger().info("接口请求方法为 --> %s" % request["method"])
        Logger().info("接口请求header --> %s" % request["headers"])
        Logger().info("接口请求数据为 --> %s" % request["json"])


        r = requests.request(**request)
    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as timeout:
        Logger().error("测试用例[%s]在执行过程中出现异常，错误信息为 --> %s" % (testname, timeout))
    try:
        assert r.status_code == 200
        return r
    except:
        Logger().error("测试用例[%s]在执行过程中出现异常，错误信息为 --> [code:%s],[error:%s]" % (testname, r.status_code, r.text))
        raise

def exex_global_values(request):
    '''
    {
        "url": "http://127.0.0.1:2333/test",
        "json": {'token': '$extracts["token"]'},
        "method": "POST",
        "headers": {
            "Content-Type": "application/json"
        },
        "timeout": 10
    }
    '''
    execlist = []
    for key in request:
        if type(request[key]) == dict:
            for key1 in request[key]:
                # print(key)
                if '$' == request[key][key1][:1]:
                    # print(key1)
                    execkey = "request['%s']['%s'] = %s" % (key, key1, request[key][key1][1:])
                    execlist.append(execkey)
                    # print(execkey)
    return execlist




def extract_global_values(extract):
    '''
    [
        {"token":"r.json()["data"]"},
        {"token":"r.json()["data"]"}
    ]
    '''
    extlist = []
    for extdict in extract:
        key = list(extdict.keys())[0]
        value = extdict[key]
        extfuc = "extracts['%s'] = %s" % (key, value)
        extlist.append(extfuc)
    return extlist


def run_validata_test(key):
    '''
    用例的校验方法
    arg : validate = {}
    '''
    asserts = {
        "Equal": equal,
        "NotEqual": notequal
        # "True": "is True",
        # "False": "is False",
        # "Is": "is",
        # "IsNot": "is not",
        # "IsNone": "is None",
        # "IsNotNone": "is not None",
        # "In": "in",
        # "NotIn": "not in",
        # "IsInstance": "isinstance",
        # "NotIsInstance": "not isinstance"
    }
    return asserts[key]

def equal(validate):
    assert validate[0] == validate[1]


def notequal(validate):
    assert validate[0] != validate[1]
