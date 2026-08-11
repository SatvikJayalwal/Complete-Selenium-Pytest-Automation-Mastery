# Text boxes, Buttons, Radio Buttons, Checkboxes

# Text Boxes (Inputs & Textareas)
# In text boxes, always think in a sequence: Locate -> Clear -> Type -> Validate.

# Two Types of text boxes :
# <input type="text">: A single-line text field (like a Username).
# <textarea>: A multi-line text box (like a "Description" section). 
# Selenium treats both exactly the same.

#STEPS
# 1. Locate
# 2. .clear()
# 3. .send_keys()
# 4. .get_attribute()




# Buttons
# Buttons usually trigger an action, like submitting a form or opening a modal.
# The standard way: button.click()

# Steps :
# 1. Locate
# 2. .click()   



# Radio Buttons
# A radio button is a circular button where only one option can be selected at a 
# time within a group. (e.g., selecting your age bracket or gender). 
# If you click a new radio button, the previous one automatically unchecks.

# The Golden Rule for Radio Buttons: Always check its state using is_selected() 
# before clicking it.

# STEPS
# 1. Locate
# 2. .is_selected()
# 3. .click()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(1)

radio_1 = driver.find_element(By.XPATH,"//input[@value='radio1']")
radio_2 = driver.find_element(By.XPATH,"//input[@value='radio2']")

radio_1.click()
print(f"Is radio 1 clicked : {radio_1.is_selected()}")

radio_2.click()
print(f"Is radio 2 clicked : {radio_2.is_selected()}")
print(f"Is radio 1 clicked : {radio_1.is_selected()}")

time.sleep(1)


# Checkboxes
# Checkboxes are square boxes where you can select multiple options at once 
# (e.g., "Select all the programming languages you know"). 
# Unlike radio buttons, clicking a checkbox toggles it (checks it if it is empty, 
# unchecks it if it is filled).

# Because it toggles, is_selected() is mandatory here to ensure you leave the checkbox 
# in the exact state your test requires.

checkbox1 = driver.find_element(By.ID,"checkBoxOption1")
checkbox1.click()
print(f"Is the checkbox1 selected : {checkbox1.is_selected()}")

checkbox3 = driver.find_element(By.ID,"checkBoxOption3")
checkbox3.click()
print(f"Is the checkbox3 selected : {checkbox3.is_selected()}")

time.sleep(1)
driver.quit()
