# Explicit_Waiting_WebDriverWait

# Explicit Wait (WebDriverWait) 
# Instead of a global rule, you tell Selenium to wait for a specific condition to occur on a specific element before moving forward.

# To use them, you must import WebDriverWait and expected_conditions (usually aliased as EC to save typing).

# Common Expected Conditions:
# EC.visibility_of_element_located: Waits until the element is physically visible on the screen.
# EC.element_to_be_clickable: Waits until the element is visible AND enabled (not greyed out).
# EC.presence_of_element_located: Waits until it exists in the HTML (like Implicit wait).
# EC.invisibility_of_element_located: Waits for a loading spinner or popup to disappear.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

wait = WebDriverWait(driver,10)

start_btn = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@id='start']/button")))
start_btn.click()

delayed_text = wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@id='finish']")))
print(f"Sucess found text : {delayed_text.text}")

driver.quit()