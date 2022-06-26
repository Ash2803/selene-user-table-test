from selene.support.shared import browser
import pytest


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com'
    browser.open("/webtables")
    browser.config.browser_name = 'chrome'
    browser.config.hold_browser_open = True

