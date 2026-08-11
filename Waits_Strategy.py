# Page Load Strategies
# Implicit Wait 

# Selenium Page Load Strategies
# Change how driver.get(url) behaves to significantly speed up your scripts:

# 1. normal (Default): Waits for the full page (images, CSS, ads) to load completely. 
# Use for standard UI testing where layout matters.

# 2. eager: Waits only for the HTML (DOM) to load, skipping heavy media. Use for fast data 
# scraping or testing functionality that ignores visuals.

# 3. none: Does not wait at all and returns control to Python instantly. Use only for 
# advanced scripts where you handle custom ready-state logic manually.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.page_load_strategy = "eager"
driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window()



# Implicit Wait (The Global Setting) --> driver.implicitly_wait(10)
#  Implicit Wait is a "set it and forget it" global timeout. You declare it once at the 
# beginning of your script, and it applies to every single find_element() command for the 
# rest of the session.

# If you set an implicit wait of 10 seconds, Selenium will wait upto 10 seconds. 
# If the element appears at second 3, it clicks it and moves on instantly. 
# If 10 seconds pass, it crashes.


# NOTE : While easy to use, they only check if an element is present in the HTML. They do not 
# check if a button is visible or clickable. If a button is hidden behind a loading spinner, 
# Implicit Wait will find the hidden button immediately, attempt to click it, and crash 
# with an ElementNotInteractableException.

driver.implicitly_wait(10)


driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
start_btn = driver.find_element(By.XPATH,"//div[@id='start']/button")
start_btn.click()

delayed_text = driver.find_element(By.ID,"finish")




