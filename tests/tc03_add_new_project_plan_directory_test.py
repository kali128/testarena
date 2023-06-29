from config import WebDriverSetup as wds
from scenarios import TestArenaScenario as tas
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utils import Browser as b
from utils import Functions as f


def test_add_new_project_plan_directory():
    driver = wds.setup()
    tas.login_to_test_arena(driver)
    wait = WebDriverWait(driver, 3)

    dir_name = 'new_test_folder_' + f.generate_string()

    #TODO stworzyć page object do strony po logowaniu
    driver.find_element(By.CLASS_NAME, 'item3').click()

    #TODO stworzyć page object do strony projektu
    driver.find_element(By.CSS_SELECTOR, '.button_link_nav').click()
    driver.find_element(By.CSS_SELECTOR, '#j_projectAddPlan').click()

    b.switch_to_last_tab(driver)

    #TODO stworzyć page object do strony zarządzania plikami/kaltalogami
    driver.find_element(By.ID, 'createDirectoryButton').click()
    driver.find_element(By.ID, 'directoryName').send_keys(dir_name)
    driver.find_element(By.ID, 'createDirectoryPopupButton').click()

    assert wait.until(ec.text_to_be_present_in_element((By.CSS_SELECTOR, '#directoryList'), dir_name))

    #TODO wywalić stworzony katalog

    wds.cleanup(driver)
