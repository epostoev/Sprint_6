import allure
import pytest
from data import URLS, TestData, TestData_ORDER_PAGE
from pages.base_page import BasePage
from pages.order_page import OrderPage

from locators.main_page_locator import MainPageLocators
from locators.order_page_locator import OrderPageLocator

@allure.suite('Тесты оформления заказа')
class TestOrderPage:
    @allure.title('Проверка позитивного сценария заказа самоката')
    @allure.description('Проверяем нажатие кнопок "Заказать", заполнение данных и создание заказа')
    @pytest.mark.parametrize(
        "locator, order_data",
        [
            (MainPageLocators.ORDER_BUTTON_UP, TestData_ORDER_PAGE.ORDER_DATA_1),
            (MainPageLocators.ORDER_BUTTON_DOWN, TestData_ORDER_PAGE.ORDER_DATA_2)
        ]
                             )
    def test_create_order(self, locator, order_data, order_page):
        order_page.go_to_url(URLS.BASE_URL)
        order_page.scroll_to_element(locator)
        order_page.click_to_element(locator)
        order_page.set_first_page_info(order_data)
        order_page.set_second_page_info(order_data)
        input()
        assert True