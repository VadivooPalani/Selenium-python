
from SSqatest.src.helpers.config_helper import get_base_url
from SSqatest.src.SeleniumExtended import SeleniumExtended
from SSqatest.src.pages.locator.HomePageLocator import HomePageLocator

class HomePage(HomePageLocator):

    def __init__(self,driver):
        self.driver=driver
        self.sl=SeleniumExtended(self.driver)

    def go_to_home_page(self):
        home_url=get_base_url()
        self.driver.get(home_url)

    def click_first_add_to_cart(self):
        self.sl.wait_and_click(self.ADD_TO_CART_PRODUCT)

