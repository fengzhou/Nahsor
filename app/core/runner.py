from app.core.testutils import run_http_test
from app.core.testutils import run_validata_test
from app.utils.log import Logger

class Runner(object):

    @staticmethod
    def run_test(testcass):
        testcass = testcass
        cassname = testcass["cass_name"]
        req = testcass["req"]
        validates = testcass["validates"]

        r = run_http_test(cassname, req)
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


