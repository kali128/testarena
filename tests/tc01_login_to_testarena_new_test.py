from config import WebDriverSetup as wds
from constants import Texts as t
from scenarios import TestArenaScenario as tas


def test_login_to_test_arena():
    driver = wds.setup()
    tas.login_to_test_arena(driver)

    assert driver.title == t.Texts.AFTER_LOGON_PAGE_TITLE.value

    wds.cleanup(driver)
