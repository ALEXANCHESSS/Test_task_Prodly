from Config.config import TestData
from Pages.main_page import MainPage
from Tests.test_base import BaseTest


class TestMain(BaseTest):

    def test_main_page(self, web_browser):
        """Проверка открытия главной страницы"""
        self.main_page = MainPage(web_browser)
        body = self.main_page.get_satus_code(TestData.URL_MAIN)
        assert body == 200
        assert self.main_page.visible_button_login()



