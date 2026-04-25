import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.settings import STANDARD_USER, PASSWORD


@pytest.fixture
def login_page(page):
    """Provide a LoginPage instance."""
    return LoginPage(page)


@pytest.fixture
def logged_in_page(page):
    """Log in and return an InventoryPage instance."""
    login = LoginPage(page)
    login.navigate_to_login()
    login.login(STANDARD_USER, PASSWORD)
    return InventoryPage(page)