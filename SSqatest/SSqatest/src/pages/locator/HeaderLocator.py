from selenium.webdriver.common.by import By

class HeaderLocator:

    CART_RIGHT_HEADER= (By.CSS_SELECTOR,'a.cart-contents')

    CART_ITEM_LOCATOR=(By.CSS_SELECTOR,'a.cart-contents span.count')