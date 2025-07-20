import pytest
from venv import logger
from helper.config import URL
from helper.utils import log_message, LogLevel
from pages.home_page import HomePage
from pages.register_page import RegisterPage


@pytest.fixture()
def setup_playwright(playwright, request):
    is_headed = request.config.getoption("--headed", default=False)
    browser = playwright.chromium.launch(headless=not is_headed)
    page = browser.new_page()
    try:
        yield page
    finally:
        log_message(logger, "Closing browser", LogLevel.INFO)
        browser.close()

@pytest.fixture()
def setup_home_page(setup_playwright):
    home_page = HomePage(setup_playwright)
    home_page.navigate_to(URL)
    log_message(logger, f"Navigate to {URL}")
    yield home_page

@pytest.fixture()
def setup_all_pages(setup_playwright):
    home_page = HomePage(setup_playwright)
    register_page = RegisterPage(setup_playwright)
    yield home_page, register_page