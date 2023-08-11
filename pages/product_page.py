from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    item_name = ''
    item_price = ''

    def check_item_info_before_adding_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_NAME), "Item name is not present"
        assert self.is_element_present(*ProductPageLocators.ITEM_PRICE), "Item price is not present"
        self.item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        self.item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        print(f"item price = {self.item_price}")
        print(f"item name = {self.item_name}")

    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Add to busket button is not presented"

    def add_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_btn.click()
        assert self.solve_quiz_and_get_code(), "the quiz has not been solved"
        time.sleep(3)

    def check_item_info_after_adding_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_ITEM_NAME), "Item name in the basket is not present"
        assert self.is_element_present(*ProductPageLocators.ADDED_ITEM_PRICE), "Item price in the basket is not present"
        print(f"new name = {self.browser.find_element(*ProductPageLocators.ADDED_ITEM_NAME).text}")
        print(f"new price = {self.browser.find_element(*ProductPageLocators.ADDED_ITEM_PRICE).text}")
        assert self.item_name == self.browser.find_element(*ProductPageLocators.ADDED_ITEM_NAME).text, "product name after adding to basket is different"
        assert self.item_price == self.browser.find_element(*ProductPageLocators.ADDED_ITEM_PRICE).text, "the price after adding to the basket is different"

