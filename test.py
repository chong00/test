import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from unittest import TestCase
from selenium.webdriver.edge.options import Options
import unittest

# common
home = "/home.html"
result = "/result.html"

class XSS(TestCase):
    def setUp(self):
        options = Options()
        options.headless = True
        options.add_argument('--disable-gpu')

        self.driver = webdriver.Edge(executable_path="/usr/bin/microsoft-edge-dev", options=options)
        self.driver.get(home)


    def test_normal_search(self):
  
        search = self.driver.find_element(By.ID, "searchinput")
        button = self.driver.find_element(By.ID, "submit")
        search.send_keys("normal test")
        button.click()
        time.sleep(3)
        self.assertEqual(result, self.driver.current_url)

    def test_XSS(self):
        search = self.driver.find_element(By.ID, "searchinput")
        button = self.driver.find_element(By.ID, "submit")
        search.send_keys("/><script>alert(1)</script>")
        button.click()
        time.sleep(3)
        self.assertEqual(home, self.driver.current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()