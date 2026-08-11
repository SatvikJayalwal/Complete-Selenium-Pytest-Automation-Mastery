# Execute_script() for clicking/scrolling hidden elements

# JavaScript Executor (execute_script())
# Sometimes, you write a perfect locator for a button, and you use .click(), but Selenium 
# crashes with an ElementClickInterceptedException. This happens when a developer places an 
# invisible <div>, a sticky header, or a loading overlay on top of your button.

# Selenium tries to click exactly like a human does. If a human cannot click it because 
# something is in the way, Selenium refuses to click it too.

# The Solution: You bypass the WebDriver entirely and inject native JavaScript directly into 
# the browser. JavaScript does not care about overlays or visibility; it forces the action 
# at the DOM level.

# Common JS Executor Commands:
# The JS Click: driver.execute_script("arguments[0].click();", web_element)

# The JS Scroll (Into View): driver.execute_script("arguments[0].scrollIntoView(true);", web_element)


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/large")

wait = WebDriverWait(driver,5)

wait.until(EC.visibility_of_element_located((By.XPATH,"//h3[contains(text(),'DOM')]")))

last_element = driver.find_element(By.XPATH,"//div[@id='sibling-50.3']")

driver.execute_script("arguments[0].scrollIntoView(true);",last_element)

time.sleep(2)

driver.quit()