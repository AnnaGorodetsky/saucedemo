from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Page object for the inventory/products page."""

    SORT_DROPDOWN = "product-sort-container"
    ITEM_PRICE = "inventory-item-price"
    ITEM_NAME = "inventory-item-name"
    CART_LINK = "shopping-cart-link"

    def select_sort_option(self, value: str):
        """Select a sorting option from the dropdown."""
        self.page.locator(f"[data-test='{self.SORT_DROPDOWN}']").select_option(value)

    def get_all_prices(self) -> list[float]:
        """Extract all product prices as a list of floats."""
        price_elements = self.page.locator(f"[data-test='{self.ITEM_PRICE}']").all()
        prices = []
        for element in price_elements:
            text = element.text_content()
            price = float(text.replace("$", ""))
            prices.append(price)
        return prices

    def add_two_most_expensive_to_cart(self) -> list[str]:
        """Find the two most expensive products, add them to cart, return their names."""
        items = self.page.locator("[data-test='inventory-item']").all()

        # Build a list of (name, price, add-button) for each product
        products = []
        for item in items:
            name = item.locator(f"[data-test='{self.ITEM_NAME}']").text_content()
            price_text = item.locator(f"[data-test='{self.ITEM_PRICE}']").text_content()
            price = float(price_text.replace("$", ""))
            button = item.locator("button", has_text="Add to cart")
            products.append({"name": name, "price": price, "button": button})

        # Sort by price descending, take top 2
        products.sort(key=lambda p: p["price"], reverse=True)
        top_two = products[:2]

        for product in top_two:
            product["button"].click()

        return [p["name"] for p in top_two]

    def go_to_cart(self):
        """Click the shopping cart icon."""
        self.click(self.CART_LINK)
