from selenium.common.exceptions import *
from Pages.basepage import BasePage
from Pages.locators import LatLongLocators
from selenium.webdriver.common.by import By


class LatLongPage(BasePage):
    url = "https://the-internet.herokuapp.com/geolocation"

    def click_button(self):
        try:
            self.driver.find_element(By.XPATH, LatLongLocators.BUTTON_WHERE).click()
        except NoSuchElementException:
            print('\"Where am I?\" button not found')
            raise
