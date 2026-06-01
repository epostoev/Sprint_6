import allure
import pytest
from data import URLS, TestData


@allure.suite("Тесты выпадающего списка в разделе 'Вопросы о важном'")
class TestMainPage:
    @allure.title("Проверка раскрытия аккордеона FAQ для вопроса № {num}")
    @allure.description(
        "Тест проверяет позитивный сценарий работы выпадающего списка 'Вопросы о важном'.\n\n"
        "Шаги:\n"
        "1. Переходим на главную страницу Самоката.\n"
        "2. Скроллим до блока вопросов и кликаем на стрелочку вопроса.\n"
        "3. Дожидаемся появления текста ответа.\n"
        "4. Проверяем, что текст ответа соответствует ожидаемому из тестовых данных.")
    @pytest.mark.parametrize('num', [0, 1, 2, 3, 4, 5, 6, 7])
    def test_question_and_answer(self, num, main_page):
        main_page.go_to_url(URLS.BASE_URL)
        assert main_page.check_answer(num, TestData.answers_data[num]), \
            f"Текст ответа для вопроса №{num} не совпадает с ожидаемым!"
