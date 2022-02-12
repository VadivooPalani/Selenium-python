from selenium.webdriver.common.by import By

class OrderReceivedPageLocator:

    ORDER_RECEIVED_MSG =(By.CSS_SELECTOR,'header.entry-header h1.entry-title')

    ORDER_NUMBER =(By.CSS_SELECTOR,'li.order strong')