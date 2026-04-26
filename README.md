# Sauce Demo — QA Automation Test Suite

Automated test suite for [Sauce Demo](https://www.saucedemo.com) using Playwright (Python) with Page Object Model architecture.

## Setup

```bash
git clone https://github.com/AnnaGorodetsky/saucedemo.git
cd saucedemo
python -m venv .venv
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # macOS/Linux
pip install -r requirements.txt
python -m playwright install chromium
```

## Running Tests

```bash
pytest -v                       # headless (default)
pytest -v --headed              # headed — see the browser
pytest tests/test_login.py -v   # run specific test file
```

## Report

```bash
pytest -v                       # generates report.html
start report.html               # open in browser (Windows)
```

Screenshots and traces are captured automatically on failure.

## Project Structure
├── config/settings.py              # Credentials, test data
├── pages/
│   ├── base_page.py                # Common actions (click, fill, get_text)
│   ├── login_page.py               # Login page object
│   ├── inventory_page.py           # Sorting, add to cart
│   ├── cart_page.py                # Cart verification
│   ├── checkout_step_one_page.py   # Checkout form
│   ├── checkout_step_two_page.py   # Checkout overview
│   └── checkout_complete_page.py   # Order confirmation
├── tests/
│   ├── conftest.py                 # Shared fixtures
│   ├── test_login.py               # Login (positive & negative)
│   ├── test_sorting.py             # Price sorting validation
│   └── test_e2e_purchase.py        # Full purchase flow
└── pytest.ini                      # Pytest & browser config

## Design Decisions

- **POM architecture** — each page is a class with its own locators and methods. Tests read like user stories, locator changes stay in one file.
- **BasePage inheritance** — common actions (click, fill, navigate) live in one base class, eliminating duplication.
- **`data-test` selectors** — more stable than CSS/IDs, exist solely for testing.
- **Fixtures** — login setup lives in `conftest.py`, so tests stay focused on their own scenario.
- **Centralized config** — credentials and test data in `config/settings.py`, never hard-coded in tests.
- **Dynamic cart logic** — the E2E test finds the two most expensive products programmatically, not by hard-coded names.

## Assumptions

- Sauce Demo is available at `https://www.saucedemo.com`
- Product prices are displayed in `$XX.XX` format
- `data-test` attributes remain consistent