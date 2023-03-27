from selenium.common.exceptions import *
from Pages.basepage import BasePage
from Pages.locators import DynamicLocators
from selenium.webdriver.common.by import By


class DynamicPage(BasePage):
    url = "https://the-internet.herokuapp.com/dynamic_controls"
    MESSAGE_BACK = "It's back!"
    MESSAGE_CHECKBOX = "A checkbox"
    MESSAGE_DISABLED = "It's disabled!"
    MESSAGE_ENABLED = "It's enabled!"
    MESSAGE_GONE = "It's gone!"
    MESSAGE_TESTMESSAGE = "Test prompt text!"

    def click_enable_button(self):
        try:
            self.driver.find_element(By.XPATH, DynamicLocators.BUTTON_ENABLE).click()
        except NoSuchElementException:
            print("\"Enable\" button not found")
            raise

    def click_disable_button(self):
        try:
            self.driver.find_element(By.XPATH, DynamicLocators.BUTTON_DISABLE).click()
        except NoSuchElementException:
            print("\"Disable\" button not found")
            raise

    def click_remove_button(self):
        try:
            self.driver.find_element(By.XPATH, DynamicLocators.BUTTON_REMOVE).click()
        except NoSuchElementException:
            print("\"Remove\" button not found")
            raise

    def click_add_button(self):
        try:
            self.driver.find_element(By.XPATH, DynamicLocators.BUTTON_ADD).click()
        except NoSuchElementException:
            print("\"Add\" button not found")
            raise

    def get_checkbox_state(self):
        try:
            return self.driver.find_element(By.XPATH, DynamicLocators.CB_BOX).is_selected()
        except NoSuchElementException:
            print("Checkbox not found")

    def click_checkbox(self):
        try:
            self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH, DynamicLocators.CB_BOX))
        except NoSuchElementException:
            print("Checkbox not found")
