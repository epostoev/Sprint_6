from selenium.webdriver.common.by import By


class MainPageLocators:

    # Кнопки на главной странице
    ORDER_BUTTON_UP = (
        By.XPATH,
        ".//div[contains(@class, 'Header_Nav')]//button[contains(@class, 'Button_Button')]")
    ORDER_BUTTON_DOWN = (
        By.XPATH,
        ".//div[contains(@class, 'Home_FinishButton')]//button[contains(@class, 'Button_Button')]")

    # Раздел "Вопросы о важном"
    QUESTION_LOCATORS = (
        By.XPATH,
        ".//div[contains(@id, 'accordion__heading-{}')]")
    ANSWER_LOCATORS = (
        By.XPATH,
        ".//div[contains(@id, 'accordion__panel-{}')]")
    QUESTION_LOCATORS_TO_SCROLL = (
        By.XPATH, ".//div[contains(@id, 'accordion__heading-7')]")
