# test_true_automatic.py
from selenium.webdriver.common.by import By

# By putting 'browser' in the parentheses, we ask the Control Room for the car key!
def test_correct_title(browser):
    browser.get("https://www.saucedemo.com/")
    
    # I am intentionally putting the WRONG title here to force a failure
    assert browser.title == "Wrong Title Labs"

def test_missing_button(browser):
    browser.get("https://www.saucedemo.com/")
    
    # I am intentionally looking for a fake button to force a failure
    browser.find_element(By.ID, "this-does-not-exist")