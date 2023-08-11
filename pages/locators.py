from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = ()
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register-form")


class ProductPageLocators():
    ADD_TO_BASKET = (By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]")
    ITEM_NAME = (By.XPATH, "//div[contains(@class, 'product_main')]/h1")
    ITEM_PRICE = (By.XPATH, "//div[contains(@class, 'product_main')]/p[contains(@class, 'price_color')]")
    ADDED_ITEM_NAME = (By.XPATH, "//div[contains(@class, 'alertinner')]/strong")
    ADDED_ITEM_PRICE = (By.XPATH, "//div[contains(@class, 'alertinner')]/p/strong")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'alertinner') and contains(string(), 'has been added')]")
