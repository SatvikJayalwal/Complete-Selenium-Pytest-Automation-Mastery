# click(), send_keys(), clear(), get_attribute(), is_displayed()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(2)


# send_keys()
# This command simulates typing on a keyboard. It is primarily used for <input> and <textarea> tags.
# send_keys() can also simulate pressing special keyboard keys 
# (like Enter, Tab, or the Arrow keys) by importing the Keys class.
username = driver.find_element(By.ID,"user-name")
username.send_keys("standard_user")
username = driver.find_element(By.ID,"password")
username.send_keys("secret_sauce")


# clear()
# Before you type into a text box, it is a golden rule to clear it first.
# If a text box already contains text, Selenium does not automatically delete it. 
# It will simply append your new text to the end of the old text, which may fail test.
username_update = driver.find_element(By.ID,"user-name")
username_update.clear()
username_update.send_keys("visual_user")


# click()
# It clicks on an element. Used on buttons, links, checkboxes, and radio buttons.
# Important Note: To click an element, it must be visible on the screen. 
# If it is covered, Selenium will throw an ElementClickInterceptedException.
click_btn = driver.find_element(By.ID,"login-button")
click_btn.click()

time.sleep(2)


driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(2)

# is_displayed() 
# This is your primary tool for test assertions. 
# Shows True : If element is visible.
# Shows False : If element is not visible.
# Note: An element can exist in the HTML (DOM) but be hidden by developers 
# using CSS (e.g., display: none). In that case, find_element will succeed, 
# but is_displayed() will return False.
text_box = driver.find_element(By.ID,"displayed-text")
hide_text_box = driver.find_element(By.ID,"hide-textbox")
hide_text_box.click()
print(text_box.is_displayed())
show_text_box = driver.find_element(By.ID,"show-textbox")
show_text_box.click()
print(text_box.is_displayed())

# get_attribute()
# you use get_attribute("value") to read exactly what is typed inside a text box.
# You use get_attribute("href") to read the exact URL a link is trying to send you to.
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(2)
username = driver.find_element(By.ID,"username")
username.send_keys("student")
print(username.get_attribute("value"))

driver.quit()