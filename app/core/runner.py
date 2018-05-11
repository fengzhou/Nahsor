# -*- coding:utf-8 -*-
from app.core.testutils import run_http_test, insert_test_result
from app.core.testutils import extract_global_values
from app.core.testutils import get_global_values, get_validata_test
from app.utils.log import Logger

Logger = Logger()
extracts = {}


class Runner(object):
    def __init__(self, testcass):
        self.cassid = testcass["id"]
        self.testname = testcass["testname"]
        self.testtype = testcass["testtype"]
        self.request = testcass["request"]
        self.validates = testcass["validate"]
        self.extract = testcass["extract"]

    def run_test(self):
        cassid = self.cassid
        testname = self.testname
        testtype = self.testtype
        request = eval(self.request)
        validates = eval(self.validates)
        extract = eval(self.extract)
        global extracts
        try:
            if testtype == "testsuite":
                execlist = get_global_values(request)
                if len(execlist) != 0:
                    for execkey in execlist:
                        # print("execkey:",execkey)
                        exec(execkey)
                r = run_http_test(testname, request)
                execlist = extract_global_values(extract)
                if len(execlist) != 0:
                    for execkey in execlist:
                        # print("execkey:",execkey)
                        exec(execkey)
            else:
                r = run_http_test(testname, request)
            runtime = r.elapsed.total_seconds()
            result = r.text
            validatelist = get_validata_test(validates)
            # run_validata_test(testname, validatelist)
            if len(validatelist) != 0:
                for validatekey in validatelist:
                    # assert  eval(validatekey) ,"%s" % str(eval(validatekey))
                    # Logger.info("测试用例[%s]检查点执行成功,检查点信息为 --> %s" % (testname, validatekey))
                    res = eval(validatekey)
                    if res == True:
                        status = 0
                        Logger.info("测试用例[%s]检查点执行成功,检查点信息为 --> %s" % (testname, validatekey))
                    else:
                        status = 1
                        Logger.war("测试用例[%s]检查点执行失败,检查点信息为 --> %s" % (testname, validatekey))
            insert_test_result(cassid,status,runtime=runtime,result=result,validate=validatekey)
        except Exception as e:
            status = 2
            Logger.error("测试用例[%s]在执行过程中出现异常，错误信息为 --> %s" % (testname, e))
            insert_test_result(cassid,status)
