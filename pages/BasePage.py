from selenium.webdriver.common.by import By


class Locator(object):
    login_details_css = '.description'
    demo_button_css = '.btn.btn-fill.btn-primary'


class Home(object):
    def __init__(self, driver):
        self.driver = driver
        self.login_details = driver.find_element(By.CSS_SELECTOR, Locator.login_details_css)
        self.demo_button = driver.find_element(By.CSS_SELECTOR, Locator.demo_button_css)

    def get_credentials(self):
        details = self.login_details.text.split('\n')
        login = str([i for i in details if i.startswith('Login: ')][0]).replace('Login: ', '')
        password = str([i for i in details if i.startswith('Hasło:')][0]).replace('Hasło: ', '')
        return {'login': login, 'pass': password}

    def go_to_login_page(self):
        self.demo_button.click()
