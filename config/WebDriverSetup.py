from selenium import webdriver


def setup(url='http://testarena.pl/demo'):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    return driver


def cleanup(driver):
    if driver is not None:
        driver.close()
        driver.quit()
