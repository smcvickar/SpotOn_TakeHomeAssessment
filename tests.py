import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from Pages.loginpage import LoginPage
from Pages.jsalertpage import JsAlertPage
from Pages.dynamicpage import DynamicPage
from Pages.latlongpage import LatLongPage
from Pages.locators import *


# Question 1: Write a couple of tests you think would be necessary for the following form: https://the-internet.herokuapp.com/login
class LogInTests(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()

    def test_correctusername_incorrectpassword(self):
        # Create LogInPage object
        loginpage = LoginPage(self.driver)
        # Navigate to correct page
        loginpage.navigate()
        # Ensure username text box is visible
        loginpage.is_element_loaded(By.XPATH, LogInLocators.TEXTBOX_USERNAME)
        # Input correct username
        loginpage.input_text(By.XPATH, LogInLocators.TEXTBOX_USERNAME, loginpage.USERNAME_CORRECT)
        # Ensure password text box is visible
        loginpage.is_element_loaded(By.XPATH, LogInLocators.TEXTBOX_PASSWORD)
        # Input incorrect password
        loginpage.input_text(By.XPATH, LogInLocators.TEXTBOX_PASSWORD, loginpage.PASSWORD_INCORRECT)
        # Ensure login button is visible
        loginpage.is_element_loaded(By.XPATH, LogInLocators.BUTTON_LOGIN)
        # Click button to validate credentials
        loginpage.click_login_button()
        # Ensure response message is visible
        loginpage.is_element_loaded(By.XPATH, LogInLocators.LABEL_RESPONSE)
        # Validate response message
        self.assertIn(loginpage.ERROR_PASSWORD, loginpage.get_text_from_element(By.XPATH, LogInLocators.LABEL_RESPONSE))
        # Ensure username text box is visible
        loginpage.is_element_loaded(By.XPATH, LogInLocators.TEXTBOX_USERNAME)
        # Validate username text box is blank
        self.assertEqual(loginpage.get_text_from_element(By.XPATH, LogInLocators.TEXTBOX_USERNAME), "")
        # Ensure password text box is visible
        loginpage.is_element_loaded(By.XPATH, LogInLocators.TEXTBOX_PASSWORD)
        # Validate password text box is blank
        self.assertEqual(loginpage.get_text_from_element(By.XPATH, LogInLocators.TEXTBOX_PASSWORD), "")

    def test_incorrectusername_correctpassword(self):
        # Create LogInPage object
        loginpage = LoginPage(self.driver)
        # Navigate to correct page
        loginpage.navigate()
        # Ensure username text box is visible
        loginpage.is_element_loaded(By.XPATH, LogInLocators.TEXTBOX_USERNAME)
        # Input incorrect username
        loginpage.input_text(By.XPATH, LogInLocators.TEXTBOX_USERNAME, loginpage.USERNAME_INCORRECT)
        # Ensure password text box is visible
        loginpage.is_element_loaded(By.XPATH, LogInLocators.TEXTBOX_USERNAME)
        # Input correct password
        loginpage.input_text(By.XPATH, LogInLocators.TEXTBOX_PASSWORD, loginpage.PASSWORD_CORRECT)
        # Ensure login button is visible
        loginpage.is_element_loaded(By.XPATH, LogInLocators.BUTTON_LOGIN)
        # Click button to validate credentials
        loginpage.click_login_button()
        # Ensure response message is visible
        loginpage.is_element_loaded(By.XPATH, LogInLocators.LABEL_RESPONSE)
        # Validate response message
        self.assertIn(loginpage.ERROR_USERNAME, loginpage.get_text_from_element(By.XPATH, LogInLocators.LABEL_RESPONSE))
        # Ensure username text box is visible
        loginpage.is_element_loaded(By.XPATH, LogInLocators.TEXTBOX_USERNAME)
        # Validate username text box is blank
        self.assertEqual(loginpage.get_text_from_element(By.XPATH, LogInLocators.TEXTBOX_USERNAME), "")
        # Ensure password text box is visible
        loginpage.is_element_loaded(By.XPATH, LogInLocators.TEXTBOX_PASSWORD)
        # Validate password text box is blank
        self.assertEqual(loginpage.get_text_from_element(By.XPATH, LogInLocators.TEXTBOX_PASSWORD), "")

    def test_incorrectusername_incorrectpassword(self):
        # Create LogInPage object
        loginpage = LoginPage(self.driver)
        # Navigate to correct page
        loginpage.navigate()
        # Ensure username text box is visible
        loginpage.is_element_loaded(By.XPATH, LogInLocators.TEXTBOX_USERNAME)
        # Input incorrect username
        loginpage.input_text(By.XPATH, LogInLocators.TEXTBOX_USERNAME, loginpage.USERNAME_INCORRECT)
        # Ensure password text box is visible
        loginpage.is_element_loaded(By.XPATH, LogInLocators.TEXTBOX_PASSWORD)
        # Input incorrect password
        loginpage.input_text(By.XPATH, LogInLocators.TEXTBOX_PASSWORD, loginpage.PASSWORD_INCORRECT)
        # Ensure login button is visible
        loginpage.is_element_loaded(By.XPATH, LogInLocators.BUTTON_LOGIN)
        # Click button to validate credentials
        loginpage.click_login_button()
        # Ensure response message is visible
        loginpage.is_element_loaded(By.XPATH, LogInLocators.LABEL_RESPONSE)
        # Validate response message
        self.assertIn(loginpage.ERROR_USERNAME, loginpage.get_text_from_element(By.XPATH, LogInLocators.LABEL_RESPONSE))
        # Ensure username text box is visible
        loginpage.is_element_loaded(By.XPATH, LogInLocators.TEXTBOX_USERNAME)
        # Validate username text box is blank
        self.assertEqual(loginpage.get_text_from_element(By.XPATH, LogInLocators.TEXTBOX_USERNAME), "")
        # Ensure password text box is visible
        loginpage.is_element_loaded(By.XPATH, LogInLocators.TEXTBOX_PASSWORD)
        # Validate password text box is blank
        self.assertEqual(loginpage.get_text_from_element(By.XPATH, LogInLocators.TEXTBOX_PASSWORD), "")

    def test_correctusername_correctpassword(self):
        # Create LogInPage object
        loginpage = LoginPage(self.driver)
        # Navigate to correct page
        loginpage.navigate()
        # Ensure username text box is visible
        loginpage.is_element_loaded(By.XPATH, LogInLocators.TEXTBOX_USERNAME)
        # Input correct username
        loginpage.input_text(By.XPATH, LogInLocators.TEXTBOX_USERNAME, loginpage.USERNAME_CORRECT)
        # Ensure password text box is visible
        loginpage.is_element_loaded(By.XPATH, LogInLocators.TEXTBOX_PASSWORD)
        # Input correct password
        loginpage.input_text(By.XPATH, LogInLocators.TEXTBOX_PASSWORD, loginpage.PASSWORD_CORRECT)
        # Ensure login button is visible
        loginpage.is_element_loaded(By.XPATH, LogInLocators.BUTTON_LOGIN)
        # Click button to validate credentials
        loginpage.click_login_button()
        # Ensure response message is visible
        loginpage.is_element_loaded(By.XPATH, LogInLocators.LABEL_RESPONSE)
        # Validate response message
        self.assertIn(loginpage.SUCCESS_MESSAGE,
                      loginpage.get_text_from_element(By.XPATH, LogInLocators.LABEL_RESPONSE))
        # Ensure logout button is visible
        loginpage.is_element_loaded(By.XPATH, LogInLocators.BUTTON_LOGOUT)
        # Click Logout button
        loginpage.click_logout_button()
        # Ensure response message is visible
        loginpage.is_element_loaded(By.XPATH, LogInLocators.LABEL_RESPONSE)
        # Validate Logout response message
        self.assertIn(loginpage.LOGOUT_MESSAGE,
                      loginpage.get_text_from_element(By.XPATH, LogInLocators.LABEL_RESPONSE))
        # Ensure username text box is visible
        loginpage.is_element_loaded(By.XPATH, LogInLocators.TEXTBOX_USERNAME)
        # Validate username text box is blank
        self.assertEqual(loginpage.get_text_from_element(By.XPATH, LogInLocators.TEXTBOX_USERNAME), "")
        # Ensure password textbox is visible
        loginpage.is_element_loaded(By.XPATH, LogInLocators.TEXTBOX_PASSWORD)
        # Validate password text box is blank
        self.assertEqual(loginpage.get_text_from_element(By.XPATH, LogInLocators.TEXTBOX_PASSWORD), "")

    def tearDown(self):
        result = self._outcome.result
        ok = all(test != self for test, text in result.errors + result.failures)

        if ok:
            print('\nOK: %s' % (self.id(),))
        for typ, errors in (('ERROR', result.errors), ('FAIL', result.failures)):
            for test, text in errors:
                if test is self:
                    msg = [x for x in text.split('\n')[1:]
                           if not x.startswith(' ')][0]
                    print("\n\n%s: %s\n     %s" % (typ, self.id(), msg))
        self.driver.quit()


# Question 2: Write tests for all three javascript alerts: https://the-internet.herokuapp.com/javascript_alerts
class JavascriptAlertTests(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()

    def test_js_alert(self):
        # Create JsAlert object
        jsalertpage = JsAlertPage(self.driver)
        # Navigate to correct page
        jsalertpage.navigate()
        # Ensure JS Alert button is visible
        jsalertpage.is_element_loaded(By.XPATH, JsLocators.BUTTON_ALERT)
        # Click JS Alert button
        jsalertpage.click_jsalert_button()
        # Switch Focus to Alert Message
        alert = self.driver.switch_to.alert
        # Validate JS Alert message
        self.assertEqual(self.driver.switch_to.alert.text, jsalertpage.MESSAGE_JSALERT)
        # Click on alert message
        alert.accept()
        # Ensure result message is visible
        jsalertpage.is_element_loaded(By.XPATH, JsLocators.LABEL_RESPONSE)
        # Validate response message
        self.assertEqual(jsalertpage.get_text_from_element(By.XPATH, JsLocators.LABEL_RESPONSE),
                         jsalertpage.MESSAGE_ALERT)

    def test_js_confirm_ok(self):
        # Create JsAlert object
        jsalertpage = JsAlertPage(self.driver)
        # Navigate to correct page
        jsalertpage.navigate()
        # Ensure JS Confirm button is visible
        jsalertpage.is_element_loaded(By.XPATH, JsLocators.BUTTON_CONFIRM)
        # Click JS Confirm button
        jsalertpage.click_jsconfirm_button()
        # Switch Focus to Alert Message
        alert = self.driver.switch_to.alert
        # Validate JS Confirm message
        self.assertEqual(self.driver.switch_to.alert.text, jsalertpage.MESSAGE_JSCONFIRM)
        # Click on OK button
        alert.accept()
        # Ensure result message is visible
        jsalertpage.is_element_loaded(By.XPATH, JsLocators.LABEL_RESPONSE)
        # Validate response message
        self.assertEqual(jsalertpage.get_text_from_element(By.XPATH, JsLocators.LABEL_RESPONSE),
                         jsalertpage.MESSAGE_CONFIRM)

    def test_js_confirm_cancel(self):
        # Create JsAlert object
        jsalertpage = JsAlertPage(self.driver)
        # Navigate to correct page
        jsalertpage.navigate()
        # Ensure JS Confirm button is visible
        jsalertpage.is_element_loaded(By.XPATH, JsLocators.BUTTON_CONFIRM)
        # Click JS Confirm button
        jsalertpage.click_jsconfirm_button()
        # Switch Focus to Alert Message
        alert = self.driver.switch_to.alert
        # Validate JS Confirm message
        self.assertEqual(self.driver.switch_to.alert.text, jsalertpage.MESSAGE_JSCONFIRM)
        # Click on Cancel button
        alert.dismiss()
        # Ensure response message is visible
        jsalertpage.is_element_loaded(By.XPATH, JsLocators.LABEL_RESPONSE)
        # Validate response message
        self.assertEqual(jsalertpage.get_text_from_element(By.XPATH, JsLocators.LABEL_RESPONSE),
                         jsalertpage.MESSAGE_CANCEL)

    def test_js_prompt_text(self):
        # Create JSAlert object
        jsalertpage = JsAlertPage(self.driver)
        # Navigate to correct page
        jsalertpage.navigate()
        # Ensure JS Prompt button is visible
        jsalertpage.is_element_loaded(By.XPATH, JsLocators.BUTTON_PROMPT)
        # Click JS Prompt button
        jsalertpage.click_jsprompt_button()
        # Switch Focus to Alert Message
        alert = self.driver.switch_to.alert
        # Validate JS Prompt message
        self.assertEqual(self.driver.switch_to.alert.text, jsalertpage.MESSAGE_JSPROMPT)
        # Input Text
        alert.send_keys(jsalertpage.MESSAGE_TESTPROMPT)
        # Click on OK
        alert.accept()
        # Ensure result message is visible
        jsalertpage.is_element_loaded(By.XPATH, JsLocators.LABEL_RESPONSE)
        # Validate response message
        responsemessage = jsalertpage.get_text_from_element(By.XPATH, JsLocators.LABEL_RESPONSE)
        testmessage = jsalertpage.MESSAGE_RESPONSE.format(inputvalue=jsalertpage.MESSAGE_TESTPROMPT)
        self.assertEqual(responsemessage, testmessage)

    def test_js_prompt_blank(self):
        # Create JSAlert object
        jsalertpage = JsAlertPage(self.driver)
        # Navigate to correct page
        jsalertpage.navigate()
        # Ensure JS Prompt button is visible
        jsalertpage.is_element_loaded(By.XPATH, JsLocators.BUTTON_PROMPT)
        # Click JS Prompt button
        jsalertpage.click_jsprompt_button()
        # Switch Focus to Alert Message
        alert = self.driver.switch_to.alert
        # Validate JS Prompt message
        self.assertEqual(self.driver.switch_to.alert.text, jsalertpage.MESSAGE_JSPROMPT)
        # Input nothing, then click on OK
        alert.accept()
        # Ensure result message is visible
        jsalertpage.is_element_loaded(By.XPATH, JsLocators.LABEL_RESPONSE)
        # Validate response message
        responsemessage = jsalertpage.get_text_from_element(By.XPATH, JsLocators.LABEL_RESPONSE).strip()
        testmessage = jsalertpage.MESSAGE_RESPONSE.format(inputvalue="").strip()
        self.assertEqual(responsemessage, testmessage)

    def test_js_prompt_cancel(self):
        # Create JSAlert object
        jsalertpage = JsAlertPage(self.driver)
        # Navigate to correct page
        jsalertpage.navigate()
        # Ensure JS Prompt button is visible
        jsalertpage.is_element_loaded(By.XPATH, JsLocators.BUTTON_PROMPT)
        # Click JS Prompt button
        jsalertpage.click_jsprompt_button()
        # Switch Focus to Alert Message
        alert = self.driver.switch_to.alert
        # Validate JS Prompt message
        self.assertEqual(self.driver.switch_to.alert.text, jsalertpage.MESSAGE_JSPROMPT)
        # Click on Cancel button
        alert.dismiss()
        # Ensure result message is visible
        jsalertpage.is_element_loaded(By.XPATH, JsLocators.LABEL_RESPONSE)
        # Validate response message
        responsemessage = jsalertpage.get_text_from_element(By.XPATH, JsLocators.LABEL_RESPONSE)
        testmessage = jsalertpage.MESSAGE_RESPONSE.format(inputvalue="null")
        self.assertEqual(responsemessage, testmessage)

    def tearDown(self):
        result = self._outcome.result
        ok = all(test != self for test, text in result.errors + result.failures)

        if ok:
            print('\nOK: %s' % (self.id(),))
        for typ, errors in (('ERROR', result.errors), ('FAIL', result.failures)):
            for test, text in errors:
                if test is self:
                    msg = [x for x in text.split('\n')[1:]
                           if not x.startswith(' ')][0]
                    print("\n\n%s: %s\n     %s" % (typ, self.id(), msg))
        self.driver.quit()


# Question 3: Validate dynamic controls - enable/disable input field and checkbox: https://the-internet.herokuapp.com/dynamic_controls
class DynamicTests(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()

    def test_click_enable_disable_button(self):
        # Create DynamicPage Object
        dynamicpage = DynamicPage(self.driver)
        # Navigate to correct page
        dynamicpage.navigate()
        # Ensure text box is visible
        dynamicpage.is_element_loaded(By.XPATH, DynamicLocators.TEXTBOX_TEXT)
        # Validate disabled state
        self.assertEqual(dynamicpage.driver.find_element(By.XPATH, DynamicLocators.TEXTBOX_TEXT).is_enabled(), False)
        # Ensure Enable button is visible
        dynamicpage.is_element_loaded(By.XPATH, DynamicLocators.BUTTON_ENABLE)
        # Click Enable button
        dynamicpage.click_enable_button()
        # Ensure the response label is visible
        dynamicpage.is_element_loaded(By.XPATH, DynamicLocators.LABEL_RESPONSE)
        # Validate response message
        self.assertEqual(dynamicpage.get_text_from_element(By.XPATH, DynamicLocators.LABEL_RESPONSE),
                         dynamicpage.MESSAGE_ENABLED)
        # Ensure text box is visible
        dynamicpage.is_element_loaded(By.XPATH, DynamicLocators.TEXTBOX_TEXT)
        # Validate enabled state
        self.assertEqual(dynamicpage.driver.find_element(By.XPATH, DynamicLocators.TEXTBOX_TEXT).is_enabled(), True)
        # Ensure Disable button is visible
        dynamicpage.is_element_loaded(By.XPATH, DynamicLocators.BUTTON_DISABLE)
        # Click Disable button
        dynamicpage.click_disable_button()
        # Ensure response label is visible
        dynamicpage.is_element_loaded(By.XPATH, DynamicLocators.LABEL_RESPONSE)
        # Validate response message
        self.assertEqual(dynamicpage.get_text_from_element(By.XPATH, DynamicLocators.LABEL_RESPONSE),
                         dynamicpage.MESSAGE_DISABLED)
        # Ensure text box is visible
        dynamicpage.is_element_loaded(By.XPATH, DynamicLocators.TEXTBOX_TEXT)
        # Validate disabled state
        self.assertEqual(dynamicpage.driver.find_element(By.XPATH, DynamicLocators.TEXTBOX_TEXT).is_enabled(), False)

    def test_checkbox(self):
        # Create DynamicPage Object
        dynamicpage = DynamicPage(self.driver)
        # Navigate to correct page
        dynamicpage.navigate()
        # Ensure checkbox is visible
        dynamicpage.is_element_loaded(By.XPATH, DynamicLocators.CB_BOX)
        # Validate unchecked state
        self.assertEqual(dynamicpage.get_checkbox_state(), False)
        # Validate checkbox text
        self.assertEqual(dynamicpage.get_text_from_element(By.XPATH, DynamicLocators.CB_TEXT),
                         dynamicpage.MESSAGE_CHECKBOX)
        # Click checkbox
        dynamicpage.click_checkbox()
        # Validate checked state
        self.assertEqual(dynamicpage.get_checkbox_state(), True)
        # Validate Remove button is visible
        dynamicpage.is_element_loaded(By.XPATH, DynamicLocators.BUTTON_REMOVE)
        # Click Remove button
        dynamicpage.click_remove_button()
        # Ensure response label is visible
        dynamicpage.is_element_loaded(By.XPATH, DynamicLocators.LABEL_RESPONSE)
        # Validate response message
        self.assertEqual(dynamicpage.get_text_from_element(By.XPATH, DynamicLocators.LABEL_RESPONSE),
                         dynamicpage.MESSAGE_GONE)
        # Ensure Add button is visible
        dynamicpage.is_element_loaded(By.XPATH, DynamicLocators.BUTTON_ADD)
        # Click Add button
        dynamicpage.click_add_button()
        # Ensure response label is visible
        dynamicpage.is_element_loaded(By.XPATH, DynamicLocators.LABEL_RESPONSE)
        # Validate response message
        self.assertEqual(dynamicpage.get_text_from_element(By.XPATH, DynamicLocators.LABEL_RESPONSE),
                         dynamicpage.MESSAGE_BACK)
        # Ensure checkbox is visible
        dynamicpage.is_element_loaded(By.XPATH, DynamicLocators.CB_BOX)
        # Validate unchecked state
        self.assertEqual(dynamicpage.get_checkbox_state(), False)

    def tearDown(self):
        result = self._outcome.result
        ok = all(test != self for test, text in result.errors + result.failures)

        if ok:
            print('\nOK: %s' % (self.id(),))
        for typ, errors in (('ERROR', result.errors), ('FAIL', result.failures)):
            for test, text in errors:
                if test is self:
                    msg = [x for x in text.split('\n')[1:]
                           if not x.startswith(' ')][0]
                    print("\n\n%s: %s\n     %s" % (typ, self.id(), msg))
        self.driver.quit()


# Question 4: Write a test to check the current latitude and longitude: https://the-internet.herokuapp.com/geolocation
class LatLongTests(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()

    def test_click_button(self):
        # Create LatLongPage object
        latlongpage = LatLongPage(self.driver)
        # Navigate to correct page
        latlongpage.navigate()
        # Ensure button is visible
        latlongpage.is_element_loaded(By.XPATH, LatLongLocators.BUTTON_WHERE)
        # Click button to display latitude and longitude
        latlongpage.click_button()
        # Ensure latitude is visible
        latlongpage.is_element_loaded(By.XPATH, LatLongLocators.LABEL_LAT)
        # Ensure latitude value isn't blank
        self.assertNotEqual(latlongpage.get_text_from_element(By.XPATH, LatLongLocators.LABEL_LAT), "")
        # Ensure longitude is visible
        latlongpage.is_element_loaded(By.XPATH, LatLongLocators.LABEL_LONG)
        # Ensure longitude value isn't blank
        self.assertNotEqual(latlongpage.get_text_from_element(By.XPATH, LatLongLocators.LABEL_LONG), "")

    def tearDown(self):
        result = self._outcome.result
        ok = all(test != self for test, text in result.errors + result.failures)

        if ok:
            print('\nOK: %s' % (self.id(),))
        for typ, errors in (('ERROR', result.errors), ('FAIL', result.failures)):
            for test, text in errors:
                if test is self:
                    msg = [x for x in text.split('\n')[1:]
                           if not x.startswith(' ')][0]
                    print("\n\n%s: %s\n     %s" % (typ, self.id(), msg))
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
