# CLI RUNNER (EXECUTING YOUR TESTS)

# IMPORTANT: Do not run Pytest files by clicking the "Play" button in your IDE or typing 
# `python test_file.py`. Execute them via Terminal.
# 
# STANDARD TERMINAL COMMANDS:
# * pytest               : Runs every test found in the current folder and subfolders.
# * pytest test_login.py : Runs only the tests inside that specific file.
# * pytest -v            : (Verbose) Prints the exact name of every test and its status.
# * pytest -s            : Prints your print() statements to the console (hidden by default).
# * pytest -v -s         : (Senior QA Default) Combines both flags for maximum visibility.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_logo():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    logo = driver.find_element(By.XPATH,"//div[@class='login_logo']")

    assert logo.is_displayed(), "Logo not displayed"
    print("Assertion passed, Logo displayed!")

    time.sleep(1)