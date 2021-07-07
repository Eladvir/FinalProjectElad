from selenium.webdriver.common.by import By

from wrapper import SeleniumWrapper

create_type_button_by_css = "div>button.add-work-package"
insert_subject_task_by_id = "wp-new-inline-edit--field-subject"
insert_description_task_by_class = "document-editor__editable"
num_of_rows_by_css = "tr[data-class-identifier^= 'wp-row']"
save_button_by_id = "work-packages--edit-actions-save"
get_subject_by_css = "tr[data-class-identifier='wp-row-%s']>td>span>span[data-field-name=subject]"
get_type_by_css = "tr[data-class-identifier='wp-row-%s']>td>span>span[data-field-name=type]"
create_dropdown_by_css = "#types-context-menu>ul>li"
get_title_by_class = "work-packages--new-details-header"
save_task_success_by_class = "-success"
wait_rows_num_by_class = "wp-inline-create--add-link"


# http://185.246.65.76:8080/projects/PROJECT_NAME/work_packages

class WorkPackagesPage(SeleniumWrapper):

    def select_from_create_dropdown(self, create_title) -> bool:
        self.wait_button_located(By.CSS_SELECTOR, create_dropdown_by_css, 10)
        element = super().get_element_from_list_by_text_by_css(create_dropdown_by_css, create_title)
        if element is not None:
            print(element.text)
            element.click()
            return True
        return False

    def click_on_create_type(self):
        self.wait_button_located(By.CSS_SELECTOR, create_type_button_by_css, 10)
        self.get_element_by_css(create_type_button_by_css).click()

    def title_check(self) -> str:
        self.wait_button_located(By.CLASS_NAME, get_title_by_class, 10)
        return self.get_element_by_class(get_title_by_class).text.split("\n")

    def insert_subject(self, subject):
        self.wait_button_located(By.ID, insert_subject_task_by_id, 10)
        title_input = self.get_element_by_id(insert_subject_task_by_id)
        title_input.send_keys(subject)

    def insert_description(self, description):
        self.wait_button_located(By.CLASS_NAME, insert_description_task_by_class, 10)
        title_input = self.get_element_by_class(insert_description_task_by_class)
        title_input.send_keys(description)

    def get_num_rows(self) -> int:
        self.wait_button_located(By.CLASS_NAME, wait_rows_num_by_class, 10)
        return len(self.get_elements_by_css(num_of_rows_by_css))

    def click_on_save(self):
        self.wait_button_clickable(By.ID, save_button_by_id, 10)
        save_button = self.get_element_by_id(save_button_by_id)
        self.scrol_to(save_button)
        save_button.click()

    def get_last_row_type(self) -> str:
        last_row_id = self.get_last_row_id()
        self.wait_button_located(By.CSS_SELECTOR, get_type_by_css % last_row_id, 10)
        return self.get_element_by_css(get_type_by_css % last_row_id).text

    def get_last_row_subject(self) -> str:
        last_row_id = self.get_last_row_id()
        self.wait_button_located(By.CSS_SELECTOR, get_subject_by_css % last_row_id, 10)
        return self.get_element_by_css(get_subject_by_css % last_row_id).text

    def get_last_row_id(self) -> int:
        self.wait_button_located(By.CSS_SELECTOR, num_of_rows_by_css, 10)
        table = self.get_elements_by_css(num_of_rows_by_css)
        return table[len(table) - 1].text.split("\n")[0]

    def save_task_success(self):
        self.wait_button_located(By.CLASS_NAME, save_task_success_by_class, 10)
        self.wait_button_invisibility(By.CLASS_NAME, save_task_success_by_class, 10)
