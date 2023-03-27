from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class BasePage(object):
    url = ""

    def __init__(self, driver):
        self.driver = driver

    def is_element_loaded(self, by, element):
        delay = 10
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((by, element)))
        except TimeoutError:
            print("Page not loaded")

    def navigate(self):
        self.driver.get(self.url)

    def get_text_from_element(self, by, element):
        return self.driver.find_element(by, element).text

    def input_text(self, by, element, text):
        try:
            self.driver.find_element(by, element).send_keys(text)
        except NoSuchElementException:
            print("Element not found")
            raise
