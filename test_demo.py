import allure


@allure.feature('Feature1')
@allure.story('Story1')
def test_minor():
    assert False


@allure.feature('Feature2')
@allure.story('Story2', 'Story3')
@allure.story('Story4')
class TestBar:

    # will have 'Feature2 and Story2 and Story3 and Story4'
    def test_bar(self):
        @allure.attach("说明")
        assert True
