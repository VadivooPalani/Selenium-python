
from SSqatest.src.pages.locator.CheckoutLocator import CheckoutLocator
from SSqatest.src.SeleniumExtended import SeleniumExtended
from SSqatest.src.helpers.generic_helpers import generate_random_email_and_password

class CheckoutPage(CheckoutLocator):

    def __init__(self,driver):
        self.driver=driver
        self.sl=SeleniumExtended(self.driver)

    def billing_input_first_name(self,first_name =None):
        first_name= first_name if first_name else 'AutomationFname'
        self.sl.wait_and_input_text(self.BILLING_FIRST_NAME,first_name)

    def billing_input_last_name(self,last_name =None):
        last_name= last_name if last_name else 'AutomationLname'
        self.sl.wait_and_input_text(self.BILLING_LAST_NAME,last_name)

    def billing_input_street_name(self, street_name=None):
        street_name = street_name if street_name else '123 car street'
        self.sl.wait_and_input_text(self.BILLING_STREET_NAME, street_name)

    def billing_input_city_name(self,city_name=None):
        city_name = city_name if city_name else 'California'
        self.sl.wait_and_input_text(self.BILLING_CITY_NAME, city_name)

    def billing_input_zip_code(self,zip_code=None):
        zip_code = zip_code if zip_code else '43213'
        self.sl.wait_and_input_text(self.BILLING_ZIP_CODE, zip_code)

    def billing_input_phone(self, phone=None):
        phone = phone if phone else '4567839'
        self.sl.wait_and_input_text(self.BILLING_PHONE, phone)

    def billing_input_email(self, email=None):
        email_address=generate_random_email_and_password()
        email=email if email else email_address['email']
        self.sl.wait_and_input_text(self.BILLING_EMAIL_ADDRESS, email)

    def fill_billing_details(self,first_name =None,last_name =None,street_name=None,city_name=None,zip_code=None,phone=None,email=None):
        self.billing_input_first_name(first_name)
        self.billing_input_last_name(last_name)
        self.billing_input_street_name(street_name)
        self.billing_input_city_name(city_name)
        self.billing_input_zip_code(zip_code)
        self.billing_input_phone(phone)
        self.billing_input_email(email)

    def click_proceed_to_checkout(self):
        self.sl.wait_and_click(self.PLACE_ORDER_BTN)







