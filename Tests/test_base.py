import pytest

from Config.config import TestData
from Pages.main_page import MainPage


@pytest.mark.usefixtures("web_browser")
class BaseTest:
    pass
