from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login url is not present"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"

    def should_be_register_name_field(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_NAME), "Registration Name field is not presented"

    def should_be_register_password_field(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD), "Registration Password field is not " \
                                                                              "presented "

    def should_be_register_confirm_password_field(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD), "Registration Confirm Password " \
                                                                                      "field is not presented "

    def should_be_register_submit_button(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_SUBMIT_BUTTON), "Registration Submit Button field " \
                                                                                   "is not presented "

    def register_new_user(self, email, password):
        self.should_be_register_name_field()
        self.should_be_register_password_field()
        self.should_be_register_confirm_password_field()
        self.should_be_register_submit_button()

        self.browser.find_element(*LoginPageLocators.REGISTER_NAME).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT_BUTTON).click()




