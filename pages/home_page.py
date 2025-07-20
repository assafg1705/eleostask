from playwright.async_api import Page

from helper.utils import log_message, LogLevel, take_screenshot
from pages.base_page import BasePage
from pages.register_page import RegisterPage


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.email_id_field = self.page.locator("//*[@id='email']")
        self.sign_in_btn = self.page.locator("//*[@id='btn1']")
        self.skip_sign_in_btn = self.page.locator("//*[@id='btn2']")
        self.register_btn = self.page.locator("//*[@id='enterimg']")

    def perform_skip_sign_in(self):
        log_message(self.logger, f"Performing Skip Sign In", level=LogLevel.INFO)
        self.click_on_element(self.skip_sign_in_btn)

        if self.skip_sign_in_btn.is_visible():
            log_message(self.logger, "Log In with skip sign in failed", level=LogLevel.ERROR)
            take_screenshot(self.page, "Skip Sign In failed screenshot")
            return None
        return RegisterPage(self.page)
