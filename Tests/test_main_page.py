from Config.config import TestData
from Pages.main_page import MainPage
from Tests.test_base import BaseTest
import pytest


class TestMain(BaseTest):

    @pytest.fixture(scope='function')
    def setup(self, web_browser):
        self.main_page = MainPage(web_browser)

    @pytest.mark.usefixtures("setup")
    def test_main_page(self):
        """Проверка открытия главной страницы"""
        body = self.main_page.get_status_code(TestData.URL_MAIN)
        assert body == 200
        assert self.main_page.visible_button_login()



