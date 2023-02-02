import pytest
import time
import softest
from ddt import file_data, ddt
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import alert_is_present, url_contains, visibility_of, \
    element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait

from pages.login_page import LoginPage
from resources.webelements import login_elements, main_menu
from utilities.util import Utils
import resources.webelements.account_admin_elements as acc_admin


@pytest.mark.usefixtures("setup")
@ddt
class TestLoginPage(softest.TestCase):
    log = Utils.custom_logger()

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LoginPage(self.driver)

    # def test_element_case(self):
    #     self.lp.get_input_account().click()
    #     self.lp.get_input_user().click()
    #     self.lp.get_input_password().click()
    #     self.lp.get_btn_submit().click()
    #
    #     self.soft_assert(self.assertEqual, self.lp.check_exists_by_xpath(login_elements.ACCOUNT_REQUIRED), True)
    #     self.soft_assert(self.assertEqual, self.lp.check_exists_by_xpath(login_elements.USER_REQUIRED), True)
    #     self.soft_assert(self.assertEqual, self.lp.check_exists_by_xpath(login_elements.PASSWORD_REQUIRED), True)
    #
    #     self.lp.enter_password("password")
    #     self.lp.enter_account("account")
    #     self.lp.enter_user("username")
    #
    #     self.soft_assert(self.assertEqual, self.lp.check_exists_by_xpath(login_elements.ACCOUNT_REQUIRED), False)
    #     self.soft_assert(self.assertEqual, self.lp.check_exists_by_xpath(login_elements.USER_REQUIRED), False)
    #     self.soft_assert(self.assertEqual, self.lp.check_exists_by_xpath(login_elements.PASSWORD_REQUIRED), False)
    #
    #     self.lp.enter_password("less8")
    #     self.soft_assert(self.assertEqual, self.lp.check_exists_by_xpath(login_elements.SHORT_PASSWORD_WARNING), True)
    #
    #     self.assert_all()
    #
    @file_data("../resources/testdata/login/login_fail.json")
    def test_login_fail(self, account, username, password):
        self.lp.login(account, username, password)
        WebDriverWait(self.driver, timeout=10).until(alert_is_present())
        self.soft_assert(self.assertEqual, self.driver.switch_to.alert.text, "Bad credential")
        self.driver.switch_to.alert.accept()
        self.assert_all()

    @file_data("../resources/testdata/login/login_success.json")
    def test_login_success(self, account, username, password):
        self.lp.login(account, username, password)
        WebDriverWait(self.driver, timeout=10).until(url_contains("performance"))
        self.soft_assert(self.assertEqual, self.lp.check_exists_by_css(main_menu.ACCOUNT_IMG), True)
        self.assert_all()
