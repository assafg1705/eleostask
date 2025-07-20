import logging
from playwright.sync_api import Page, Locator
from helper.utils import log_message, LogLevel, take_screenshot

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = logging.getLogger(self.__class__.__name__)

    def safe_execute(self, action, action_name: str, *args, **kwargs):
        try:
            log_message(self.logger, f"Execution Action {action_name} with arguments {args}, kwargs={kwargs}", LogLevel.INFO)
            action(*args)
        except Exception as e:
            log_message(self.logger, f"Execution failed {action_name} with arguments {args}, kwargs={kwargs}", LogLevel.INFO)
            take_screenshot(self.page, action_name)
            raise

    def click_on_element(self, locator: Locator):
        self.safe_execute(locator.click, "click_element")

    def type_text(self, locator: Locator, text: str):
        self.safe_execute(locator.fill, "type_text", text)

    def get_text(self, locator: Locator) -> str:
        return self.safe_execute(locator.input_value, "get text")

    def navigate_to(self, url: str):
        self.safe_execute(self.page.goto, "navigate_to", url)

    def hover_on_element(self, locator: Locator):
        self.safe_execute(locator.hover, "hover on element")

    def wait_for_element_to_be_visible(self, locator: Locator, element_state: str = "visible", wait_timeout: int = 5000):
        self.safe_execute(locator.wait_for, "wait for", state=element_state, timeout=wait_timeout)



