from selenium import webdriver
from selenium.webdriver.common.by import By

from login_page import LoginPage

def test_successful_login():

    driver = webdriver.Chrome()
    mylogin_page = LoginPage(driver)

    mylogin_page.open_page()
    mylogin_page.login("standard_user","secret_sauce")

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    print("LOGIN SUCCESSFUL")

    driver.quit()

