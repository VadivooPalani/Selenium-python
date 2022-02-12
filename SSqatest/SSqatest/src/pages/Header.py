
from SSqatest.src.pages.locator.HeaderLocator import HeaderLocator
from SSqatest.src.SeleniumExtended import SeleniumExtended

class Header(HeaderLocator):

    def __init__(self,driver):
        self.driver=driver
        self.sl=SeleniumExtended(self.driver)

    def click_right_cart_section_header(self):
        self.sl.wait_and_click(self.CART_RIGHT_HEADER)

    def wait_until_cart_is_updated_with_item(self,count):
        if count==1:
            expected_result = str(count) + ' item'
        else:
            expected_result = str(count) + ' items'
        self.sl.wait_and_check_text(self.CART_ITEM_LOCATOR,expected_result)

