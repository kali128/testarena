from selenium.webdriver.common.by import By


class Locator(object):
    project_tab_class = 'item3'
    task_tab_class = 'item6'


class AfterLoginPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.project_tab = driver.find_element(By.CLASS_NAME, Locator.project_tab_class)
        self.task_tab = driver.find_element(By.CLASS_NAME, Locator.task_tab_class)

    def go_to_task_page(self):
        self.task_tab.click()

    def go_to_project_page(self):
        self.project_tab.click()
