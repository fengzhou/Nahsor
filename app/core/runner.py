from app.core.testutils import run_http_test
from app.core.testutils import run_validata_test
from app.utils.log import Logger

class Runner(object):
    def __init__(self, testcass):
        self.testcass = testcass
        self.cassname = testcass["cass_name"]
        self.req = testcass["req"]
        self.validates = testcass["validates"]
        # print(self.validates)
    def run_test(self):
        r = run_http_test(self.cassname, self.req)
        # print(r.status_code)
        for validate in self.validates:
            key = list(validate.keys())[0]
            # print(key)
            chicker = run_validata_test(key)
            chicklist = []
            for i in validate[key]:
                chicklist.append(eval(i))
            # validate = validate[key]
            try:
                chicker(chicklist)
                Logger().info("测试用例[%s]检查点执行通过,检查点信息为 --> %s" % (self.cassname, chicklist))
            except Exception as e:
                Logger().war("测试用例[%s]测试不通过,错误信息为 --> %s" % (self.cassname, e))
