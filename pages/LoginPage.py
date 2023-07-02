from selenium.webdriver.common.by import By


class Locator(object):
    input_email_id = 'email'
    input_password_id = 'password'
    button_login_id = 'login'
    error_class = 'login_form_error'


class LoginPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.email = driver.find_element(By.ID, Locator.input_email_id)
        self.password = driver.find_element(By.ID, Locator.input_password_id)
        self.login = driver.find_element(By.ID, Locator.button_login_id)

    def log_in(self, login, password):
        self.email.send_keys(login)
        self.password.send_keys(password)
        self.login.click()

    def get_error_message_text(self):
        return self.driver.find_element(By.CLASS_NAME, Locator.error_class).text
