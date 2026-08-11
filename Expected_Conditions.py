# clickable, visibility, presence, text_to_be_present

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/dynamic_controls")

wait = WebDriverWait(driver,10)

enable_btn = wait.until(EC.element_to_be_clickable((By.XPATH,"//form[@id='input-example']/button")))
enable_btn.click()

success_text = wait.until(EC.text_to_be_present_in_element((By.XPATH,"//p[@id='message']"), "It's enabled!"))
print(f"{success_text}")

textbox = wait.until(EC.element_to_be_clickable((By.XPATH,"//form[@id='input-example']/input")))
textbox.send_keys("Test completed")

print("Done")

driver.quit()