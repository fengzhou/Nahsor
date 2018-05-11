# -*- coding:utf-8 -*-
import requests
from app.utils.log import Logger
from app.utils.dbfucs import excute

Logger = Logger()

def run_http_test(testname, request):
    '''
    对HTTP接口发送请求
    '''
    Logger.info("开始执行测试用例[%s]" % testname)
    Logger.info("接口请求地址为 --> %s" % request["url"])
    Logger.info("接口请求方法为 --> %s" % request["method"])
    Logger.info("接口请求header --> %s" % request["headers"])
    Logger.info("接口请求数据为 --> %s" % request["json"])
    try:
        r = requests.request(**request)
    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as timeout:
        Logger.error("测试用例[%s]在执行过程中出现异常，错误信息为 --> %s" % (testname, timeout))
    Logger.info("接口响应时间为 --> %ss" % r.elapsed.total_seconds())
    Logger.info("接口响应状态为 --> %s" % r.status_code)
    Logger.info("接口响应内容为 --> %s" % r.text)
    if r.status_code == 200:
        return r
    else:
        # Logger.error("测试用例[%s]在执行过程中出现异常，错误信息为 --> [code:%s],[error:%s]" % (testname, r.status_code, r.text))
        raise Exception()

def get_global_values(request):
    '''
    替换request里带了$的参数为全局变量中的值。
    {
        "url": "http://127.0.0.1:2333/test",
        "json": {'token': '$token'},
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
                    execkey = "request['%s']['%s'] = extracts['%s']" % (key, key1, request[key][key1][1:])
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
    execlist = []
    for extdict in extract:
        key = list(extdict.keys())[0]
        value = extdict[key]
        extfuc = "extracts['%s'] = %s" % (key, value)
        execlist.append(extfuc)
    return execlist


def run_execs_test(execlist):
    '''
    执行赋值类型的表达式
    extracts['token'] = 'ssdsfsdf4s6f54s6f1a3s'
    '''
    # print(**arg)
    if len(execlist) != 0:
        for execkey in execlist:
            print(execkey)
            exec(execkey)


def run_evals_test(evalist):
    '''
    执行判断类型的表达式
    "12233" == 'sdsdd'
    '''
    if len(evalist) != 0:
        for evalkey in evalist:
            print(evalkey)
            eval(evalkey)


def run_validata_test(testname, validatelist):
    '''
    测试用例的检查点执行
    '''
    if len(validatelist) != 0:
        for validatekey in validatelist:
            res = eval(validatekey)
            if res == True:
                Logger.info("测试用例[%s]检查点执行成功,检查点信息为 --> %s" % (testname, validatekey))
            else:
                Logger.war("测试用例[%s]检查点执行失败,检查点信息为 --> %s" % (testname, validatekey))


def get_validata_test(validates):
    '''
    提取的校验方法
    arg : [{"Equal": ["r.status_code", "200"]}]
    '''
    asserts = {
        "Equal": "==",
        "NotEqual": "!=",
        "True": "is True",
        "False": "is False",
        "Is": "is",
        "IsNot": "is not",
        "IsNone": "is None",
        "IsNotNone": "is not None",
        "In": "in",
        "NotIn": "not in",
        "IsInstance": "isinstance",
        "NotIsInstance": "not isinstance"
    }
    validatelist = []
    for validate in validates:
        key = list(validate.keys())[0]
        # print(key)
        asserts[key]
        validate[key]
        validatekey = validate[key][0] + asserts[key] + validate[key][1]
        validatelist.append(validatekey)

    return validatelist


def insert_test_result(cassid,status,runtime="",result="",validate=""):
    '''
    将测试结果存入到数据库
    '''
    sql = "INSERT INTO `t_reports` (`cassid`, `status`, `runtime`, `result`, `validate`) VALUES ('%s', '%s', '%s', '%s', '%s')" % (cassid,status,runtime,result,validate)
    dbres = excute(sql)
    if dbres != True:
        Logger.error("保存测试结果到数据库出错，错误信息 --> %s" % dbres)