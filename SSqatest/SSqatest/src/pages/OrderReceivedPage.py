from SSqatest.src.SeleniumExtended import SeleniumExtended
from SSqatest.src.pages.locator.OrderReceivedPageLocator import OrderReceivedPageLocator

class OrderReceivedPage(OrderReceivedPageLocator):

    def __init__(self,driver):
        self.driver=driver
        self.sl=SeleniumExtended(self.driver)

    def check_order_received_message(self):
        self.sl.wait_and_check_text(self.ORDER_RECEIVED_MSG,'Order received')


    def get_order_number(self):
        return self.sl.wait_and_get_text(self.ORDER_NUMBER)

