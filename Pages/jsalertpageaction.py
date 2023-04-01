from Pages.basepage import BasePage
from Pages.locators import JsLocators
from selenium.webdriver.common.by import By


class JsAlertPageAction(BasePage):
    def click_js_alert_button(self):
        # Ensure JS Alert button is loaded on page
        self.wait_for_element_to_be_loaded(By.XPATH, JsLocators.BUTTON_ALERT)
        # Click JS Alert button
        self.driver.find_element(By.XPATH, JsLocators.BUTTON_ALERT).click()

    def click_js_confirm_button(self):
        # Ensure JS Confirm button is loaded on page
        self.wait_for_element_to_be_loaded(By.XPATH, JsLocators.BUTTON_CONFIRM)
        # Click JS Confirm button
        self.driver.find_element(By.XPATH, JsLocators.BUTTON_CONFIRM).click()

    def click_js_prompt_button(self):
        # Ensure JS Prompt button is loaded on page
        self.wait_for_element_to_be_loaded(By.XPATH, JsLocators.BUTTON_PROMPT)
        # Click JS Prompt button
        self.driver.find_element(By.XPATH, JsLocators.BUTTON_PROMPT).click()

    def get_response_value(self):
        # Ensure response label is loaded on page
        self.wait_for_element_to_be_loaded(By.XPATH, JsLocators.LABEL_RESPONSE)
        # Return response value
        return self.get_text_from_element(By.XPATH, JsLocators.LABEL_RESPONSE).strip()
