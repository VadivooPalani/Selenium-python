from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException,StaleElementReferenceException
import pdb
import time

class SeleniumExtended:

    def __init__(self,driver):
        self.driver=driver
        self.default_timeout=10

    def wait_and_input_text(self,locator,input_text,timeout=None):
        timeout =timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(input_text)


    def wait_and_click(self,locator,timeout=None):
        timeout = timeout if timeout else self.default_timeout
        try:
            WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
            ).click()
        except StaleElementReferenceException:
            time.sleep(2)
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            ).click()

    def wait_and_check_text(self,locator,text,timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator,text)
        )


    def wait_and_view_element(self,locator,timeout=None):

        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))


    def wait_and_find_all_matching_element(self,locator,timeout=None,err=None):
        timeout = timeout if timeout else self.default_timeout
        err = err if err else f'Unable to find any element located by locator {locator}'
        try:

            elements=WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator))

        except TimeoutException:
            raise TimeoutException(err)

        return elements

    def wait_and_get_text(self,locator,timeout=None):
        timeout = timeout if timeout else self.default_timeout
        element=WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))
        return element.text

    