class TestSorting:
    """Tests for product sorting functionality."""

    def test_sort_by_price_low_to_high(self, logged_in_page):
        """Verify products are sorted by price in ascending order."""
        logged_in_page.select_sort_option("lohi")
        prices = logged_in_page.get_all_prices()

        assert prices == sorted(prices), \
            f"Prices are not sorted low to high: {prices}"