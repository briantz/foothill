# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest

class SauceLabsHeaders(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://deanza.edu/"
        self.verificationErrors = []
    
    def test_sauce_labs_headers(self):
        driver = self.driver

        driver.get(self.base_url)
        driver.find_element_by_link_text("About De Anza").click()
        try: self.assertRegexpMatches(driver.title, r"About")
        except AssertionError as e: self.verificationErrors.append(str(e))

        driver.get(self.base_url)
        driver.find_element_by_link_text("Academic Calendar").click()
        try: self.assertRegexpMatches(driver.title, r"Academic")
        except AssertionError as e: self.verificationErrors.append(str(e))
    
        driver.get(self.base_url)
        driver.find_element_by_link_text("Academic Probation").click()
        try: self.assertRegexpMatches(driver.title, r"Probation")
        except AssertionError as e: self.verificationErrors.append(str(e))

        driver.get(self.base_url)
        driver.find_element_by_link_text("Chemistry Department").click()
        try: self.assertRegexpMatches(driver.title, r"Chemistry")
        except AssertionError as e: self.verificationErrors.append(str(e))

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
