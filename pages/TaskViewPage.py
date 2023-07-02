from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Locator(object):
    added_task_popup_id = 'j_info_box'
    task_title_id = 'text'


def wait_for_element(driver, locator):
    wait = WebDriverWait(driver, 3)
    wait.until(ec.presence_of_element_located((By.ID, locator)))


class TaskViewPage(object):
    def __init__(self, driver):
        self.driver = driver
        wait_for_element(driver, Locator.added_task_popup_id)
        self.added_task_popup = driver.find_element(By.ID, Locator.added_task_popup_id)
        self.task_title = driver.find_element(By.ID, Locator.task_title_id)

    def get_popup_text(self, expected_text):
        wait = WebDriverWait(self.driver, 3)
        return wait.until(ec.text_to_be_present_in_element((By.ID, Locator.added_task_popup_id), expected_text))
