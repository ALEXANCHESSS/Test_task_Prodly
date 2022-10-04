from Pages.auth_page import AuthPage
from Tests.test_base import BaseTest


class TestAuth(BaseTest):


    def test_registration(self, web_browser):
        self.auth_page = AuthPage(web_browser)
        self.auth_page.sign_up.click()
        self.auth_page.

    def test_login(self, web_browser):
        self.auth_page = AuthPage(web_browser)





