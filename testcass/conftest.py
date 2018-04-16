# -*- coding:utf-8 -*-
import pytest

# def pytest_collect_file():
#     print("测试！！！！")

@pytest.fixture()
def test():
    print("test!!")