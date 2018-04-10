import json
import requests
import allure
import pytest
import os


path = os.getcwd()

with open(path + '/testcass/testdata.json', 'r', encoding='utf-8') as f:
    testdata = json.load(f)
    print(testdata)
for testcass in testdata:
    print(testcass["name"])
    print(testcass["request"])

print(json.dumps(testcass['request']['data']))
@allure.feature("获取token数据")
@allure.story(testcass["name"])
class TestBar:
    # will have 'Feature2 and Story2 and Story3 and Story4'
    @allure.title(testcass["name"])
    # @pytest.mark.parametrize()
    def test_bar2():
        with allure.step("步骤1"):
            response = requests.request(testcass['request']['method'], testcass['request']['url'], data=testcass['request']['data'], headers=testcass['request']['headers'])
            # print(response.text)
            allure.attach(response.text, '接口返回值')
            assert testcass["assert"][0] == testcass["assert"][1]
        with allure.step("步骤三"):
            allure.attach('失败的步骤', '具体内容')
            assert False