from .base_page import BasePage

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

# class MainPage(BasePage): 
#     def go_to_login_page(self):
#         link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
#         link.click()
#         alert = self.browser.switch_to.alert
#         alert.accept()

#     def should_be_login_link(self):
#         assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
