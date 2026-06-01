from selenium.webdriver.common.by import By


class OrderPageLocator:
    FIELD_NAME = (
        By.XPATH,
        ".//div[contains(@class, 'Order_Form')]//input[@placeholder = '* Имя']")
    FIELD_SECOND_NAME = (
        By.XPATH,
        ".//div[contains(@class, 'Order_Form')]//input[@placeholder = '* Фамилия']")
    FIELD_ADDRESS = (
        By.XPATH,
        ".//div[contains(@class, 'Order_Form')]//input[@placeholder = '* Адрес: куда привезти заказ']")
    FIELD_SUBWAY = (
        By.XPATH,
        ".//div[contains(@class, 'Order_Form')]//input[@placeholder = '* Станция метро']")
    FIELD_PHONE = (
        By.XPATH,
        ".//div[contains(@class, 'Order_Form')]//input[@placeholder = '* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (
        By.XPATH,
        ".//div[contains(@class, 'Order_NextButton')]//button")
    SELECT_ITEM_IN_DROPDOWN_METRO = (
        By.XPATH, ".//ul[@class='select-search__options']//div[text()='{}']")

    # Экран второй аренды
    TITLE_PAGE_RENT_INFO = (
        By.XPATH, ".//div[contains(@class,'Order_Header')]")
    FIELD_DATA = (
        By.XPATH,
        ".//input[contains(@class, 'Input_Input') and contains(@placeholder, '* Когда привезти самокат')]")
    FIELD_RENT_PERIOD = (
        By.XPATH,
        ".//div[@class = 'Dropdown-placeholder' and text() = '* Срок аренды']")
    DROPDOWN_ITEM_RENTAL_PERIOD = (
        By.XPATH, ".//div[@class = 'Dropdown-menu']//div[text() = 'пятеро суток']")
    CHECKBOX_BLACK_COLOR_SAMOKAT = (
        By.XPATH,
        ".//input[@id = 'black']")
    FIELD_FOR_DELIVERY = (
        By.XPATH,
        ".//div[contains(@class, 'Input_Input')]//input[@placeholder='Комментарий для курьера']")
    BUTTON_MAKE = (
        By.XPATH,
        ".//div[contains(@class, 'Order_Button')]//button[text() = 'Заказать']")
    FIELD_COMMENTS = (
        By.XPATH,
        ".//input[contains (@class, 'Input_Input') and @placeholder = 'Комментарий для курьера']"
    )
    BUTTON_ORDER = (
        By.XPATH,
        ".//div[contains (@class, 'Order_Button')]//button[text() = 'Заказать']")
    BUTTON_CONFIM_ORDER = (
        By.XPATH,
        "//div[contains(@class, 'Order_Button')]//button[text() = 'Да']"
    )
    BUTTON_CHECK_STATUS_OF_ORDER = (
        By.XPATH,
        "//div[contains(@class, 'Order_NextButton')]//button[text() = 'Посмотреть статус']"
    )
