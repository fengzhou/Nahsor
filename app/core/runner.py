from app.core.testutils import run_http_test
from app.core.testutils import run_validata_test

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
                print("检查点执行通过！")
            except:
                print("【%s】测试不通过" % self.cassname)


def run_test(testcass):
    """
    去掉self后的runner
    :param testcass:
    :return:
    """
    testcass = testcass
    cassname = testcass["cass_name"]
    req = testcass["req"]
    validates = testcass["validates"]

    r = run_http_test(cassname, req)
    for validate in validates:
        key = list(validate.keys())[0]
        # print(key)
        chicker = run_validata_test(key)
        chicklist = []
        for i in validate[key]:
            chicklist.append(eval(i))
        # validate = validate[key]
        try:
            chicker(chicklist)
            print("检查点执行通过！")
        except:
            print("【%s】测试不通过" % cassname)
