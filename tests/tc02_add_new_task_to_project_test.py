from config import WebDriverSetup as wds
from constants import Texts as t
from scenarios import TestArenaScenario as tas
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_add_new_task_to_project():
    driver = wds.setup()
    tas.login_to_test_arena(driver)
    wait = WebDriverWait(driver, 3)

    task = {
        'title': 'NEW TASK',
        'description': 'New task description',
        'environments': 'dev test 1',
        'versions': 'test123',
        'date': '2023-07-30 23:59'
    }

    #TODO stworzyć page object do strony po logowaniu
    driver.find_element(By.CLASS_NAME, 'item6').click()
    driver.find_element(By.CLASS_NAME, 'button_link').click()

    #TODO stworzyć page object do strony zkładania zadania
    driver.find_element(By.ID, 'title').send_keys(task['title'])
    driver.find_element(By.ID, 'description').send_keys(task['description'])

    driver.find_element(By.ID, 'token-input-environments').send_keys(task['environments'])
    wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'token-input-dropdown-item2-facebook')))
    driver.find_element(By.ID, 'token-input-environments').send_keys(Keys.RETURN)

    driver.find_element(By.ID, 'token-input-versions').send_keys(task['versions'])
    wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'token-input-dropdown-item2-facebook')))
    driver.find_element(By.ID, 'token-input-versions').send_keys(Keys.RETURN)

    driver.find_element(By.ID, 'dueDate').send_keys(task['date'])
    driver.find_element(By.ID, 'dueDate').send_keys(Keys.RETURN)

    driver.find_element(By.ID, 'j_assignToMe').click()

    driver.find_element(By.ID, 'save').click()

    assert wait.until(ec.text_to_be_present_in_element((By.ID, 'j_info_box'), t.Texts.TASK_ADDED.value))
    assert driver.find_element(By.ID, 'text').text.endswith(task['title'])

    wds.cleanup(driver)
