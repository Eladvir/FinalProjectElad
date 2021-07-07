from selenium.webdriver.common.by import By

from wrapper import SeleniumWrapper

menu_sidebar_by_css = "#menu-sidebar>ul>li"
work_overview_by_name = "editable-toolbar-title"
projects_menu_by_id = "projects-menu"


# http://185.246.65.76:8080/projects/
class ProjectPage(SeleniumWrapper):

    def checking_project_name(self) -> str:
        self.wait_button_located(By.NAME, work_overview_by_name, 10)
        return self.get_element_by_id(projects_menu_by_id).text

    def select_from_menu_sidebar(self, project_overview_title) -> bool:
        self.wait_button_clickable(By.CSS_SELECTOR, menu_sidebar_by_css, 10)
        element = self.get_element_from_list_by_text_by_css(menu_sidebar_by_css, project_overview_title)
        if element is not None:
            element.click()
            return True
        return False
