from app.core.testutils import run_http_test
from app.core.testutils import run_validata_test
from app.utils.log import Logger
from app.utils.jsonfuc import json_to_dict

class Runner(object):
    def __init__(self, testcass):
        self.testname = testcass["testname"]
        self.testtype = testcass["testtype"]
        self.request = testcass["request"]
        self.validates = testcass["validate"]

    def run_test(self):
        testname = self.testname
        testtype = self.testtype
        request = self.request
        validates = self.validates
        # request = json_to_dict(request)
        # 这个地方格式转换有问题！
        print(request)
        try:
            r = run_http_test(testname, request)
            for validate in validates:
                key = list(validate.keys())[0]
                chicker = run_validata_test(key)
                chicklist = []
                for i in validate[key]:
                    chicklist.append(eval(i))
                try:
                    chicker(chicklist)
                    Logger().info("测试用例[%s]检查点执行通过,检查点信息为 --> %s" % (cassname, chicklist))
                except Exception as e:
                    Logger().war("测试用例[%s]测试不通过,错误信息为 --> %s" % (cassname, e))
        except:
            pass


