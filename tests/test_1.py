from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from locators import MainPageLocators, AuthLocators, AddPostOrder, ProfileLocators
from data import URLS
from datetime import datetime
import time

class Test_1:
    def test_1(self, driver):
        wait = WebDriverWait
        input(f"\nHello World")
