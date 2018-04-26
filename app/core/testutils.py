import requests

# def run_http_test(cassname, req):
#     '''
#     对HTTP接口发送请求
#     '''
#     try:
#         r = requests.request(**req)
#     except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as timeout:
#         print("【%s】在只从过程中出现异常，错误信息：%s" % (cassname, timeout))
#     return r
def run_http_test(cassname, req):
    '''
    对HTTP接口发送请求
    '''
    try:
        r = requests.request(**req)
    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as timeout:
<<<<<<< HEAD
        print("【%s】在只从过程中出现异常，错误信息：%s" % (cassname,timeout))
=======
        print("【%s】在只从过程中出现异常，错误信息：%s" % (cassname, timeout))
>>>>>>> 6b97d43e0bb17e40d4a505acd7417872ead759e3
    return r


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


