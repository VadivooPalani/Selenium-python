
import pytest
from SSqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut


@pytest.mark.usefixtures("init_driver")
class TestLoginNegative():

   @pytest.mark.TC01
   def test_login_none_exising(self):
       my_account_page_obj = MyAccountSignedOut(self.driver)

       # go to my account fn
       my_account_page_obj.go_to_account_page()

       #login field details fn
       my_account_page_obj.login_input('aswedrftg')

       #login password details fn
       my_account_page_obj.password_input('qwert')

       #Button click-Login
       my_account_page_obj.signin_button()

       #Error Message
       expected_err_msg = "ERROR: Invalid username. Loost your password?"
       my_account_page_obj.error_message(expected_err_msg)

       # verify user is signedin or not





