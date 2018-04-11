import json
import requests
import allure
import pytest
import os

def xxx():
    path = os.listdir()
    namelist = []
    requestlist = []
    for f in path:
        if ".json" in f:
            with open(f, 'r', encoding='utf-8') as f:
                testdata = json.load(f)
                # print(testdata)
    nonlocal testdata
    for data in testdata:
        name = data["name"]
        namelist.append(name)
        request = data["request"]
        requestlist.append(request)
    # print(namelist)
    return namelist, requestlist

print(xxx()[1])

@allure.feature('testsuite1')
@allure.story("testcass111")
@allure.title("测试报告")
@pytest.mark.parametrize("request",xxx()[1])
def test_cass(request):
    # with allure.step("步骤一"):
    res = requests.request(request["method"],request["url"],headers=request["headers"],data=request["data"])
    allure.attach(res.text, "返回的参数")
    assert True
