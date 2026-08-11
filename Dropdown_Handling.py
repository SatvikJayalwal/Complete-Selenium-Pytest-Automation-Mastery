# Select class (visible_text, value, index), Custom Bootstrap dropdowns

# Select 
# You must first import the Select class, 
# pass your located element into it, and then choose one of three selection methods:

# select_by_visible_text(): Selects the exact text the user sees on the screen.
# select_by_value(): Selects based on the hidden HTML value attribute. 
# select_by_index(): Selects based on position, starting at 0. 

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

time.sleep(2)

dropdown = driver.find_element(By.XPATH,"//select[@id='dropdown-class-example']")

dropdown_options = Select(dropdown)

dropdown_options.select_by_index(2)
dropdown_options.select_by_visible_text("Option1")
dropdown_options.select_by_value("option3")

time.sleep(1)



# Modern websites (built with React, Angular, or Bootstrap) rarely use the standard 
# <select> tag as it is difficult to style with CSS.
# Instead, developers build "fake" dropdowns using <div>, <ul>, and <li> tags, and 
# use JavaScript to make them look and act like dropdowns.

##Eg.
## <div id="custom-dropdown-btn">Select Country</div>
## <ul class="dropdown-menu">
##     <li>United States</li>
##     <li>Canada</li>
##     <li>Mexico</li>
## </ul>

# If you try to put a <div> or <ul> into Selenium's Select class, your script will 
# immediately crash with an UnexpectedTagNameException.


# Strategy
# To automate these, you have to do exactly what a human does:
# Click the dropdown button to open the menu.
# Grab all the options into a Python List using find_elements().
# Loop through the list, check the text, and click the one you want.


driver.get("https://demoqa.com/automation-practice-form")
time.sleep(1)
driver.execute_script("window.scrollTo(0, 500);")
time.sleep(1)

state_dropdown_trigger = driver.find_element(By.ID,"state")
state_dropdown_trigger.click()

time.sleep(1)

modern_dropdown_options = driver.find_elements(By.XPATH,"//div[contains(@id,'react-select-3-option')]")

for option in modern_dropdown_options :
    
    if option.text=="Haryana":
        print(f"Clicking {option.text}")
        option.click()
        break

time.sleep(1)
driver.quit()