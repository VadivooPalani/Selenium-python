
import pytest
from SSqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut
from SSqatest.src.pages.MyAccountSignedIn import MyAccountSignedIn

from SSqatest.src.helpers.generic_helpers import generate_random_email_and_password
@pytest.mark.usefixtures("init_driver")
class TestRegisterNewUser:

    @pytest.mark.TC02
    def test_register_valid_new_user(self):

        my_account_signout =MyAccountSignedOut(self.driver)
        my_account_signin=MyAccountSignedIn(self.driver)

        rand_email_and_pass=generate_random_email_and_password()
        #go to my account
        my_account_signout.go_to_account_page()
        my_account_signout.register_email_input(rand_email_and_pass['email'])
        my_account_signout.register_pass_input("Abcnmkjre@123")
        my_account_signout.register_button()

        # verify user signedin
        my_account_signin.verify_if_user_signedin()