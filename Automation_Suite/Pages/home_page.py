from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from Configs.Config import Config

class HomePage(BasePage):
    INPUT_TEXT_FIELD = (By.NAME, "input_text")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Config.BASE_URL)
        self.driver.maximize_window()
    
    def enter_input_string(self, input_string):
        self.enter_text(self.INPUT_TEXT_FIELD, input_string)
        return self
    
    def click_submit(self):
        self.click_element(self.SUBMIT_BUTTON)
        from Pages.result_page import ResultPage
        return ResultPage(self.driver)
    
    def submit_form(self, input_string=Config.TEST_STRING):
        self.enter_input_string(input_string)
        return self.click_submit()