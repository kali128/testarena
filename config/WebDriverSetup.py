from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import os


def setup(url='http://testarena.pl/demo'):
    if os.getenv('HEADLESS') == 'True':
        driver = headless_mode()
    else:
        driver = webdriver.Chrome()
        driver.maximize_window()
    driver.wait = WebDriverWait(driver, 3)
    driver.get(url)
    return driver


def cleanup(driver):
    if driver is not None:
        driver.close()
        driver.quit()


def headless_mode():
    options = Options()
    options.add_argument("--headless")
    return webdriver.Chrome(options=options)
