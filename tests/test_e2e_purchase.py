from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.checkout_complete_page import CheckoutCompletePage
from config.settings import CHECKOUT_INFO


class TestE2EPurchase:
    """Tests for end-to-end purchase flow."""

    def test_purchase_two_most_expensive_items(self, logged_in_page):
        """Add two most expensive items, checkout, and verify completion."""
        # Add two most expensive products to cart
        added_names = logged_in_page.add_two_most_expensive_to_cart()
        assert len(added_names) == 2, "Should have added exactly 2 items"

        # Go to cart and verify items are present
        logged_in_page.go_to_cart()
        cart = CartPage(logged_in_page.page)
        cart_items = cart.get_cart_item_names()

        for name in added_names:
            assert name in cart_items, \
                f"'{name}' should be in cart but found: {cart_items}"

        # Proceed to checkout
        cart.click_checkout()

        # Fill in checkout information
        step_one = CheckoutStepOnePage(cart.page)
        step_one.fill_checkout_info(
            CHECKOUT_INFO["first_name"],
            CHECKOUT_INFO["last_name"],
            CHECKOUT_INFO["zip_code"]
        )
        step_one.click_continue()

        # Click Finish
        step_two = CheckoutStepTwoPage(step_one.page)
        step_two.click_finish()

        # Verify completion message
        complete = CheckoutCompletePage(step_two.page)
        message = complete.get_confirmation_message()

        assert message == "Thank you for your order!", \
            f"Expected 'Thank you for your order!' but got: '{message}'"