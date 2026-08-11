# The Auto-Discovery Naming Conventions
# Pytest operates on "Auto-Discovery." When you type pytest in your terminal, it scans your 
# entire project folder looking for tests. But it is entirely blind unless you follow three 
# strict naming conventions.

# File Names: Your Python files must start with test_ or end with _test.py.
# Good: test_login.py
# Bad: login_script.py (Pytest will ignore this completely).

# Function Names: Your test functions inside the file must start with test_.
# Good: def test_valid_credentials():
# Bad: def verify_login(): (Pytest will skip this function).

# Class Names (Optional): If you group your tests inside classes, the class name must start 
# with a capital Test and cannot have an __init__ method.
# Good: class TestLoginFeature:



# Assertions : 
# An assertion are checkpoint in your code that compares the Actual Result of a test against 
# the Expected Result.

# Without assertions, your automation script is just blindly clicking buttons—it's not actually 
# testing anything! If the assertion passes, the test passes. If the actual and expected 
# results don't match, the assertion fails, and you've caught a bug.

# In Pytest, you never use if/else for validations. You use the Python assert keyword.


# 4 Essential Types of Assertions

# 1. Page/URL Assertion (Did we land in the right place?)
# After clicking "Login", you want to verify that browser actually navigated to inventory page.

# Expected: [https://www.saucedemo.com/inventory.html](https://www.saucedemo.com/inventory.html)
# Actual: driver.current_url

# 2. Text Assertion (Is the message correct?)
# If a user types the wrong password, they should see a specific error message.

# Expected: "Epic sadface: Username and password do not match any user in this service"
# Actual: error_element.text

# 3. Visibility/State Assertion (Is the element there?)
# Once logged in, is the shopping cart icon visible on the screen?

# Expected: True (The element is displayed)
# Actual: cart_icon.is_displayed()

# 4. Count Assertion (Are all items loading?)
# The Swag Labs homepage should load exactly 6 inventory items. If a developer accidentally 
# breaks the database, maybe only 2 load. We need to check the count.

# Expected: 6
# Actual: len(inventory_items)

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

time.sleep(1)

# ASSERTION 1: TEXT MATCHING (Negative Test)
username = driver.find_element(By.ID,"user-name")
username.send_keys("standard_user")
password = driver.find_element(By.ID,"password")
password.send_keys("wrong_password")
btn = driver.find_element(By.ID,"login-button").click()

time.sleep(1)

error_msg = driver.find_element(By.XPATH,"//h3[@data-test='error']").text

assert "Username and password do not match" in error_msg, f"Unexpected error : {error_msg}"

print("Assertion passed, Error msg is correct")

# ASSERTION 2 & 3: URL & VISIBILITY (Positive Test)

# ASSERT 2: Are we on the right URL?
driver.refresh()
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

assert driver.current_url == "https://www.saucedemo.com/inventory.html", f"Login failed,wrong URL"
print("Url assertion passed .. correct url")

# ASSERT 3: Is the shopping cart visible?
cart = driver.find_element(By.XPATH,"//div[@id='shopping_cart_container']")
assert cart.is_displayed(), "shopping cart not there"
print("Assertion passed shopping cart is displayed")

# ASSERTION 4: COUNTING (List Length)
all_items = driver.find_elements(By.CLASS_NAME,"inventory_item")
assert len(all_items) == 6, "The numbers did not match"
print("Assertion passed number = 6")
time.sleep(1)
driver.quit()

