##
from typing import Union, Dict

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class MainPage:
    def __init__(self, email: str, password: str, page_url: str, xpath_dict: Dict):
        self.email = email
        self.password = password
        self.page_url = page_url
        self.xpath_dict = xpath_dict
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def _access_login_page(self):
        self.driver.maximize_window()
        self.driver.get(self.page_url)
        email_path = self.driver.find_element(By.XPATH, self.xpath_dict['EMAIL_XPATH'])
        password_path = self.driver.find_element(By.XPATH, self.xpath_dict['PASSWORD_XPATH'])
        email_path.send_keys(self.email)
        password_path.send_keys(self.password)

    @staticmethod
    def _click_button(wait: WebDriverWait, find_by: Union[WebElement, tuple[By, str]]) -> None:
        button = wait.until(ec.element_to_be_clickable(find_by))
        button.click()

    def get_to_main_page(self):
        self._access_login_page()
        self._click_button(wait=self.wait, find_by=(By.XPATH, self.xpath_dict['LOG_IN_BUTTON_XPATH']))
