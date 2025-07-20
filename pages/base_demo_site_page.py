from pages.base_page import BasePage
from playwright.sync_api import Page


class BaseDemoSitePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.automation_demo_site_header = self.page.locator("//h1[text='Automation Demo Site ']")
        self.home_menu_btn = self.page.locator("//a[@href='Index.html']")
        self.register_menu_btn = self.page.locator("//a[@href='Register.html']")
        self.webtable_menu_btn = self.page.locator("//a[@href='WebTable.html']")
        self.switchto_menu_btn = self.page.locator("//a[@href='SwitchTo.html']")
        self.widgets_menu_btn = self.page.locator("//a[@href='Widgets.html']")
        self.interactions_menu_btn = self.page.locator("//a[@href='Interactions.html']")
        self.datepicker_menu_btn = self.page.locator("//a[@href='Datepicker.html']")

    def open_widgets_datepicker(self):
        from pages.date_picker_page import DatePickerPage
        self.hover_on_element(self.widgets_menu_btn)
        self.click_on_element(self.datepicker_menu_btn)
        return DatePickerPage(self.page)
