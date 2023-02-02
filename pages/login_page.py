from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver
from resources.webelements import login_elements


class LoginPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_input_account(self):
        return self.wait_until_element_is_clickable(By.XPATH, login_elements.INPUT_ACCOUNT)

    def enter_account(self, account):
        self.get_input_account().click()
        self.get_input_account().clear()
        self.get_input_account().send_keys(account);

    def get_input_user(self):
        return self.wait_until_element_is_clickable(By.XPATH, login_elements.INPUT_USER)

    def enter_user(self, user):
        self.get_input_user().click()
        self.get_input_user().clear()
        self.get_input_user().send_keys(user);

    def get_input_password(self):
        return self.wait_until_element_is_clickable(By.XPATH, login_elements.INPUT_PASSWORD)

    def enter_password(self, password):
        self.get_input_password().click()
        self.get_input_password().clear()
        self.get_input_password().send_keys(password);

    def get_btn_submit(self):
        return self.driver.find_element(By.XPATH, login_elements.BUTTON_SUBMIT)

    def click_submit(self):
        self.get_btn_submit().click()

    def login(self, account, username, password):
        self.enter_account(account)
        self.enter_user(username)
        self.enter_password(password)
        self.click_submit()