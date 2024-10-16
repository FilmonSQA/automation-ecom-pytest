
import pytest
from demostore_automation.src.pages.MyAccountSignedOutPage import MyAccountSignedOutPage

pytestmark = [pytest.mark.fe, pytest.mark.regression, pytest.mark.smoke, pytest.mark.my_account]

@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:
    """
    A set of negative tests to verify the login functionality with non-existing users.
    """

    @pytest.mark.estcf13
    def test_login_none_existing_user(self):
        """
        Test to verify the login functionality with a non-existing user.
        """
        
        print("Testing None Existing User Login")
        my_acct_page = MyAccountSignedOutPage(self.driver)
        my_acct_page.go_to_my_account()
        my_acct_page.input_login_username("abcdef@supersqa.com")
        my_acct_page.input_login_password("abcdefg")
        my_acct_page.click_login_button()

        expected_err = "Unknown email address. Check again or try your username."

        # Waiting for the error to appear
        my_acct_page.wait_until_error_is_displayed(expected_err)

        # Adding an assertion to verify the error message is displayed correctly
        assert my_acct_page.get_error_message() == expected_err, "Error message does not match expected text."

        breakpoint()