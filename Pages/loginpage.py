from selenium.common.exceptions import *
from Pages.basepage import BasePage
from Pages.locators import LogInLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    url = "https://the-internet.herokuapp.com/login"
    ERROR_USERNAME = "Your username is invalid!"
    ERROR_PASSWORD = "Your password is invalid!"
    SUCCESS_MESSAGE = "You logged into a secure area!"
    LOGOUT_MESSAGE = "You logged out of the secure area!"
    PASSWORD_CORRECT = "SuperSecretPassword!"
    PASSWORD_INCORRECT = "WrongPassword"
    USERNAME_CORRECT = "tomsmith"
    USERNAME_INCORRECT = "seanmcvickar"

    def click_login_button(self):
        try:
            self.driver.find_element(By.XPATH, LogInLocators.BUTTON_LOGIN).click()
        except NoSuchElementException:
            print('\"Login\" button not found')
            raise

    def click_logout_button(self):
        try:
            self.driver.find_element(By.XPATH, LogInLocators.BUTTON_LOGOUT).click()
        except NoSuchElementException:
            print('\"Logout\" button not found')
            raise
