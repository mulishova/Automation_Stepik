from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//div[contains(@class, 'basket')]//a[contains(@class, 'btn-default')]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    LOGIN_URL = ()
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_NAME = (By.XPATH, "//input[contains(@name, 'registration-email')]")
    REGISTER_PASSWORD = (By.XPATH, "//input[contains(@name, 'registration-password1')]")
    REGISTER_CONFIRM_PASSWORD = (By.XPATH, "//input[contains(@name, 'registration-password2')]")
    REGISTER_SUBMIT_BUTTON = (By.XPATH, "//button[contains(@name, 'registration_submit')]")


class ProductPageLocators():
    ADD_TO_BASKET = (By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]")
    ITEM_NAME = (By.XPATH, "//div[contains(@class, 'product_main')]/h1")
    ITEM_PRICE = (By.XPATH, "//div[contains(@class, 'product_main')]/p[contains(@class, 'price_color')]")
    ADDED_ITEM_NAME = (By.XPATH, "//div[contains(@class, 'alertinner')]/strong")
    ADDED_ITEM_PRICE = (By.XPATH, "//div[contains(@class, 'alertinner')]/p/strong")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'alertinner')]")


class BasketPageLocators():
    BASKET_ITEMS = (By.XPATH, "//form[contains(@class, 'basket')]")
    EMPTY_BASKET_LABEL = (By.XPATH, "//div[contains(@id, 'content_inner')]/p")
