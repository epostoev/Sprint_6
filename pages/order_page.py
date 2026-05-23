import allure
from pages.base_page import BasePage
from locators.main_page_locator import MainPageLocators
from locators.order_page_locator import OrderPageLocator
from data import TestData_ORDER_PAGE

class OrderPage(BasePage):
    pass
    @allure.step("Заполняем первую страницу заказа")
    def set_first_page_info(self, data):
        self.scroll_to_element(OrderPageLocator.FIELD_NAME)
        self.click_to_element(OrderPageLocator.FIELD_NAME)
        self.add_text_to_element(OrderPageLocator.FIELD_NAME, TestData_ORDER_PAGE.ORDER_DATA_1["name"])
        self.scroll_to_element(OrderPageLocator.FIELD_SECOND_NAME)
        self.click_to_element(OrderPageLocator.FIELD_SECOND_NAME)
        self.add_text_to_element(OrderPageLocator.FIELD_SECOND_NAME, TestData_ORDER_PAGE.ORDER_DATA_1["second_name"])

