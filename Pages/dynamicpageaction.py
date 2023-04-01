from Pages.basepage import BasePage
from Pages.locators import DynamicLocators
from selenium.webdriver.common.by import By



class DynamicPageAction(BasePage):
    def click_enable_button(self):
        # Ensure Enable button is loaded on page
        self.wait_for_element_to_be_loaded(By.XPATH, DynamicLocators.BUTTON_ENABLE)
        # Click Enable button
        self.driver.find_element(By.XPATH, DynamicLocators.BUTTON_ENABLE).click()

    def click_disable_button(self):
        # Ensure Disable button is loaded on page
        self.wait_for_element_to_be_loaded(By.XPATH, DynamicLocators.BUTTON_DISABLE)
        # Click Disable button
        self.driver.find_element(By.XPATH, DynamicLocators.BUTTON_DISABLE).click()

    def click_remove_button(self):
        # Ensure Remove button is loaded on page
        self.wait_for_element_to_be_loaded(By.XPATH, DynamicLocators.BUTTON_REMOVE)
        # Click Remove button
        self.driver.find_element(By.XPATH, DynamicLocators.BUTTON_REMOVE).click()

    def click_add_button(self):
        # Ensure Add button is loaded on page
        self.wait_for_element_to_be_loaded(By.XPATH, DynamicLocators.BUTTON_ADD)
        # Click Add button
        self.driver.find_element(By.XPATH, DynamicLocators.BUTTON_ADD).click()

    def click_checkbox(self):
        # Ensure checkbox is loaded on page
        self.wait_for_element_to_be_loaded(By.XPATH, DynamicLocators.CB_BOX)
        # Click checkbox
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH, DynamicLocators.CB_BOX))

    def get_checkbox_state(self):
        # Ensure checkbox is loaded on page
        self.wait_for_element_to_be_loaded(By.XPATH, DynamicLocators.CB_BOX)
        # Return checkbox checked state
        return self.driver.find_element(By.XPATH, DynamicLocators.CB_BOX).is_selected()

    def get_textbox_state(self):
        # Ensure textbox is loaded on page
        self.wait_for_element_to_be_loaded(By.XPATH, DynamicLocators.TEXTBOX_TEXT)
        # Return textbox enabled state
        return self.driver.find_element(By.XPATH, DynamicLocators.TEXTBOX_TEXT).is_enabled()

    def get_response_value(self):
        # Ensure response label is loaded on page
        self.wait_for_element_to_be_loaded(By.XPATH, DynamicLocators.LABEL_RESPONSE)
        # Return response value
        return self.get_text_from_element(By.XPATH, DynamicLocators.LABEL_RESPONSE).strip()

    def wait_for_enable_disable_loading_element_to_disappear(self):
        self.wait_for_element_to_disappear(By.XPATH, DynamicLocators.LOADING_ENABLE_DISABLE)

    def wait_for_remove_add_loading_element_to_disappear(self):
        self.wait_for_element_to_disappear(By.XPATH, DynamicLocators.LOADING_REMOVE_ADD)
