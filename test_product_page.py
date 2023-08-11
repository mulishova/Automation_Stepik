from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.check_item_info_before_adding_to_basket()
    page.should_be_add_to_basket_btn()
    page.add_to_basket()
    page.check_item_info_after_adding_to_basket()
