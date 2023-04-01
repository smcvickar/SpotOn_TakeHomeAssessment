from Pages.basepage import BasePage
from Pages.locators import LogInLocators
from selenium.webdriver.common.by import By


class LoginPageAction(BasePage):
    def click_login_button(self):
        # Ensure Login button is loaded on page
        self.wait_for_element_to_be_loaded(By.XPATH, LogInLocators.BUTTON_LOGIN)
        # Click Login button
        self.driver.find_element(By.XPATH, LogInLocators.BUTTON_LOGIN).click()

    def click_logout_button(self):
        # Ensure Logout button is loaded on page
        self.wait_for_element_to_be_loaded(By.XPATH, LogInLocators.BUTTON_LOGOUT)
        # Click Logout button
        self.driver.find_element(By.XPATH, LogInLocators.BUTTON_LOGOUT).click()

    def input_text_username(self, text):
        self.input_text(LogInLocators.TEXTBOX_USERNAME, text)

    def input_text_password(self, text):
        self.input_text(LogInLocators.TEXTBOX_PASSWORD, text)

    def get_response_value(self):
        # Ensure response label is loaded on page
        self.wait_for_element_to_be_loaded(By.XPATH, LogInLocators.LABEL_RESPONSE)
        # Return response value
        return self.get_text_from_element(By.XPATH, LogInLocators.LABEL_RESPONSE)

    def get_username_value(self):
        # Ensure username textbox is loaded on page
        self.wait_for_element_to_be_loaded(By.XPATH, LogInLocators.TEXTBOX_USERNAME)
        # Return username textbox value
        return self.get_text_from_element(By.XPATH, LogInLocators.TEXTBOX_USERNAME)

    def get_password_value(self):
        # Ensure password textbox is loaded on page
        self.wait_for_element_to_be_loaded(By.XPATH, LogInLocators.TEXTBOX_PASSWORD)
        # Return password textbox value
        return self.get_text_from_element(By.XPATH, LogInLocators.TEXTBOX_PASSWORD)
