from wrapper import SeleniumWrapper
from selenium.webdriver.common.by import By

username_input_by_id = "username"
password_input_by_id = "password"
sign_in_button_by_css = "#login-form>form>input[name='login'][type='submit']"


# http://185.246.65.76:8080/login
class LogInPage(SeleniumWrapper):

    def click_sing_in_button(self):
        self.wait_button_clickable(By.CSS_SELECTOR, sign_in_button_by_css, 10)
        self.get_element_by_css(sign_in_button_by_css).click()

    def insert_username(self, username):
        self.wait_button_located(By.ID, username_input_by_id, 10)
        self.get_element_by_id(username_input_by_id).send_keys(username)

    def insert_password(self, password):
        self.wait_button_located(By.ID, password_input_by_id, 10)
        self.get_element_by_id(password_input_by_id).send_keys(password)
