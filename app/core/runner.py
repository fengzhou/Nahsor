from app.core.testutils import run_http_test, get_validata_test
from app.core.testutils import extract_global_values, run_execs_test, run_evals_test
from app.core.testutils import run_validata_test, exec_global_values
from app.utils.log import Logger
from app.utils.jsonfuc import json_to_dict

Logger = Logger()
extracts = {}


class Runner(object):
    def __init__(self, testcass):
        self.testname = testcass["testname"]
        self.testtype = testcass["testtype"]
        self.request = testcass["request"]
        self.validates = testcass["validate"]
        self.extract = testcass["extract"]

    def run_test(self):
        testname = self.testname
        testtype = self.testtype
        request = eval(self.request)
        validates = eval(self.validates)
        extract = eval(self.extract)
        global extracts
        try:
            if testtype == "testsuite":
                execlist = exec_global_values(request)
                # print(execlist)
                # run_execs_test(execlist)
                if len(execlist) != 0:
                    for execkey in execlist:
                        print("execkey:",execkey)
                        exec(execkey)
                r = run_http_test(testname, request)
                execlist = extract_global_values(extract)
                # print(evalist)
                # run_execs_test(execlist)
                if len(execlist) != 0:
                    for execkey in execlist:
                        print("execkey:",execkey)
                        exec(execkey)
            else:
                r = run_http_test(testname, request)
            
            validatelist = get_validata_test(validates)
            # run_validata_test(testname, validatelist)
            if len(validatelist) != 0:
                for validatekey in validatelist:
                    res = eval(validatekey)
                    if res == True:
                        Logger.info("测试用例[%s]检查点执行成功,检查点信息为 --> %s" % (testname, validatekey))
                    else:
                        Logger.war("测试用例[%s]检查点执行失败,检查点信息为 --> %s" % (testname, validatekey))

        except Exception as e:
            Logger.war("测试用例[%s]测试不通过,错误信息为 --> %s" % (testname, e))


