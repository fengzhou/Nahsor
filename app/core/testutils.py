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
