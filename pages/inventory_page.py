from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Page object for the inventory/products page."""

    SORT_DROPDOWN = "product-sort-container" # data-test="product-sort-container"
    ITEM_PRICE = "inventory-item-price" #data-test="inventory-item-price"

    def select_sort_option(self, value: str):
        """Select a sorting option from the dropdown."""
        self.page.locator(f"[data-test='{self.SORT_DROPDOWN}']").select_option(value)

    def get_all_prices(self) -> list[float]:
        """Extract all product prices as a list of floats."""
        price_elements = self.page.locator(f"[data-test='{self.ITEM_PRICE}']").all()
        prices = []
        for element in price_elements:
            text = element.text_content()       # e.g. "$29.99"
            price = float(text.replace("$", ""))  # e.g. 29.99
            prices.append(price)
        return prices