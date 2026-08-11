# Shadow_root

# Shadow DOM (shadow_root)
# Modern web frameworks (like Web Components or Salesforce Lightning) use Shadow DOMs. 
# A Shadow DOM is 
# essentially a mini, private HTML document attached to a specific element on the main page.

# The Trap:

# Standard driver.find_element() cannot look inside a Shadow DOM. It acts like a black box.
# XPath is completely unsupported inside a Shadow DOM. You must use CSS Selectors.

# The Strategy for Shadow DOMs
# To interact with an element inside a Shadow DOM, you have to do a two-step breach:

# Locate the Shadow Host (the standard HTML element on the main page that holds the Shadow DOM) using 
# normal locators.
# Extract the .shadow_root property from that host.
# Use find_element() on the shadow root itself (not the driver!) using a CSS Selector.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/shadowdom")

wait = WebDriverWait(driver,5)

wait.until(EC.visibility_of_element_located((By.XPATH,"//h1[contains(text(),'Simple template')]")))

shadow_host = driver.find_element(By.TAG_NAME,"my-paragraph")

shadow_root = shadow_host.shadow_root

hidden_text = shadow_root.find_element(By.CSS_SELECTOR,"p")

print(f"Sucess! The text inside the box is : {hidden_text.text}")

time.sleep(1)
driver.quit()