from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage (BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login URL is not correct"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
    
    def register_new_user(self):
        fake_email = str(time.time()) + "@fakemail.org"
        fake_password = email = str(time.time()) + "fakepassword"
        
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL)
        email_field.send_keys(fake_email)

        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password_field.send_keys(fake_password)

        password2_field = self.browser.find_element(*LoginPageLocators.PASSWORD2)
        password2_field.send_keys(fake_password)
        
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()