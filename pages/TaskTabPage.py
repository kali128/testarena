from selenium.webdriver.common.by import By


class Locator(object):
    add_task_class = 'button_link'


class TaskTabPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.add_task = driver.find_element(By.CLASS_NAME, Locator.add_task_class)

    def click_add_task(self):
        self.add_task.click()
