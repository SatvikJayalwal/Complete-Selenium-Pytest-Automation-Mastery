# window_handles, switch_to.window, opening new tabs

# Just like with iFrames, when a link opens a completely new tab, Selenium does not 
# automatically switch to it. Your script will remain focused on the original tab, and if you 
# try to interact with the new one, it will fail.


# ==========================================
# 1. WINDOW HANDLES IN SELENIUM
# ==========================================
# Tabs are assigned unique, dynamic IDs (Window Handles), not names.
# - driver.current_window_handle -> Returns ID of the currently focused tab.
# - driver.window_handles -> Returns a List [] of all open tab IDs.

# ==========================================
# 2. LOGIC FOR SWITCHING TABS
# ==========================================
# IDs are randomly generated every run; NEVER hardcode them.

# Standard switching pattern:

# Step 1: Save the current tab ID
# original_tab = driver.current_window_handle

# Step 2: Perform action that opens the new tab (e.g., click)

# Step 3: Get the list of all open tabs
# all_tabs = driver.window_handles

# Step 4: Loop through and switch to the new one
# for tab in all_tabs:
#     if tab != original_tab:
#         driver.switch_to.window(tab)
#         break


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")

wait = WebDriverWait(driver,10)

original_tab_id = driver.current_window_handle

click_for_new_tab = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@href='/windows/new']")))
click_for_new_tab.click()

all_tab_id = driver.window_handles

for tab in all_tab_id :
    if tab != original_tab_id :
        driver.switch_to.window(tab)
        text_of_new_tab = wait.until(EC.visibility_of_element_located((By.XPATH,"//h3[text()='New Window']")))
        print(text_of_new_tab.text)
        break

time.sleep(1)

#switching to new tab 
driver.switch_to.new_window('tab')
driver.get("https://www.wikipedia.org/")

time.sleep(1)

driver.quit()

