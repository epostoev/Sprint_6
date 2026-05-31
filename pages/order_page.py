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
        locator_q_formatted = self.format_locators(OrderPageLocator.SELECT_ITEM_IN_DROPDOWN_METRO, data["subway"])
        self.click_to_element(locator_q_formatted)
        self.scroll_to_element(OrderPageLocator.FIELD_PHONE)
        self.click_to_element(OrderPageLocator.FIELD_PHONE)
        self.add_text_to_element(OrderPageLocator.FIELD_PHONE, data["phone"])
        self.click_to_element(OrderPageLocator.NEXT_BUTTON)

    @allure.step("Заполняем вторую страницу заказа")
    def set_second_page_info(self, data):
        self.find_element_with_wait(OrderPageLocator.TITLE_PAGE_RENT_INFO)
        self.scroll_to_element(OrderPageLocator.FIELD_DATA)
        self.click_to_element(OrderPageLocator.FIELD_DATA)
        self.add_text_to_element(OrderPageLocator.FIELD_DATA, data["date"])
        self.click_to_element(OrderPageLocator.TITLE_PAGE_RENT_INFO)
        self.scroll_to_element(OrderPageLocator.FIELD_RENT_PERIOD)
        self.click_to_element(OrderPageLocator.FIELD_RENT_PERIOD)
        self.click_to_element(OrderPageLocator.DROPDOWN_ITEM_RENTAL_PERIOD)
        self.scroll_to_element(OrderPageLocator.CHECKBOX_BLACK_COLOR_SAMOKAT)
        self.click_to_element(OrderPageLocator.CHECKBOX_BLACK_COLOR_SAMOKAT)
        self.scroll_to_element(OrderPageLocator.FIELD_COMMENTS)
        self.click_to_element(OrderPageLocator.FIELD_COMMENTS)
        self.add_text_to_element(OrderPageLocator.FIELD_COMMENTS, data["comment"])
        self.scroll_to_element(OrderPageLocator.BUTTON_ORDER)
        self.click_to_element(OrderPageLocator.BUTTON_ORDER)
        self.scroll_to_element(OrderPageLocator.BUTTON_CONFIM_ORDER)
        self.click_to_element(OrderPageLocator.BUTTON_CONFIM_ORDER)

    @allure.step("Проверить отображение кнопки ""Посмотреть статус"" после создания заказа")
    def check_displaying_of_button_check_status_of_order(self):
        element = self.find_element_with_wait(OrderPageLocator.BUTTON_CHECK_STATUS_OF_ORDER)
        return element.is_displayed()