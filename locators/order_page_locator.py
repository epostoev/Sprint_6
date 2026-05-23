from selenium.webdriver.common.by import By

class OrderPageLocator:
    FIELD_NAME = (By.XPATH, ".//div[contains(@class, 'Order_Form')]//input[@placeholder = '* Имя']")
    FIELD_SECOND_NAME = (By.XPATH, ".//div[contains(@class, 'Order_Form')]//input[@placeholder = '* Фамилия']")
    FIELD_ADDRESS = (By.XPATH, ".//div[contains(@class, 'Order_Form')]//input[@placeholder = '* Адрес: куда привезти заказ']")
    FIELD_SUBWAY = (By.XPATH, ".//div[contains(@class, 'Order_Form')]//input[@placeholder = '* Станция метро']")
    FIELD_PHONE = (By.XPATH, ".//div[contains(@class, 'Order_Form')]//input[@placeholder = '* Телефон: на него позвонит курьер']")