from playwright.sync_api import Page, expect
from helper.enum import Month
from pages.base_demo_site_page import BaseDemoSitePage
from helper.date_helper import validate_date_format, parse_date

class DatePickerPage(BaseDemoSitePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.date_picker_disabled = self.page.locator("//*[@id='datepicker1']")
        self.date_picker_enabled = self.page.locator("//*[@id='datepicker2']")
        self.selected_date = self.page.locator("//a[class*='datepick-selected'")
        self.change_year = self.page.locator("//select[@title='Change the year']")
        self.change_month = self.page.locator("//select[@title='Change the month']")
        self.date_pick_popup = self.page.locator("//div[@class='datepick-popup']")
        self.date_pick = self.page.locator("//select[class='datepick-month-year']")
        self.year_selector = "select[title='Change the year']"

    def set_date_in_picker(self, date_str: str):
        validate_date_format(date_str)
        day, month, year = parse_date(date_str)

        self.click_on_element(self.date_picker_enabled)
        self.wait_for_element_to_be_visible(self.date_pick_popup)

        self.click_on_element(self.change_year)
        self.wait_for_element_to_be_visible(self.change_year)
        self.page.select_option("select[title='Change the year']", label=f"{year}")

        self.click_on_element(self.change_month)
        self.page.select_option("select[title='Change the month']", value=Month.get_name(month))

        self.page.click(f"//div[contains(@class, 'datepick-month')]//a[text()='{day}']")

    def get_date_value(self) -> str:
        return self.date_picker_enabled.input_value()
