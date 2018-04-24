# -*- coding:utf-8 -*-

from core import run_test
import logging
from exception import MyException
logger = logging.getLogger(__name__)

def pytest_collect_file(parent, path):
    '''
    重写pytestpytest_collect_file，加载json格式的用例。
    '''
    # print(path)
    if path.ext == ".json" and path.basename.startswith("test"):
        return JsonFile(path, parent)
    return None

class JsonFile(pytest.File):
    '''
    自定义的`File`类将每个测试块加载为不同的测试
    '''
    def __init__(self, *args, **kwargs):
        super(JsonFile, self).__init__(*args, **kwargs)

        # 这个（下面的PlaceObj）是让pytest-pspec不会出错的。
        # 这个'do​​ctstring'是文件名，每个文件都是'docstring'
        # 个人测试是实际的测试名称
        class PlaceObj(object):
            __doc__ = self.fspath

        self.obj = PlaceObj

    def collect(self):
        '''
        解析json文件，并转换为字典测试用例
        '''
        import json
        try:
            all_tests = json.load(self.fspath.open())
        except:
            raise
        
        for test_spec in all_tests:
            if not test_spec:
                logger.warning("Empty document in input file '%s'", self.fspath)
                continue

            try:
                yield JsonItem(test_spec["test_name"], self, test_spec, self.fspath)
            except (TypeError, KeyError):
                # verify_tests(test_spec)  # 校验用例格式
                raise

class JsonItem(pytest.Item):
    '''
    对测试用例的测试进行重新封装
    '''
    def __init__(self, name, parent, spec, path):
        super(JsonItem, self).__init__(name, parent)
        self.path = path
        self.spec = spec

        class PlaceObj(object):
            __doc__ = name

        self.obj = PlaceObj

    def runtest(self):
        # for name, value in sorted(self.spec.items()):
        #     # some custom test execution (dumb example follows)
        #     if name != value:
        #         
        run_test(self.path, self.spec)


    def repr_failure(self, excinfo):
        '''
        重写pytest 中的repr_failure方法，用来展示测试执行错误的详细信息
        '''

        if not issubclass(excinfo.type, MyException):
            return super(JsonItem, self).repr_failure(excinfo)

        return super(JsonItem, self).repr_failure(excinfo)

    def reportinfo(self):
        return self.fspath, 0, "{self.path}::{self.name:s}".format(self=self)
