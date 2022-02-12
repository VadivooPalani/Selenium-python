import pytest

from SSqatest.src.pages.locator.MyAccountSignedOutLocator import MyAccountSignedOutLocator

from SSqatest.src.SeleniumExtended import SeleniumExtended
from SSqatest.src.helpers.config_helper import get_base_url
import logging as logger

class MyAccountSignedOut(MyAccountSignedOutLocator):

    endpoint ='/my-account/'


    def __init__(self,driver):
        self.driver=driver
        self.sl=SeleniumExtended(self.driver)

    def go_to_account_page(self):
        base_url=get_base_url()
        print(f'Base URL :{base_url}')
        my_account_url=base_url+ MyAccountSignedOut.endpoint
        logger.info(f'Going to {my_account_url}')
        self.driver.get(my_account_url)

    def login_input(self,username):
        self.sl.wait_and_input_text(self.LOGIN_USER_NAME,username)

    def password_input(self,password):
        self.sl.wait_and_input_text(self.LOGIN_PASSWORD, password)

    def signin_button(self):
        self.sl.wait_and_click(self.LOGIN_BUTTON)

    def error_message(self,expected_err_msg):
        self.sl.wait_and_check_text(self.ERROR_EXCEPTION,expected_err_msg)

    def register_email_input(self,email):
        self.sl.wait_and_input_text(self.REGISTER_EMAIL,email)

    def register_pass_input(self,password):
        self.sl.wait_and_input_text(self.REGISTER_PASS,password)

    def register_button(self):
        self.sl.wait_and_click(self.REGISTER_BUTTON)