from Base.base import WebPage
from Base.elements import WebElement
from Config.config import TestData


class MainPage(WebPage):
    log_in = WebElement(css_selector=".login.active")

    def __init__(self, web_browser, url=''):
        if not url:
            url = TestData.URL_MAIN
        super().__init__(web_browser, url)

    def visible_button_login(self):
        """Checking the visibility of the "login" button"""
        if self.log_in.is_visible():
            return True
        else:
            return False
