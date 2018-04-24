import json
from app.core.runner import Runner

def jsonfile(filename):
    '''
    判断导入的json文件格式是否合法
    '''
    filetype = filename.split(".")
    # print(filetype[-1])
    if filetype[-1] == "json" and filename.startswith("test"):
        return filename
    else:
        print("导入的json文件格式不正确")
        return None



def collect_file_cass(filename):
    '''
    读取json并执行用例。
    '''
    with open(filename, 'r') as f:
        all_tests = json.load(f)
        # print(all_tests)
    for test in all_tests:
        if not test:
            print("没有测试用例")
        # try:
        runner = Runner(test)
        yield runner.run_test()
        # except:
        #     print("【%s】用例执行失败" % test["cass_name"])


def collect_db_cass(jsoncasss):
    '''
    读取json并执行用例。
    '''
    # all_tests = json.loads(jsoncasss)
    for test in jsoncasss:
        if not test:
            print("没有测试用例")
        test = json.loads(test)
        try:
            runner = Runner(test)
            yield runner.run_test()
        except:
            print("【%s】用例执行失败" % test["cass_name"])


def verify_test(test):
    if test.has_key('cass_name'):
        pass



# filename = "test_json.json"
# jsonfile(filename)
# collect_file_cass(filename)
# for i in collect_file_cass(filename):
#     print("用例执行结束！")