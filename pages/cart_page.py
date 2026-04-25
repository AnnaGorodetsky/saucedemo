from pages.base_page import BasePage


class CartPage(BasePage):
    """Page object for the shopping cart page."""

    ITEM_NAME = "inventory-item-name"
    CHECKOUT_BUTTON = "checkout"

    def get_cart_item_names(self) -> list[str]:
        """Return names of all items in the cart."""
        elements = self.page.locator(f"[data-test='{self.ITEM_NAME}']").all()
        return [el.text_content() for el in elements]

    def click_checkout(self):
        """Click the Checkout button."""
        self.click(self.CHECKOUT_BUTTON)