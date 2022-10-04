from Base.base import WebPage
from Base.elements import WebElement
from Config.config import TestData


class AuthPage(WebPage):

    tel_or_login = WebElement(css_selector="#loginUsername")
    password = WebElement(css_selector="#loginPassword")
    button_login = WebElement(css_selector=".send")
    sign_up = WebElement(css_selector=".sign-up-link")
    name = WebElement(css_selector="input[name='name']")
    tel = WebElement(css_selector="input[name='phone']")
    mail = WebElement(css_selector="input[name='email']")
    psw = WebElement(css_selector="input[name='password']")
    code = WebElement(css_selector="input[name='reg_id']")
    submit_reg = WebElement(css_selector=".send")


    def __init__(self, web_browser, url='https://stage.prodly.ru/login'):
        if not url:
            url = TestData.URL_MAIN
        super().__init__(web_browser, url)

    def log_in(self, login, psw):
        self.tel_or_login.send_keys(login)
        self.password.send_keys(psw)
        self.button_login.click()

    def registry_new_account(self, name, tel, mail, psw, code=''):
        self.name.send_keys(name)
        self.tel.send_keys(tel)
        self.mail.send_keys(mail)
        self.psw.send_keys(psw)
        self.code.send_keys(code)
        self.submit_reg.click()




