import unittest
import time
import requests
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Pages.home_page import HomePage
from Configs.Config import Config

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

class TestInputSubmission(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()
    @classmethod    
    def tearDown(cls):
        if cls.driver:
            cls.driver.close()
            cls.driver.quit()
    
    
    def test_tc_a01_basic_input_submission(self):
        home_page = HomePage(self.driver)
        result_page = home_page.submit_form(Config.TEST_STRING)
        self.assertTrue(result_page.is_result_page_displayed(), 
                      "Result page is not displayed after form submission")
        ui_length = result_page.get_length_value()
        ui_substring = result_page.get_substring_value()
        print(f"UI Length: {ui_length}")
        print(f"UI Substring: {ui_substring}")
        self.assertEqual(ui_length, Config.EXPECTED_LENGTH, 
                       f"Expected length {Config.EXPECTED_LENGTH}, but got {ui_length}")
        self.assertEqual(ui_substring, Config.EXPECTED_SUBSTRING, 
                       f"Expected substring '{Config.EXPECTED_SUBSTRING}', but got '{ui_substring}'")
        url = Config.API_ENDPOINT
        headers = {"Content-Type": "application/json"}
        payload = {"inptstr": Config.TEST_STRING}
        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            api_response = response.json()
            self.assertEqual(ui_length, api_response["Length"], 
                           f"UI length ({ui_length}) does not match API length ({api_response['Length']})")
            self.assertEqual(ui_substring, api_response["Substring"], 
                           f"UI substring ('{ui_substring}') does not match API substring ('{api_response['Substring']}')")
        except requests.exceptions.RequestException as e:
            self.fail(f"API request failed: {e}")

if __name__ == "__main__":
    unittest.main()