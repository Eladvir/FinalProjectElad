from selenium import webdriver
import open_project_config
from ui_pages.my_page import MyPage
from ui_pages.project_page import ProjectPage
from ui_pages.login_page import LogInPage
from ui_pages.new_project_page import NewProjectPage
from ui_pages.work_packages_page import WorkPackagesPage

driver = webdriver.Chrome("C:\\Users\\elad\\PycharmProjects\\chromedriver.exe")

project_page = ProjectPage(driver)
my_page = MyPage(driver)
new_project_page = NewProjectPage(driver)
work_packages_page = WorkPackagesPage(driver)
login_page = LogInPage(driver)

PROJECT_NAME = "Elad Dvir!! FINAL ONE"
USERNAME = open_project_config.ui_config["username"]
PASSWORD = open_project_config.ui_config["password"]
DESCRIPTION_TEXT = "this is description text"


def test_create_project():
    driver.get("http://185.246.65.76:8080/login")
    driver.maximize_window()
    login_page.insert_username(USERNAME)  # Enter a username into the login form
    login_page.insert_password(PASSWORD)  # Enter a password into the login form
    login_page.click_sing_in_button()  # Clicking the login button on the form
    my_page.click_on_green_plus()
    my_page.click_on_new_project()

    new_project_page.insert_project_name(PROJECT_NAME)
    new_project_page.click_on_advanced_settings_button()
    assert new_project_page.more_options_are_revealed().is_displayed(), f"more options are revealed not display"
    new_project_page.insert_description_text(DESCRIPTION_TEXT)

    new_project_page.click_on_status()
    new_project_page.click_on_track()

    new_project_page.click_on_save_button()

    assert PROJECT_NAME == project_page.checking_project_name(), f"The project name isn't {PROJECT_NAME}"
    driver.quit()
