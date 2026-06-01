from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


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
        return self.driver.find_element(*locator)

    @allure.step("Кликаем по элементу")
    def click_to_element(self, some):
        self.wait.until(
            EC.element_to_be_clickable(some))
        self.driver.find_element(*some).click()

    def wait_text(self, locator, text):
        self.wait.until_not(
            EC.text_to_be_present_in_element_value(locator, text))
        return self.driver.find_element(*locator).text

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)

        return method, locator

    @allure.step("Ждём открытия новой вкладки")
    def wait_for_new_window(self, expected_count):
        WebDriverWait(self.driver, 10).until(
            EC.number_of_windows_to_be(expected_count))

    @allure.step("Переключаемся на новую вкладку")
    def switch_to_another_window(self):
        windows_list = self.driver.window_handles
        self.driver.switch_to.window(windows_list[-1])

    @allure.step("Ждём редирект на {url_part}")
    def wait_for_url_contains(self, url_part, timeout=30):
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(url_part)
        )

    @allure.step("Прокручиваем страницу до элемента")
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("")
    def get_current_url(self):
        return self.driver.current_url