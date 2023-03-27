from selenium.common.exceptions import *
from Pages.basepage import BasePage
from Pages.locators import JsLocators
from selenium.webdriver.common.by import By


class JsAlertPage(BasePage):
    url = "https://the-internet.herokuapp.com/javascript_alerts"
    MESSAGE_JSALERT = "I am a JS Alert"
    MESSAGE_JSCONFIRM = "I am a JS Confirm"
    MESSAGE_JSPROMPT = "I am a JS prompt"
    MESSAGE_ALERT = "You successfully clicked an alert"
    MESSAGE_CONFIRM = "You clicked: Ok"
    MESSAGE_CANCEL = "You clicked: Cancel"
    MESSAGE_RESPONSE = "You entered: {inputvalue}"
    MESSAGE_TESTPROMPT = "Test prompt text!"

    def click_jsalert_button(self):
        try:
            self.driver.find_element(By.XPATH, JsLocators.BUTTON_ALERT).click()
        except NoSuchElementException:
            print('\"JS Alert\" button not found')
            raise

    def click_jsconfirm_button(self):
        try:
            self.driver.find_element(By.XPATH, JsLocators.BUTTON_CONFIRM).click()
        except NoSuchElementException:
            print('\"JS Confirm\" button not found')
            raise

    def click_jsprompt_button(self):
        try:
            self.driver.find_element(By.XPATH, JsLocators.BUTTON_PROMPT).click()
        except NoSuchElementException:
            print('\"JS Prompt\" button not found')
            raise
