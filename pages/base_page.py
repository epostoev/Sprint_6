from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 5
        self.wait = WebDriverWait(self.driver, self.timeout)
    
    def go_to_url(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        self.wait.until(
            EC.visibility_of_element_located(locator))
        return self.driver_element(*locator)
    
    def click_to_element(self, some):
        self.wait.until(
            EC.element_to_be_clickable(some))
        self.driver.find_element(*some).click()

    def wait_text(self, locator, text):
        self.wait.until_not(
            EC.text_to_be_present_in_element_value(locator, text))
        return  self.driver.find_element(*locator).text
    
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text
    
    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)

        return method, locator
    
    def swith_to_another_window(self):
        windows_list = self.driver.window_handles
        self.driver.swith_to_window(windows_list[-1])