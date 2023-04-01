import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Pages.loginpageaction import LoginPageAction
from Pages.jsalertpageaction import JsAlertPageAction
from Pages.dynamicpageaction import DynamicPageAction
from Pages.latlongpageaction import LatLongPageAction
from Pages.constants import *


def suppressWebdriverMessages(driver):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def outputResults(obj):
    result = obj._outcome.result
    ok = all(test != obj for test, text in result.errors + result.failures)

    if ok:
        print('\nOK: %s' % (obj.id(),))
    for typ, errors in (('ERROR', result.errors), ('FAIL', result.failures)):
        for test, text in errors:
            if test is obj:
                msg = [x for x in text.split('\n')[1:]
                       if not x.startswith(' ')][0]
                print("\n\n%s: %s\n     %s" % (typ, obj.id(), msg))


# Question 1: Write a couple of tests you think would be necessary for the following form: https://the-internet.herokuapp.com/login
class LogInTests(unittest.TestCase):
    def setUp(self):
        suppressWebdriverMessages(self)
        self.driver.maximize_window()

    def test_login_validUsername_invalidPassword(self):
        # Create LogInPageAction object
        login_page = LoginPageAction(self.driver)
        # Navigate to correct page
        login_page.navigate(url_login_page)
        # Input valid username
        login_page.input_text_username(input_username_valid)
        # Input invalid password
        login_page.input_text_password(input_password_invalid)
        # Click button to validate credentials
        login_page.click_login_button()
        # Test Response message
        self.assertIn(message_login_invalid_password, login_page.get_response_value())
        # Test Username text is blank
        self.assertEqual(login_page.get_username_value(), blank)
        # Test Password text is blank
        self.assertEqual(login_page.get_password_value(), blank)

    def test_login_invalidUsername_validPassword(self):
        # Create LogInPageAction object
        login_page = LoginPageAction(self.driver)
        # Navigate to correct page
        login_page.navigate(url_login_page)
        # Input invalid username
        login_page.input_text_username(input_username_invalid)
        # Input valid password
        login_page.input_text_password(input_password_valid)
        # Click button to validate credentials
        login_page.click_login_button()
        # Test Response message
        self.assertIn(message_login_invalid_username, login_page.get_response_value())
        # Test Username text is blank
        self.assertEqual(login_page.get_username_value(), blank)
        # Test Password text is blank
        self.assertEqual(login_page.get_password_value(), blank)

    def test_login_invalidUsername_invalidPassword(self):
        # Create LogInPageAction object
        login_page = LoginPageAction(self.driver)
        # Navigate to correct page
        login_page.navigate(url_login_page)
        # Input invalid username
        login_page.input_text_username(input_username_invalid)
        # Input invalid password
        login_page.input_text_password(input_password_invalid)
        # Click button to validate credentials
        login_page.click_login_button()
        # Test Response message
        self.assertIn(message_login_invalid_username, login_page.get_response_value())
        # Test Username text is blank
        self.assertEqual(login_page.get_username_value(), blank)
        # Test Password text is blank
        self.assertEqual(login_page.get_password_value(), blank)

    def test_login_validUsername_validPassword(self):
        # Create LogInPageAction object
        login_page = LoginPageAction(self.driver)
        # Navigate to correct page
        login_page.navigate(url_login_page)
        # Input valid username
        login_page.input_text_username(input_username_valid)
        # Input valid password
        login_page.input_text_password(input_password_valid)
        # Click button to validate credentials
        login_page.click_login_button()
        # Test Response message
        self.assertIn(message_login_securearea_success, login_page.get_response_value())

    def test_logout(self):
        # Create LogInPageAction object
        login_page = LoginPageAction(self.driver)
        # Navigate to correct page
        login_page.navigate(url_login_page)
        # Input valid username
        login_page.input_text_username(input_username_valid)
        # Input valid password
        login_page.input_text_password(input_password_valid)
        # Click button to validate credentials
        login_page.click_login_button()
        # Click button to log out
        login_page.click_logout_button()
        # Test Response message
        self.assertIn(message_login_securearea_logout, login_page.get_response_value())
        # Test Username text is blank
        self.assertEqual(login_page.get_username_value(), blank)
        # Test Password text is blank
        self.assertEqual(login_page.get_password_value(), blank)

    def tearDown(self):
        outputResults(self)
        self.driver.quit()


