from selenium.webdriver.common.by import By


class Locator(object):
    add_attachment_css = '.button_link_nav'
    attachment_type_plan_css = '#j_projectAddPlan'


class ProjectTabPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.add_attachment = driver.find_element(By.CSS_SELECTOR, Locator.add_attachment_css)

    def add_attachment_plan(self):
        self.add_attachment.click()
        self.driver.find_element(By.CSS_SELECTOR, Locator.attachment_type_plan_css).click()
