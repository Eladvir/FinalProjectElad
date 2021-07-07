from selenium import webdriver

import open_project_config
from ui_pages.login_page import LogInPage
from ui_pages.project_page import ProjectPage
from ui_pages.my_page import MyPage
from ui_pages.new_project_page import NewProjectPage
from ui_pages.work_packages_page import WorkPackagesPage

driver = webdriver.Chrome("C:\\Users\\elad\\PycharmProjects\\chromedriver.exe")

project_page = ProjectPage(driver)
my_page = MyPage(driver)
new_project = NewProjectPage(driver)
work_packages_page = WorkPackagesPage(driver)
login_page = LogInPage(driver)

PROJECTNAMETOOPEN = "Elad Dvir!! FINAL ONE"
USERNAME = open_project_config.ui_config["username"]
PASSWORD = open_project_config.ui_config["password"]
EXPECTED_TITEL_TO_CHECK = ['New', 'TASK']
TASK_SUBJECT = "titel $ task"
TASK_DESCTIPTION = "this is the description!!!"
SELECT_FROM_CREATE_DROPDOWN = "TASK"
SELECT_FROM_MENU_SIDEBAR = "Work packages"


def test_create_task():
    driver.get("http://185.246.65.76:8080/login")
    login_page.insert_username(USERNAME)  # Enter a username into the login form
    login_page.insert_password(PASSWORD)  # Enter a password into the login form
    login_page.click_sing_in_button()  # Clicking the login button on the form
    my_page.click_on_select_project(PROJECTNAMETOOPEN)  # Opening a particular project out of all the projects
    project_page.select_from_menu_sidebar(SELECT_FROM_MENU_SIDEBAR)
    current_num_of_rows = work_packages_page.get_num_rows()
    work_packages_page.click_on_create_type()
    work_packages_page.select_from_create_dropdown(SELECT_FROM_CREATE_DROPDOWN)
    assert work_packages_page.title_check() == EXPECTED_TITEL_TO_CHECK, f"the titel isn't:{EXPECTED_TITEL_TO_CHECK}"
    work_packages_page.insert_subject(TASK_SUBJECT)
    work_packages_page.insert_description(TASK_DESCTIPTION)
    work_packages_page.click_on_save()
    work_packages_page.save_task_success()
    assert work_packages_page.get_num_rows() == current_num_of_rows + 1, f"The number of table number of rows isn't {current_num_of_rows} + 1 row "
    assert TASK_SUBJECT == work_packages_page.get_last_row_subject(), f"The subject of the task isn't match the subject {TASK_SUBJECT}."
    assert SELECT_FROM_CREATE_DROPDOWN == work_packages_page.get_last_row_type(), f"The task type isn't {SELECT_FROM_CREATE_DROPDOWN}"
    driver.quit()
