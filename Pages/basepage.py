from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_to_be_loaded(self, by, element):
        delay = 10
        WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((by, element)))

    def wait_for_element_to_disappear(self, by, element):
        delay = 10
        WebDriverWait(self.driver, delay).until(EC.invisibility_of_element((by, element)))

    def navigate(self, url):
        self.driver.get(url)

    def get_text_from_element(self, by, element):
        return self.driver.find_element(by, element).text.strip()

    def input_text(self, element, text):
        # Ensure element is loaded on page
        self.wait_for_element_to_be_loaded(By.XPATH, element)
        # Input text into element
        self.driver.find_element(By.XPATH, element).send_keys(text)
