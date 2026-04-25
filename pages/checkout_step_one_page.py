from pages.base_page import BasePage


class CheckoutStepOnePage(BasePage):
    """Page object for checkout step one — fill in information."""

    FIRST_NAME = "firstName"
    LAST_NAME = "lastName"
    POSTAL_CODE = "postalCode"
    CONTINUE_BUTTON = "continue"

    def fill_checkout_info(self, first_name: str, last_name: str, zip_code: str):
        """Fill in the checkout form."""
        self.fill_field(self.FIRST_NAME, first_name)
        self.fill_field(self.LAST_NAME, last_name)
        self.fill_field(self.POSTAL_CODE, zip_code)

    def click_continue(self):
        """Click the Continue button."""
        self.click(self.CONTINUE_BUTTON)