# Question 2: Write tests for all three javascript alerts: https://the-internet.herokuapp.com/javascript_alerts
class JavascriptAlertTests(unittest.TestCase):
    def setUp(self):
        suppressWebdriverMessages(self)
        self.driver.maximize_window()

    def test_js_alert_click_ok(self):
        # Create JsAlertPageAction object
        alert_page = JsAlertPageAction(self.driver)
        # Navigate to correct page
        alert_page.navigate(url_javascript_alerts)
        # Click JS Alert button
        alert_page.click_js_alert_button()
        # Switch focus to Alert Message
        alert = self.driver.switch_to.alert
        # Test JS Alert message
        self.assertEqual(alert.text, message_jsalert)
        # Click on alert message
        alert.accept()
        # Test Response message
        self.assertEqual(message_jsalert_click, alert_page.get_response_value())

    def test_js_confirm_click_ok(self):
        # Create JsAlertPageAction object
        alert_page = JsAlertPageAction(self.driver)
        # Navigate to correct page
        alert_page.navigate(url_javascript_alerts)
        # Click JS Confirm button
        alert_page.click_js_confirm_button()
        # Switch focus to Alert Message
        alert = self.driver.switch_to.alert
        # Test JS Confirm message
        self.assertEqual(alert.text, message_jsconfirm)
        # Click on OK button
        alert.accept()
        # Test Response message
        self.assertEqual(message_jsalert_confirm, alert_page.get_response_value())

    def test_js_confirm_click_cancel(self):
        # Create JsAlertPageAction object
        alert_page = JsAlertPageAction(self.driver)
        # Navigate to correct page
        alert_page.navigate(url_javascript_alerts)
        # Click JS Confirm button
        alert_page.click_js_confirm_button()
        # Switch focus to Alert Message
        alert = self.driver.switch_to.alert
        # Test JS Confirm message
        self.assertEqual(alert.text, message_jsconfirm)
        # Click on OK button
        alert.dismiss()
        # Test Response message
        self.assertEqual(message_jsalert_cancel, alert_page.get_response_value())

    def test_js_prompt_input_text_click_ok(self):
        # Create JsAlertPageAction object
        alert_page = JsAlertPageAction(self.driver)
        # Navigate to correct page
        alert_page.navigate(url_javascript_alerts)
        # Click JS Prompt button
        alert_page.click_js_prompt_button()
        # Switch Focus to Alert Message
        alert = self.driver.switch_to.alert
        # Test JS Prompt message
        self.assertEqual(alert.text, message_jsprompt)
        # Input text into JS Prompt
        alert.send_keys(input_testprompt)
        # Click on OK
        alert.accept()
        # Test Response message
        self.assertEqual(message_jsprompt_message.format(inputvalue=input_testprompt), alert_page.get_response_value())

    def test_js_prompt_input_text_click_cancel(self):
        # Create JsAlertPageAction object
        alert_page = JsAlertPageAction(self.driver)
        # Navigate to correct page
        alert_page.navigate(url_javascript_alerts)
        # Click JS Prompt button
        alert_page.click_js_prompt_button()
        # Switch Focus to Alert Message
        alert = self.driver.switch_to.alert
        # Test JS Prompt message
        self.assertEqual(alert.text, message_jsprompt)
        # Input text into JS Prompt
        alert.send_keys(input_testprompt)
        # Click on Cancel
        alert.dismiss()
        # Test Response message
        self.assertEqual(message_jsprompt_message.format(inputvalue="null"), alert_page.get_response_value())

    def test_js_prompt_click_cancel(self):
        # Create JsAlertPageAction object
        alert_page = JsAlertPageAction(self.driver)
        # Navigate to correct page
        alert_page.navigate(url_javascript_alerts)
        # Click JS Prompt button
        alert_page.click_js_prompt_button()
        # Switch Focus to Alert Message
        alert = self.driver.switch_to.alert
        # Test JS Prompt message
        self.assertEqual(alert.text, message_jsprompt)
        # Click on Cancel
        alert.dismiss()
        # Test Response message
        self.assertEqual(message_jsprompt_message.format(inputvalue="null"), alert_page.get_response_value())

    def test_js_prompt_input_blank_text_click_ok(self):
        # Create JsAlertPageAction object
        alert_page = JsAlertPageAction(self.driver)
        # Navigate to correct page
        alert_page.navigate(url_javascript_alerts)
        # Click JS Prompt button
        alert_page.click_js_prompt_button()
        # Switch Focus to Alert Message
        alert = self.driver.switch_to.alert
        # Test JS Prompt message
        self.assertEqual(alert.text, message_jsprompt)
        # Input blank text into JS Prompt
        alert.send_keys(blank)
        # Click on OK
        alert.accept()
        # Test Response message
        self.assertEqual(message_jsprompt_message.format(inputvalue=blank).strip(), alert_page.get_response_value())

    def tearDown(self):
        outputResults(self)
        self.driver.quit()


