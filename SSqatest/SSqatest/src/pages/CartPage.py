
from SSqatest.src.SeleniumExtended import SeleniumExtended
from SSqatest.src.pages.locator.CartLocator import CartLocator

class CartPage(CartLocator):

    def __init__(self,driver):
        self.driver=driver
        self.sl = SeleniumExtended(self.driver)


    #fetch all product from cart page
    def product_available_in_cart_page(self):
        product_available=self.sl.wait_and_find_all_matching_element(self.PRODUCT_AVAILABLE_IN_CART_PAGE)

        product_names=[i.text for i in product_available]
        return product_names

    # Enter the input for appl coupon
    def input_apply_coupon(self,coupon):
        self.sl.wait_and_input_text(self.COUPON_INPUT_FIELD,coupon)

    def click_apply_coupon_btn(self):
        self.sl.wait_and_click(self.APPLY_COUPON_BTN)

    def success_message_on_coupon_applied(self):
        return self.sl.wait_and_get_text(self.APPLY_COUPON_SUCCESS_MESSAGE)

    def apply_coupon(self,coupon):
        self.input_apply_coupon(coupon)
        self.click_apply_coupon_btn()
        text=self.success_message_on_coupon_applied()
        assert text == 'Coupon code applied successfully.', 'The coupon is not valid one!!!'

    # click checkout button
    def click_proceed_to_checkout(self):
        self.sl.wait_and_click(self.PROCEED_TO_CHECKOUT_BTN)

