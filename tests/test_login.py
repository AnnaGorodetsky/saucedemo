from config.settings import STANDARD_USER, LOCKED_OUT_USER, PASSWORD


class TestLogin:
    """Tests for login functionality."""

    def test_successful_login(self, login_page):
        """Verify standard_user can log in and reaches inventory page."""
        login_page.navigate_to_login()
        login_page.login(STANDARD_USER, PASSWORD)

        assert "/inventory.html" in login_page.get_current_url(), \
            "User should be redirected to inventory page after login"

    def test_locked_out_user(self, login_page):
        """Verify locked_out_user sees the correct error message."""
        login_page.navigate_to_login()
        login_page.login(LOCKED_OUT_USER, PASSWORD)

        expected_error = "Epic sadface: Sorry, this user has been locked out."
        actual_error = login_page.get_error_message()

        assert actual_error == expected_error, \
            f"Expected error: '{expected_error}', but got: '{actual_error}'"