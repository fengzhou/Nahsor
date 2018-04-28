from app.core.testutils import run_http_test
from app.core.testutils import extract_global_values
from app.core.testutils import run_validata_test, exex_global_values
from app.utils.log import Logger
from app.utils.jsonfuc import json_to_dict
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
                execlist = exex_global_values(request)
                if len(execlist) != 0:
                    for execkey in execlist:
                        print(execkey)
                        exec(execkey)
                r = run_http_test(testname, request)
                extlist = extract_global_values(extract)
                for value in extlist:
                    # print(value)
                    exec(value)
            else:
                r = run_http_test(testname, request)
            for validate in validates:
                key = list(validate.keys())[0]
                # print(key)
                chicker = run_validata_test(key)
                chicklist = []
                for i in validate[key]:
                    chicklist.append(eval(i))
                try:
                    chicker(chicklist)
                    Logger().info("测试用例[%s]检查点执行通过,检查点信息为 --> %s" % (testname, chicklist))
                except Exception as e:
                    raise
                    Logger().war("测试用例[%s]测试不通过,错误信息为 --> %s" % (testname, e))
        except Exception as e:
            Logger().war("测试用例[%s]测试不通过,错误信息为 --> %s" % (testname, e))


