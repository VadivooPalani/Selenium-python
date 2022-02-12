from SSqatest.src.SeleniumExtended import SeleniumExtended
from SSqatest.src.pages.locator.MyAccountSignedInLocator import MyAccountSignedInLocator

class MyAccountSignedIn(MyAccountSignedInLocator):

    def __init__(self,driver):
        self.driver=driver
        self.sl_obj=SeleniumExtended(self.driver)

    def verify_if_user_signedin(self):
        self.sl_obj.wait_and_view_element(self.LEFT_NAV_LOGOUT)


