from selenium.webdriver.common.by import By

class MyAccountSignedOutLocator:

    LOGIN_USER_NAME = (By.ID,'username')

    LOGIN_PASSWORD =(By.ID,'password')

    LOGIN_BUTTON = (By.CSS_SELECTOR,"button[name='login']")

    ERROR_EXCEPTION = (By.CSS_SELECTOR ,"ul.woocommerce-error")

    REGISTER_EMAIL =(By.ID,"reg_email")

    REGISTER_PASS =(By.ID,'reg_password')

    REGISTER_BUTTON =(By.CSS_SELECTOR,"button[name='register']")

