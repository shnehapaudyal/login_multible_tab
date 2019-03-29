import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class LoginRunner(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

        self.driver.get("http://www.hamropatro.com")
        self.assertIn("Nepali Calendar 2075 | हाम्रो नेपाली पात्रो २०७५ | Hamro Nepali Patro", self.driver.title)

    def tearDown(self):
        self.driver.close()

