from config import WebDriverSetup as wds
from constants import Texts as t
from scenarios import TestArenaScenario as tas
from models import Task
from pages import AfterLoginPage as alp
from pages import TaskTabPage as tp
from pages import AddTaskPage as adp
from pages import TaskViewPage as tvp


def test_add_new_task_to_project():
    driver = wds.setup()
    task = Task.Task(environments='aaa', versions='1.0-SNAPSHOT')

    tas.login_to_test_arena(driver)
    alp.AfterLoginPage(driver).go_to_task_page()
    tp.TaskTabPage(driver).click_add_task()
    adp.AddTaskPage(driver).add_task(task)

    page = tvp.TaskViewPage(driver)
    assert page.get_popup_text(t.Texts.TASK_ADDED.value)
    assert page.task_title.text.endswith(task.title)

    wds.cleanup(driver)
