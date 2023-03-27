class LogInLocators(object):
    TEXTBOX_USERNAME = "//*[@id=\"username\"]"  # XPATH
    TEXTBOX_PASSWORD = "//*[@id=\"password\"]"  # XPATH
    BUTTON_LOGIN = "//*[@id=\"login\"]/button/i"  # XPATH
    BUTTON_LOGOUT = "//i[@class='icon-2x icon-signout']"  # XPATH
    LABEL_RESPONSE = "//div[@id='flash']"  # XPATH


class JsLocators(object):
    BUTTON_ALERT = "//button[normalize-space()='Click for JS Alert']"  # XPATH
    BUTTON_CONFIRM = "//button[normalize-space()='Click for JS Confirm']"  # XPATH
    BUTTON_PROMPT = "//button[normalize-space()='Click for JS Prompt']"  # XPATH
    LABEL_RESPONSE = "//p[@id='result']"  # XPATH


class DynamicLocators(object):
    BUTTON_ADD = "//button[normalize-space()='Add']"  # XPATH
    BUTTON_DISABLE = "//button[normalize-space()='Disable']"  # XPATH
    BUTTON_ENABLE = "//button[normalize-space()='Enable']"  # XPATH
    BUTTON_REMOVE = "//button[normalize-space()='Remove']"  # XPATH
    CB_BOX = "//input[@type='checkbox']"  # XPATH
    CB_TEXT = "//div[@id='checkbox']"  # XPATH
    LABEL_RESPONSE = "//p[@id='message']"  # XPATH
    TEXTBOX_TEXT = "//input[@type='text']"  # XPATH


class LatLongLocators(object):
    BUTTON_WHERE = "//button[normalize-space()='Where am I?']"  # XPATH
    LABEL_LAT = "//div[@id='lat-value']"  # XPATH
    LABEL_LONG = "//div[@id='long-value']"  # XPATH
