import allure
import pytest
from data import URLS, TestData
from pages.base_page import BasePage
from pages.main_page import MainPage

@allure.title('Тесты на проверку вопросов')
@allure.description('TO DO')
class TestMainPage:
    @pytest.mark.parametrize('num', [1, 2, 3, 4, 5, 6, 7])
    def test_question_and_answer(self, num, main_page):
        main_page.go_to_url(URLS.BASE_URL)
        assert (
            main_page.check_answer(num, TestData.answers_data[num])
        )