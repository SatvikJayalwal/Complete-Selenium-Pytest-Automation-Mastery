# above(), below(), to_left_of(), near()

# Relative locators use JavaScript to evaluate the physical size and position (pixels) 
# of elements as they are rendered on the screen.

# You must import the locate_with function to use them:

# Five Relative Locator Commands 
# above()Finds an element positioned higher on the page than the base element.
# below()Finds an element positioned lower on the page than the base element.
# to_left_of()Finds an element positioned to the left of the base element.
# to_right_of()Finds an element positioned to the right of the base element.
# near()Finds an element that is at most 50 pixels away from the base element.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
import time

driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(1)

#base element (easy to find)
username = driver.find_element(By.ID,"username")
username.send_keys("student")

#traverse using locate with 
password = locate_with(By.TAG_NAME,"input").below(username)
driver.find_element(password).send_keys("Password123")


# You can even chain these commands together to be hyper-specific. 
# For example, finding a "Cancel" button that is both to the right of the "Save" 
# button AND below the form header.
# for example
## cancel_btn_loc = locate_with(By.TAG_NAME, "button").below(header).to_right_of(save_btn)
## driver.find_element(cancel_btn_loc).click()


# Disadvantages of Relative Locators
# Responsive Web Design: Because Relative Locators rely on physical screen pixels, 
# they break if the screen size changes. On a Desktop monitor, a "Submit" button 
# might be to_right_of() a text box. But if you run that exact same test on a Mobile 
# view or a smaller window, the test may crash.

# Performance: They are slightly slower than a direct By.ID or CSS Selector because 
# Selenium has to execute JavaScript to calculate the coordinates of multiple elements 
# before it can click.
