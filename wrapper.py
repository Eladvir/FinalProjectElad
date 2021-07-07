from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class SeleniumWrapper:
    driver: WebDriver

    def __init__(self, driver):
        self.driver: webdriver = driver

    def get_element_by_id(self, element_id):
        try:
            return self.driver.find_element_by_id(element_id)
        except NoSuchElementException as e:
            return None

    def get_element_by_xpath(self, xpath):
        try:
            return self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException as e:
            return None

    def get_elements_by_xpath(self, xpath):
        try:
            return self.driver.find_elements_by_xpath(xpath)
        except NoSuchElementException as e:
            return None

    def get_element_by_class(self, class_name):
        try:
            return self.driver.find_element_by_class_name(class_name)
        except NoSuchElementException as e:
            return None

    def get_element_by_css(self, css_selector):
        try:
            return self.driver.find_element_by_css_selector(css_selector)
        except NoSuchElementException as e:
            return None

    def get_elements_by_css(self, css_selector):
        try:
            return self.driver.find_elements_by_css_selector(css_selector)
        except NoSuchElementException as e:
            return None



    def get_element_from_list_by_text(self, locator: By, locator_value, text_to_search: str) -> WebElement:
        element_list = self.driver.find_elements(locator, locator_value)

        for element in element_list:

            if text_to_search == element.text:
                return element
        return None

    def get_element_from_list_by_text_by_class(self, class_text, text_to_search):
        return self.get_element_from_list_by_text(By.CLASS_NAME, class_text, text_to_search)

    def get_element_from_list_by_text_by_css(self, resource_xpath, text_to_search):
        return self.get_element_from_list_by_text(By.CSS_SELECTOR, resource_xpath, text_to_search)

    def scrol_to(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_button_clickable(self, by, element, limit_time):
        try:
            WebDriverWait(self.driver, limit_time).until(EC.element_to_be_clickable((by, element)))
        except NoSuchElementException as e:
            return None

    def wait_button_located(self, by, element, limit_time):
        try:
            WebDriverWait(self.driver, limit_time).until(EC.visibility_of_element_located((by, element)))
        except NoSuchElementException as e:
            return None

    def wait_button_invisibility(self, by, element, limit_time):
        try:
            WebDriverWait(self.driver, limit_time).until(EC.invisibility_of_element_located((by, element)))
        except NoSuchElementException as e:
            return None
