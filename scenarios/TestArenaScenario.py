from pages import BasePage as bp
from pages import LoginPage as lp
from utils import Browser as b


def login_to_test_arena(driver):
    home = bp.Home(driver)
    credentials = home.get_credentials()
    home.go_to_login_page()
    b.switch_to_last_tab(driver)
    lp.LoginPage(driver).log_in(credentials['login'], credentials['pass'])
