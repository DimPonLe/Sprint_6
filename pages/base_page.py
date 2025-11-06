from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def wait_for_element_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    def execute_js_scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_for_element_clickable(self, element, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(element))