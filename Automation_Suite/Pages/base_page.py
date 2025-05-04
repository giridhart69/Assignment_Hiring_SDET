from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Configs.Config import Config

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT)
    
    def wait_for_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def wait_for_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def find_element(self, locator):
        self.wait_for_element(locator)
        return self.driver.find_element(*locator)
    
    def click_element(self, locator):
        element = self.wait_for_element(locator)
        element.click()
    
    def enter_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_element_text(self, locator):
        element = self.wait_for_visibility(locator)
        return element.text