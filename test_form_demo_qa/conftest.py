from selene import browser
from selenium import webdriver
import pytest

@pytest.fixture(scope='function')
def open_browser():
    browser.config.base_url='https://demoqa.com'
    driver_options = webdriver.ChromeOptions()
    # driver_options.add_argument('--headless=new')
    browser.config.driver_options = driver_options

    yield

    browser.quit()
