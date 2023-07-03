from config import WebDriverSetup as wds
from scenarios import TestArenaScenario as tas
from utils import Browser as b
from utils import Functions as f
from pages import AfterLoginPage, ProjectTabPage, AddAttachmentPage


def test_add_new_project_plan_directory():
    driver = wds.setup()
    dir_name = 'new_test_folder_' + f.generate_string()

    tas.login_to_test_arena(driver)
    AfterLoginPage.AfterLoginPage(driver).go_to_project_page()
    ProjectTabPage.ProjectTabPage(driver).add_attachment_plan()
    b.switch_to_last_tab(driver)
    attachment = AddAttachmentPage.AddAttachmentPage(driver)
    attachment.create_directory(dir_name)

    assert attachment.check_folder_exists(dir_name)

    attachment.delete_folder_by_name(dir_name)

    wds.cleanup(driver)
