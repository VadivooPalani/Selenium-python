
from selenium.webdriver.common.by import By

class CartLocator:

    PRODUCT_AVAILABLE_IN_CART_PAGE= (By.CSS_SELECTOR,'tr.cart_item td.product-name')

    COUPON_INPUT_FIELD =(By.ID,'coupon_code')

    APPLY_COUPON_BTN =(By.NAME,'apply_coupon')

    APPLY_COUPON_SUCCESS_MESSAGE=(By.CSS_SELECTOR,'div.woocommerce-message')

    PROCEED_TO_CHECKOUT_BTN =(By.CSS_SELECTOR,'a.checkout-button')

