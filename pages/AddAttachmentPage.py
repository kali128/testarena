from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Locator(object):
    create_directory_button_id = 'createDirectoryButton'
    directory_name_id = 'directoryName'
    create_directory_popup_button_id = 'createDirectoryPopupButton'
    directory_list_css = '#directoryList'


class AddAttachmentPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.create_directory_button = driver.find_element(By.ID, Locator.create_directory_button_id)

    def create_directory(self, dir_name):
        self.create_directory_button.click()
        self.driver.find_element(By.ID, Locator.directory_name_id).send_keys(dir_name)
        self.driver.find_element(By.ID, Locator.create_directory_popup_button_id).click()

    def check_folder_exists(self, dir_name):
        wait = WebDriverWait(self.driver, 3)
        return wait.until(ec.text_to_be_present_in_element((By.CSS_SELECTOR, Locator.directory_list_css), dir_name))