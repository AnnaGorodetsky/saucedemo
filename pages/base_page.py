from playwright.sync_api import Page


class BasePage:
    """Base class for all page objects. Contains common actions."""

    def __init__(self, page: Page):
        self.page = page

    def navigate(self, path: str = "/"):
        """Navigate to a path relative to base URL."""
        self.page.goto(path)

    def get_title(self) -> str:
        """Return the page title."""
        return self.page.title()

    def get_current_url(self) -> str:
        """Return the current URL."""
        return self.page.url

    def click(self, locator: str):
        """Click an element by data-test attribute."""
        self.page.locator(f"[data-test='{locator}']").click()

    def fill_field(self, locator: str, value: str):
        """Fill a text field by data-test attribute."""
        self.page.locator(f"[data-test='{locator}']").fill(value)

    def get_text(self, locator: str) -> str:
        """Get text content of an element by data-test attribute."""
        return self.page.locator(f"[data-test='{locator}']").text_content()

    def is_visible(self, locator: str) -> bool:
        """Check if an element is visible by data-test attribute."""
        return self.page.locator(f"[data-test='{locator}']").is_visible()

