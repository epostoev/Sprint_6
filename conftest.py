import pytest
from selenium import webdriver
from data import URLS
from pages.main_page import MainPage

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(URLS.BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.timeout = 10
    return page
