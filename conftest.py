import pytest
import urls
import allure
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@pytest.fixture()
def browser():
    firefox_options = Options()
    firefox_options.set_preference("browser.privatebrowsing.autostart", True)
    driver = webdriver.Firefox(options=firefox_options)
    driver.get(urls.HOME_URL)
    driver.fullscreen_window()
    yield driver
    driver.quit()