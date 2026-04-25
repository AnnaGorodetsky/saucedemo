from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    """Page object for checkout complete page."""

    COMPLETE_HEADER = "complete-header"

    def get_confirmation_message(self) -> str:
        """Return the thank you message text."""
        return self.get_text(self.COMPLETE_HEADER)