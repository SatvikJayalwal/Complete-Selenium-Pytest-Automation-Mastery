# Switching by index/name/id, nested iframes, default_content

# SELENIUM IFRAME NOTES

# --- THE IFRAME TRAP ---
# - iFrames are entirely separate webpages embedded in the main page.
# - Selenium ONLY sees the main DOM by default.
# - Trying to find an element inside an iFrame without switching throws NoSuchElementException.

# --- 1. ENTERING AN IFRAME ---
# Must explicitly step into the iFrame.

# Method A: By ID or Name (BEST)
# driver.switch_to.frame("frame_id")

# Method B: By WebElement (FLEXIBLE - Use when no ID/Name exists)
# iframe_element = driver.find_element(By.CSS_SELECTOR, "iframe.custom-frame")
# driver.switch_to.frame(iframe_element)

# Method C: By Index (RISKY - Breaks easily if DOM structure changes)
# driver.switch_to.frame(0) 

# --- 2. ESCAPING AN IFRAME ---
# Selenium is blind to the main page until you step back out.

# Master Reset: Jumps all the way out to the primary webpage DOM
# driver.switch_to.default_content()

# Step Back: Moves up exactly one level (Useful for nested iFrames)
# driver.switch_to.parent_frame()

# --- 3. PRACTICE SCENARIO ---
# Target: https://the-internet.herokuapp.com/iframe (WYSIWYG Editor)
# Flow: 
# 1. Navigate to URL.
# 2. Step into iFrame.
# 3. Clear default text & write new message.
# 4. Step back out using default_content().
# 5. Read main page header to verify escape.



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://letcode.in/frame/")

wait = WebDriverWait(driver,10)

wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID,"firstFr")))

parent_frame_name = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@name='fname']")))

parent_frame_name.clear()
parent_frame_name.send_keys("Satvik")

inner_iframe = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
driver.switch_to.frame(inner_iframe)

email_box = wait.until(EC.element_to_be_clickable((By.NAME, "email")))
email_box.send_keys("test@gmail.com")

driver.switch_to.default_content()

main_header = wait.until(EC.visibility_of_element_located((By.XPATH,"//h1[contains(text(),'Frame')]")))
print(f"{main_header.text}")


time.sleep(2)
driver.quit()