from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys


class Locator(object):
    title_id = 'title'
    description_id = 'description'
    environment_id = 'token-input-environments'
    version_id = 'token-input-versions'
    due_date_id = 'dueDate'
    assign_to_me_id = 'j_assignToMe'
    dropdown_class = 'token-input-dropdown-item2-facebook'
    save_id = 'save'


def wait_for_dropdown(driver):
    wait = WebDriverWait(driver, 3)
    wait.until(ec.presence_of_element_located((By.CLASS_NAME, Locator.dropdown_class)))


class AddTaskPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.title = driver.find_element(By.ID, Locator.title_id)
        self.description = driver.find_element(By.ID, Locator.description_id)
        self.environment = driver.find_element(By.ID, Locator.environment_id)
        self.version = driver.find_element(By.ID, Locator.version_id)
        self.due_date = driver.find_element(By.ID,  Locator.due_date_id)
        self.assign_to_me = driver.find_element(By.ID,  Locator.assign_to_me_id)
        self.save = driver.find_element(By.ID,  Locator.save_id)

    def add_task(self, task):
        self.title.send_keys(task.title)
        self.description.send_keys(task.description)
        self.environment.send_keys(task.environments)
        wait_for_dropdown(self.driver)
        self.environment.send_keys(Keys.RETURN)
        self.version.send_keys(task.versions)
        wait_for_dropdown(self.driver)
        self.version.send_keys(Keys.RETURN)
        self.due_date.send_keys(task.date)
        self.due_date.send_keys(Keys.RETURN)
        self.assign_to_me.click()
        self.save.click()
