from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url, "URL is not correct"

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.login_form), "Login form is absent"

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.registration_form), "Registration form is absent"