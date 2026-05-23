import allure
import data
from pages.base_page import BasePage
from locators.main_page_locator import MainPageLocators
from locators.order_page_locator import OrderPageLocator
from data import TestData_ORDER_PAGE

class OrderPage(BasePage):
    

    @allure.step("Заполняем первую страницу заказа")
    def set_first_page_info(self, data):
        self.scroll_to_element(OrderPageLocator.FIELD_NAME)
        self.click_to_element(OrderPageLocator.FIELD_NAME)
        self.add_text_to_element(OrderPageLocator.FIELD_NAME, data["name"])
        self.scroll_to_element(OrderPageLocator.FIELD_SECOND_NAME)
        self.click_to_element(OrderPageLocator.FIELD_SECOND_NAME)
        self.add_text_to_element(OrderPageLocator.FIELD_SECOND_NAME, data["second_name"])
        self.scroll_to_element(OrderPageLocator.FIELD_ADDRESS)
        self.click_to_element(OrderPageLocator.FIELD_ADDRESS)
        self.add_text_to_element(OrderPageLocator.FIELD_ADDRESS, data["address"])
        self.scroll_to_element(OrderPageLocator.FIELD_SUBWAY)
        self.click_to_element(OrderPageLocator.FIELD_SUBWAY)
        self.add_text_to_element(OrderPageLocator.FIELD_SUBWAY, data["subway"])

        locator_q_formatted = self.format_locators(
            OrderPageLocator.SELECT_ITEM_IN_DROPDOWN_METRO, data["subway"])
        self.click_to_element(locator_q_formatted)
        input()
        self.scroll_to_element(OrderPageLocator.FIELD_PHONE)
        self.click_to_element(OrderPageLocator.FIELD_PHONE)
        self.add_text_to_element(OrderPageLocator.FIELD_PHONE, data["phone"])
        self.click_to_element(OrderPageLocator.NEXT_BUTTON)

