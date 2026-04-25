from pages.base_page import BasePage


class CheckoutStepTwoPage(BasePage):
    """Page object for checkout step two — overview and finish."""

    FINISH_BUTTON = "finish"

    def click_finish(self):
        """Click the Finish button."""
        self.click(self.FINISH_BUTTON)