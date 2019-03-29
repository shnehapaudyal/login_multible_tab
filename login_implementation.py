import time

import action as action
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from initiate import LoginRunner

class Initiate(LoginRunner):
    def test_login(self):
        time.sleep(3)
        hover_profile= self.driver.find_element_by_id("user")
        ActionChains(self.driver).move_to_element(hover_profile).perform();
        time.sleep(5)
        #assert hover_profile is "logout", "login_element should be 'login'"
        login_element = self.driver.find_element_by_id("logout")
        login_element.click()
        time.sleep(3)

        google_button = self.driver.find_element_by_class_name('googleButton')
        google_button.click()
        time.sleep(3)
        window_before = self.driver.window_handles[0]

        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

        self.driver.get('https://accounts.google.com/signin/oauth/identifier?client_id=366682898353-acmb37ig2gpqnve85r8l5j922e0k496n.apps.googleusercontent.com&as=WGIYSyDYkypTgilavRKIRw&destination=https%3A%2F%2Fhamropatro.firebaseapp.com&approval_state=!ChQ2TjNoS2xFVkVnRHRhRUtwS01ZZBIfVXh5MnA3WFUya0lkOEhuU1JuY2dubXAtSm96c214WQ%E2%88%99AJDr988AAAAAXJyntUXA08t6U3fTbnucRZFXxA5AiuAf&oauthgdpr=1&xsrfsig=ChkAeAh8T06_P0dG9Z-OimVt6kcUisFwTOEREg5hcHByb3ZhbF9zdGF0ZRILZGVzdGluYXRpb24SBXNvYWN1Eg9vYXV0aHJpc2t5c2NvcGU&flowName=GeneralOAuthFlow')
        time.sleep(5)
        google_email = self.driver.find_element_by_id("identifierId")
        google_email.send_keys("something@gmail.com")
        google_email.send_keys(Keys.RETURN)
        time.sleep(3)
        google_password = self.driver.find_element_by_name('password')
        google_password.send_keys("password")
        google_password.send_keys(Keys.RETURN)
        time.sleep(3)
        self.driver.switch_to.window(window_before)
        time.sleep(3)
        self.assertIn("Nepali Calendar 2075 | हाम्रो नेपाली पात्रो २०७५ | Hamro Nepali Patro", self.driver.title)
        #self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')


if __name__ == '__main__':
    unittest.main()

