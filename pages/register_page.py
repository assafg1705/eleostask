from playwright.sync_api import Page

from pages.base_demo_site_page import BaseDemoSitePage

class RegisterPage(BaseDemoSitePage):
    def __init__(self, page: Page):
        super().__init__(page)