# Question 3: Validate dynamic controls - enable/disable input field and checkbox: https://the-internet.herokuapp.com/dynamic_controls
class DynamicTests(unittest.TestCase):
    def setUp(self):
        suppressWebdriverMessages(self)
        self.driver.maximize_window()

    def test_click_enable_button(self):
        # Create DynamicPageAction Object
        dynamic_page = DynamicPageAction(self.driver)
        # Navigate to correct page
        dynamic_page.navigate(url_dynamic_controls)
        # Click Enable button
        dynamic_page.click_enable_button()
        # Wait for loading element to disappear
        dynamic_page.wait_for_enable_disable_loading_element_to_disappear()
        # Test Response message
        self.assertEqual(message_dynamic_enabled, dynamic_page.get_response_value())
        # Test text box enabled state
        self.assertEqual(dynamic_page.get_textbox_state(), True)

    def test_click_disable_button(self):
        # Create DynamicPageAction Object
        dynamic_page = DynamicPageAction(self.driver)
        # Navigate to correct page
        dynamic_page.navigate(url_dynamic_controls)
        # Click Enable button
        dynamic_page.click_enable_button()
        # Wait for loading element to disappear
        dynamic_page.wait_for_enable_disable_loading_element_to_disappear()
        # Click Disable button
        dynamic_page.click_disable_button()
        # Wait for loading element to disappear
        dynamic_page.wait_for_enable_disable_loading_element_to_disappear()
        # Test Response message
        self.assertEqual(message_dynamic_disabled, dynamic_page.get_response_value())
        # Test text box enabled state
        self.assertEqual(dynamic_page.get_textbox_state(), False)

    def test_click_checkbox_checked(self):
        # Create DynamicPageAction Object
        dynamic_page = DynamicPageAction(self.driver)
        # Navigate to correct page
        dynamic_page.navigate(url_dynamic_controls)
        # Test checkbox unchecked state
        self.assertEqual(dynamic_page.get_checkbox_state(), False)
        # Click checkbox
        dynamic_page.click_checkbox()
        # Test checkbox checked state
        self.assertEqual(dynamic_page.get_checkbox_state(), True)

    def test_click_checkbox_unchecked(self):
        # Create DynamicPageAction Object
        dynamic_page = DynamicPageAction(self.driver)
        # Navigate to correct page
        dynamic_page.navigate(url_dynamic_controls)
        # Test checkbox unchecked state
        self.assertEqual(dynamic_page.get_checkbox_state(), False)
        # Click checkbox
        dynamic_page.click_checkbox()
        # Click checkbox again
        dynamic_page.click_checkbox()
        # Test checkbox unchecked state
        self.assertEqual(dynamic_page.get_checkbox_state(), False)

    def test_click_checkbox_remove_button(self):
        # Create DynamicPageAction Object
        dynamic_page = DynamicPageAction(self.driver)
        # Navigate to correct page
        dynamic_page.navigate(url_dynamic_controls)
        # Click Remove button
        dynamic_page.click_remove_button()
        # Wait for loading element to disappear
        dynamic_page.wait_for_remove_add_loading_element_to_disappear()
        # Test response message
        self.assertEqual(message_dynamic_gone, dynamic_page.get_response_value())

    def test_click_checkbox_add_button_checked(self):
        # Create DynamicPageAction Object
        dynamic_page = DynamicPageAction(self.driver)
        # Navigate to correct page
        dynamic_page.navigate(url_dynamic_controls)
        # Click checkbox
        dynamic_page.click_checkbox()
        # Click Remove button
        dynamic_page.click_remove_button()
        # Wait for loading element to disappear
        dynamic_page.wait_for_remove_add_loading_element_to_disappear()
        # Click Add button
        dynamic_page.click_add_button()
        # Wait for loading element to disappear
        dynamic_page.wait_for_remove_add_loading_element_to_disappear()
        # Test response message
        self.assertEqual(message_dynamic_back, dynamic_page.get_response_value())
        # Test checkbox is unchecked
        self.assertEqual(dynamic_page.get_checkbox_state(), False)

    def test_click_checkbox_add_button_unchecked(self):
        # Create DynamicPageAction Object
        dynamic_page = DynamicPageAction(self.driver)
        # Navigate to correct page
        dynamic_page.navigate(url_dynamic_controls)
        # Click Remove button
        dynamic_page.click_remove_button()
        # Wait for loading element to disappear
        dynamic_page.wait_for_remove_add_loading_element_to_disappear()
        # Click Add button
        dynamic_page.click_add_button()
        # Wait for loading element to disappear
        dynamic_page.wait_for_remove_add_loading_element_to_disappear()
        # Test response message
        self.assertEqual(message_dynamic_back, dynamic_page.get_response_value())
        # Test checkbox is unchecked
        self.assertEqual(dynamic_page.get_checkbox_state(), False)

    def tearDown(self):
        outputResults(self)
        self.driver.quit()


# Question 4: Write a test to check the current latitude and longitude: https://the-internet.herokuapp.com/geolocation
class LatLongTests(unittest.TestCase):
    def setUp(self):
        suppressWebdriverMessages(self)
        self.driver.maximize_window()
        # Configure webdriver to use defined latitude and longitude
        params = {
            "latitude": input_latitude,
            "longitude": input_longitude,
            "accuracy": 100
        }
        self.driver.execute_cdp_cmd("Page.setGeolocationOverride", params)

    def test_click_button(self):
        # Create LatLongPage object
        latlng_page = LatLongPageAction(self.driver)
        # Navigate to correct page
        latlng_page.navigate(url_latlong_page)
        # Click button to display latitude and longitude
        latlng_page.click_where_button()
        # Test Latitude value
        self.assertEqual(latlng_page.get_latitude_value(), input_latitude)
        # Test Longitude value
        self.assertEqual(latlng_page.get_longitude_value(), input_longitude)

    def tearDown(self):
        outputResults(self)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
