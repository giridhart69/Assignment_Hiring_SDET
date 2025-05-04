from selenium.webdriver.common.by import By
from Pages.base_page import BasePage

class ResultPage(BasePage):
    RESULT_HEADING = (By.XPATH, "//h1[text()='Result']")
    SUBSTRING_TEXT = (By.XPATH, "//p[contains(text(),'substring without')]")
    LENGTH_VALUE = (By.XPATH, "//h1/parent::div//p[1]/strong")
    SUBSTRING_VALUE = (By.XPATH, "//h1/parent::div//p[2]/strong")
    
    def is_result_page_displayed(self):
        try:
            self.wait_for_visibility(self.RESULT_HEADING)
            self.wait_for_visibility(self.SUBSTRING_TEXT)
            return True
        except:
            return False
    
    def get_length_value(self):
        length_element = self.find_element(self.LENGTH_VALUE)
        try:
            return int(length_element.text)
        except ValueError:
            return None
    
    def get_substring_value(self):
        substring_element = self.find_element(self.SUBSTRING_VALUE)
        return substring_element.text