import allure
import pytest
from data import URLS, ExpectedURLS
from pages.main_page import MainPage
from locators.main_page_locator import MainPageLocators


class TestLogoRedirect:

    def test_logoredirect_to_yandex_success(self, main_page):
        main_page.go_to_url(URLS.BASE_URL)
        main_page.wait_visibility_of_header_logo_yandex()
        main_page.click_to_element(MainPageLocators.LOGO_YANDEX)
        main_page.wait_for_new_window(2)
        main_page.switch_to_another_window()
        main_page.wait_for_url_contains(ExpectedURLS.YANDEX, timeout=30)

        assert ExpectedURLS.YANDEX in main_page.driver.current_url

    def test_logoredirect_to_scooter_main_page_success(self, main_page):
        main_page.go_to_url(URLS.BASE_URL)
        main_page.click_to_element(MainPageLocators.LOGO_SAMOKAT)

        assert main_page.driver.current_url == URLS.BASE_URL
