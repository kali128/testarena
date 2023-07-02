from config import WebDriverSetup as wds
from pages import BasePage as bp
from pages import LoginPage as lp
from constants import Texts as t
from utils import Browser as b


def test_login_to_test_arena():
    driver = wds.setup()
    home = bp.Home(driver)
    credentials = home.get_credentials()
    home.go_to_login_page()
    b.switch_to_last_tab(driver)
    login = lp.LoginPage(driver)
    login.log_in(credentials['login'], 'invalid_password')

    assert login.get_error_message_text() == t.Texts.LOGIN_ERROR_MESSAGE.value

    wds.cleanup(driver)
