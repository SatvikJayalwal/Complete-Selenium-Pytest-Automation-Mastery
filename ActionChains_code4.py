# Scrolling

# In older versions of Selenium, scrolling required injecting custom JavaScript 
# (driver.execute_script). In Selenium 4.2+, scrolling is natively built into ActionChains.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/")
time.sleep(1)
actions = ActionChains(driver)
footer_text = driver.find_element(By.XPATH,"//a[@target='_blank']")

actions.scroll_to_element(footer_text).perform()

time.sleep(1)

driver.quit()