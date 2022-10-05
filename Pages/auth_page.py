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
    add_store = WebElement(xpath='//a[contains(text(), "Добавить торговую точку")]')
    error_login = WebElement(css_selector='.input-wrap.password-wrap')
    close_add_store = WebElement(css_selector='.close-icon.btnClose')
    personal_area = WebElement(css_selector='.personal-area')
    button_logout = WebElement(xpath='//a[contains(text(), "Выход")]')



    def __init__(self, web_browser, url='https://stage.prodly.ru/login'):
        if not url:
            url = TestData.URL_MAIN
        super().__init__(web_browser, url)

    def log_in(self, login, psw):
        self.tel_or_login.send_keys(login)
        self.password.send_keys(psw)
        self.button_login.click()

    def visible_fields_mail_and_psw(self):
        self.wait_page_loaded(timeout=20)
        if self.tel_or_login.is_visible() and self.password.is_visible():
            return True
        else:
            return False

    def registry_new_account(self, name, tel, mail, psw, code=''):
        self.name.send_keys(name)
        self.tel.send_keys(tel)
        self.mail.send_keys(mail)
        self.psw.send_keys(psw)
        self.code.send_keys(code)
        self.submit_reg.click()

    def visible_button_add_store(self):
        self.wait_page_loaded(timeout=20)
        if self.add_store.is_visible():
            return True
        else:
            return False

    def visible_button_error_login(self):
        if self.error_login.is_visible():
            return True
        else:
            return False

    def close_window_with_add_store(self):
        self.close_add_store.click()

    def logout_personal_area(self):
        self.personal_area.click()
        self.button_logout.click()




