from Pages.basepage import BasePage
from Pages.locators import LatLongLocators
from selenium.webdriver.common.by import By


class LatLongPageAction(BasePage):
    def click_where_button(self):
        # Ensure Enable button is loaded on page
        self.wait_for_element_to_be_loaded(By.XPATH, LatLongLocators.BUTTON_WHERE)
        # Click Where button
        self.driver.find_element(By.XPATH, LatLongLocators.BUTTON_WHERE).click()

    def get_latitude_value(self):
        # Ensure Latitude is loaded on page
        self.wait_for_element_to_be_loaded(By.XPATH, LatLongLocators.LABEL_LAT)
        # Return Latitude value
        return float(self.get_text_from_element(By.XPATH, LatLongLocators.LABEL_LAT))

    def get_longitude_value(self):
        # Ensure Longitude is loaded on page
        self.wait_for_element_to_be_loaded(By.XPATH, LatLongLocators.LABEL_LONG)
        # Return Longitude value
        return float(self.get_text_from_element(By.XPATH, LatLongLocators.LABEL_LONG))
