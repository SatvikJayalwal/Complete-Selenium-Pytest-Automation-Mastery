# @pytest.fixture, scopes, yield, conftest.py

# PYTEST FIXTURES: QUICK RECALL NOTES

# 1. WHAT IS A FIXTURE? (@pytest.fixture)
# - Think of it as a "Kitchen Assistant" for your tests.
# - It handles the Setup (opening browser) and Teardown (closing browser) automatically.
#
# 2. THE 'YIELD' KEYWORD
# - Divides the fixture into two parts:
#   * Above yield = SETUP (Prep the kitchen / Open Chrome)
#   * The yield itself = Pauses and hands the 'driver' to the test to use.
#   * Below yield = TEARDOWN (Clean up / Close Chrome after the test finishes).
#
# 3. USING THE FIXTURE
# - Just pass the fixture's name into your test's parentheses: def test_login(browser):
# - No need to call the function; Pytest injects the browser automatically.
#
# 4. CONFTEST.PY (The Magic File)
# - A file named exactly 'conftest.py' holds all your fixtures.
# - ANY test file in your project can instantly use these fixtures without importing them.
#
# 5. SCOPES (How often the fixture runs)
# - scope="function" (Default): Opens/closes browser for EVERY test (Safest, fresh browser).
# - scope="module": Opens/closes once per test file.
# - scope="session": Opens/closes once for the entire test run.


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# def test_title():

#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://www.saucedemo.com/")

#     title = driver.title
#     assert title == "Swag Labs", "Title is wrong"
#     print(f"Assertion passed, Title : {title}")
#     driver.quit()

# def test_login():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://www.saucedemo.com/")

#     login = driver.find_element(By.ID,"login-button")
#     assert login.is_displayed(), "Login not displayed"
#     print("Assertion passed, Login is successfully displayed!")
#     driver.quit()

# The issue: You wrote driver = webdriver.Chrome() and driver.quit() twice. 
# If you had 50 tests, you would write them 50 times. That is messy and hard to maintain!


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.fixture

def browser():

    driver = webdriver.Chrome()               #SETUP :LAUNCH BROWSER
    yield driver                              #YIELD : HAND DRIVER TO TEST AND PAUSE
    driver.quit()                             #TEARDOWN : CLOSE BROSER AFTER TEST


def test_title(browser):
    browser.get("https://www.saucedemo.com/")
    title = browser.title
    assert title == "Swag Labs", "Title is wrong"
    print(f"Assertion passed, Title : {title}")

def test_login(browser):
    browser.get("https://www.saucedemo.com/")
    
    login = browser.find_element(By.ID,"login-button")
    assert login.is_displayed(), "Login not displayed"
    print("Assertion passed, Login is successfully displayed!")

# To run the code from terminal --> pytest Fixtures.py -v -s 