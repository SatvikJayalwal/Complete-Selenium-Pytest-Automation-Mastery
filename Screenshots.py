# Screenshots

# =====================================================================
# TAKING SCREENSHOTS (VISUAL EVIDENCE)
# Best Practice: Use in test teardowns to provide visual proof of bugs.
# =====================================================================

# 1. FULL VIEWPORT SCREENSHOT
# Captures: The entire visible browser viewport.
# Best for: General failure evidence (e.g., "The whole page crashed").
# driver.save_screenshot("path.png") 

# 2. ELEMENT-SPECIFIC SCREENSHOT
# Captures: Only the specific physical dimensions of a single WebElement.
# Best for: Visual regression testing (e.g., "Did the logo change colors?").
# element.screenshot("path.png")

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
time.sleep(2)

form = driver.find_element(By.XPATH,"//form[@id='login']")

form.screenshot("form.jpg")

driver.save_screenshot("test.jpg")

time.sleep(1)

driver.quit()