from selenium.webdriver.common.by import By

from wrapper import SeleniumWrapper

green_plus_button_by_xpath = "//a[@title='Open quick add menu']"
new_project_button_by_xpath = "//a[@title='New project']"
projects_menu_by_id = "projects-menu"
all_projects_name_by_class = "ui-menu-item-wrapper"


# http://185.246.65.76:8080/my/page
class MyPage(SeleniumWrapper):

    def click_on_green_plus(self):
        self.wait_button_clickable(By.XPATH, green_plus_button_by_xpath, 10)
        self.get_element_by_xpath(green_plus_button_by_xpath).click()

    def click_on_new_project(self):
        self.wait_button_clickable(By.XPATH, new_project_button_by_xpath, 10)
        self.get_element_by_xpath(new_project_button_by_xpath).click()

    def click_on_select_project(self, project_name):
        self.click_on_projects_menu()
        self.wait_button_clickable(By.CLASS_NAME, all_projects_name_by_class, 10)
        self.get_element_from_list_by_text_by_class(all_projects_name_by_class, project_name).click()

    def click_on_projects_menu(self):
        self.wait_button_clickable(By.ID, projects_menu_by_id, 10)
        self.get_element_by_id(projects_menu_by_id).click()
