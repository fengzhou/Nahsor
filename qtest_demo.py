import allure


def pytest_configure():
    allure.environment(report='测试报告名称', browser='chrome')


@allure.feature('testsuite1')
@allure.story('testcass1')
def test_minor():
    allure.environment(country='countrys')
    with allure.step("步骤一"):
        @allure.attach("说明这个步骤", "???")
        assert True
    with allure.step("步骤二", "???"):
        @allure.attach("说明")
        assert True
    with allure.step("步骤三", "???"):
        @allure.attach("说明")
        assert False


@allure.title("测试报告")
@allure.severity("critical")  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.feature('testsuite2')
@allure.story('testcass2', 'testcass3')
@allure.story('testcass4')
class TestBar:
    def test_bar(self):
        @allure.attach("说明")
        assert True

    def test_bar2(self):
        with allure.step("步骤一"):
            @allure.attach("说明")
            assert True
        with allure.step("步骤二"):
            @allure.attach("说明")
            assert True
        with allure.step("步骤三"):
            @allure.attach("说明")
            assert True


