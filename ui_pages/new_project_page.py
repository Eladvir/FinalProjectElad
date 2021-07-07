from selenium.webdriver.common.by import By
from wrapper import SeleniumWrapper

save_button_by_css = "div.op-form--submit>button.-highlight"
project_name_input_by_id = "formly_3_textInput_name_0"
advanced_settings_button_by_xpath = "//button[@type='button'][@class='op-fieldset--toggle']"
insert_text_to_description_by_css = "#formly_9_formattableInput_description_1>div>op-ckeditor>div>div>div>p"
status_dropdown_by_id = "formly_9_selectProjectStatusInput__links.status_4"
on_track_button_by_css = "div>span.-on-track"
more_options_by_class = "op-fieldset--fields"


class NewProjectPage(SeleniumWrapper):

    def click_on_advanced_settings_button(self):
        self.wait_button_clickable(By.XPATH, advanced_settings_button_by_xpath, 10)
        self.get_element_by_xpath(advanced_settings_button_by_xpath).click()

    def more_options_are_revealed(self):
        self.wait_button_located(By.CLASS_NAME, more_options_by_class, 10)
        return self.get_element_by_class(more_options_by_class)

    def click_on_track(self):
        self.wait_button_clickable(By.CSS_SELECTOR, on_track_button_by_css, 10)
        self.get_element_by_css(on_track_button_by_css).click()

    def click_on_save_button(self):
        self.wait_button_clickable(By.CSS_SELECTOR, save_button_by_css, 10)
        self.get_element_by_css(save_button_by_css).click()

    def insert_description_text(self, description_text):
        self.wait_button_located(By.CSS_SELECTOR, insert_text_to_description_by_css, 10)
        self.get_element_by_css(insert_text_to_description_by_css).send_keys(description_text)

    def insert_project_name(self, project_name):
        self.wait_button_located(By.ID, project_name_input_by_id, 10)
        self.get_element_by_id(project_name_input_by_id).send_keys(project_name)

    def click_on_status(self):
        self.wait_button_clickable(By.ID, status_dropdown_by_id, 10)
        status = self.get_element_by_id(status_dropdown_by_id)
        self.scrol_to(status)
        status.click()
