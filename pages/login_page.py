from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page object for the Sauce Demo login page."""

    # Locators (data-test attributes)
    USERNAME_FIELD = "username"
    PASSWORD_FIELD = "password"
    LOGIN_BUTTON = "login-button"
    ERROR_MESSAGE = "error"

    def navigate_to_login(self):
        """Open the login page."""
        self.navigate("/")

    def login(self, username: str, password: str):
        """Perform login with given credentials."""
        self.fill_field(self.USERNAME_FIELD, username)
        self.fill_field(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        """Return the login error message text."""
        return self.get_text(self.ERROR_MESSAGE)