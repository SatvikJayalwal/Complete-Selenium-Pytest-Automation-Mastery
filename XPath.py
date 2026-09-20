# Absolute/Relative, contains(), text(), XPath Axes (parent, child, sibling)

# Absolute XPath (/)
# An absolute XPath starts from root of the HTML document and traces 
# down to your element, layer by layer, using a single forward slash /.
# Example: /html/body/div[2]/div/div[1]/form/input[1]
# Why it is terrible: If a developer adds a single new <div> anywhere on the page, 
# this entire path breaks. 

# NEVER use Absolute XPath in automation.

# Relative XPath (//)
# A relative XPath uses a double forward slash // that tells Selenium: 
# "Scan the entire DOM and jump straight to the first element that matches 
# my criteria, regardless of where it lives."
# Example: //input[@id='user-name']

# Why it is the standard: It is highly flexible to UI changes. 

# ALWAYS USER RELATIVE XPATH in automation.




# Basic Relative XPath Syntax
# //tagname[@attribute='value']

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
time.sleep(1)

# text()
# //tagname[text()='Exact Text']
driver.find_element(By.XPATH,"//button[text()='Add Element']").click()

# contains()
# Syntax (Attribute): //tagname[contains(@attribute, 'partial_value')]
# Syntax (Text): //tagname[contains(text(), 'partial_text')]

driver.find_element(By.XPATH,"//button[contains(text(),'Del')]").click()
time.sleep(1)

# XPath Axes (parent, child, sibling)(Traversing the DOM)
# Syntax : /relation name(eg.parent)::target tag(eg.div)

driver.get("https://the-internet.herokuapp.com/tables")
time.sleep(1)

last_name = driver.find_element(By.XPATH,"//td[text()='fbach@yahoo.com']/parent::tr")
print(f"{last_name.text}")

driver.quit()