from selenium import webdriver
from baidu.test_case.models.driver import browser
import unittest
import os

class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    def tearDown(self):
        self.driver.quit()




if __name__ == '__main__':
    a = MyTest()
    a.setUp()