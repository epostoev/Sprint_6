from selenium.webdriver.common.by import By


class MainPageLocators:
    # Раздел "Вопросы о важном"
    QUESTION_LOCATORS = (By.XPATH, ".//div[contains(@id, 'accordion__heading-{}')]")
    # question = {
    #     1: (By.XPATH, ".//div[contains(@id, 'accordion__heading-0')]"),
    #     2: (By.XPATH, ".//div[contains(@id, 'accordion__heading-1')]"),
    #     3: (By.XPATH, ".//div[contains(@id, 'accordion__heading-2')]"),
    #     4: (By.XPATH, ".//div[contains(@id, 'accordion__heading-3')]"),
    #     5: (By.XPATH, ".//div[contains(@id, 'accordion__heading-4')]"),
    #     6: (By.XPATH, ".//div[contains(@id, 'accordion__heading-5')]"),
    #     7: (By.XPATH, ".//div[contains(@id, 'accordion__heading-6')]"),
    #     8: (By.XPATH, ".//div[contains(@id, 'accordion__heading-7')]")
    # }
    ANSWER_LOCATORS = (By.XPATH, ".//div[contains(@id, 'accordion__panel-{}')]")
    # answer = {
    #     1: (By.XPATH, ".//div[contains(@id, 'accordion__panel-0')]"),
    #     2: (By.XPATH, ".//div[contains(@id, 'accordion__panel-1')]"),
    #     3: (By.XPATH, ".//div[contains(@id, 'accordion__panel-2')]"),
    #     4: (By.XPATH, ".//div[contains(@id, 'accordion__panel-3')]"),
    #     5: (By.XPATH, ".//div[contains(@id, 'accordion__panel-4')]"),
    #     6: (By.XPATH, ".//div[contains(@id, 'accordion__panel-5')]"),
    #     7: (By.XPATH, ".//div[contains(@id, 'accordion__panel-6')]"),
    #     8: (By.XPATH, ".//div[contains(@id, 'accordion__panel-7')]"),
    # }
    QUESTION_LOCATORS_TO_SCROLL = (By.XPATH, ".//div[contains(@id, 'accordion__heading-7')]")
