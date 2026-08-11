from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

def test_login(browser):
    browser.get("https://www.saucedemo.com/")
    
    login = browser.find_element(By.ID,"login-button")
    assert login.is_displayed(), "Login not displayed"
    print("Assertion passed, Login is successfully displayed!")