import pytest
from SSqatest.src.pages.HomePage import HomePage
from SSqatest.src.pages.Header import Header
from SSqatest.src.pages.CartPage import CartPage
from SSqatest.src.pages.CheckoutPage import CheckoutPage
from SSqatest.src.pages.OrderReceivedPage import OrderReceivedPage
from SSqatest.src.configs.generic_configs import GenericConfigs

@pytest.mark.usefixtures('init_driver')
class TestEndToEndCheckoutGuestUser:

    @pytest.mark.TC03
    def test_end_to_end_checkout_guest_user(self):

        self.home_obj=HomePage(self.driver)
        self.header_obj=Header(self.driver)
        self.cart_obj =CartPage(self.driver)
        self.checkout_obj=CheckoutPage(self.driver)
        self.orderreceived_obj=OrderReceivedPage(self.driver)
        #Go to home page
        self.home_obj.go_to_home_page()
        #Add product to the cart
        self.home_obj.click_first_add_to_cart()

        # Confirm the cart is updated with the item before going to cart page
        self.header_obj.wait_until_cart_is_updated_with_item(1)

        #Move to cart page
        self.header_obj.click_right_cart_section_header()
        #Get all product name available in th cart page

        products =self.cart_obj.product_available_in_cart_page()
        assert len(products) ==1 , f'Cart should be with 1 item but we are having' +{len(products)}

        #Apply coupon
        self.cart_obj.apply_coupon(GenericConfigs.FREE_COUPON)

        #Proceed to checkout
        self.cart_obj.click_proceed_to_checkout()

        #Fill the form before place order

        self.checkout_obj.fill_billing_details()
        # place order
        self.checkout_obj.click_proceed_to_checkout()

        # check the order confirmation
        self.orderreceived_obj.check_order_received_message()

        #verify the order stores in DB(via DB or API)
        order_num=self.orderreceived_obj.get_order_number()
        print('----------------')
        print(order_num)


