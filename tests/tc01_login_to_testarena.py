from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_to_test_arena():
    chrome_driver = webdriver.Chrome()

    chrome_driver.get('http://testarena.pl/demo')
    chrome_driver.maximize_window()

    title = 'TestArena'
    assert title == chrome_driver.title

    login_detiles = chrome_driver.find_elements(By.CSS_SELECTOR, '.description')[0].text.split('\n')
    login = str([i for i in login_detiles if i.startswith('Login: ')][0]).replace('Login: ', '')
    password = str([i for i in login_detiles if i.startswith('Hasło:')][0]).replace('Hasło: ', '')

    chrome_driver.find_elements(By.CSS_SELECTOR, '.btn.btn-fill.btn-primary')[0].click()

    current_tab = chrome_driver.current_window_handle
    all_tabs = chrome_driver.window_handles

    chrome_driver.switch_to.window(all_tabs[1])

    title = 'TestArena Demo'
    assert title == chrome_driver.title

    input_login = chrome_driver.find_elements(By.ID, 'email')[0]
    input_login.send_keys(login)

    input_password = chrome_driver.find_elements(By.ID, 'password')[0]
    input_password.send_keys(password)

    button_login = chrome_driver.find_elements(By.ID, 'login')[0]
    button_login.click()

    title = 'Kokpit - TestArena Demo'
    assert title == chrome_driver.title

    chrome_driver.close()
