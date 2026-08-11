# JS Alerts (accept, dismiss), Authentication Popups

# Once an alert is on the screen, you use driver.switch_to.alert to take control of it.

# The four Alert Commands:
# alert.accept(): Clicks the "OK" button.
# alert.dismiss(): Clicks the "Cancel" button.
# alert.text: Reads the message displayed on the alert.
# alert.send_keys("text"): Types text into a Prompt alert.

# Types of Alerts (The switch_to.alert interface)

# Alert: Has just an "OK" button. Used for warnings.
# Confirm: Has "OK" and "Cancel" buttons. Used for yes/no choices.
# Prompt: Has a text input box, plus "OK" and "Cancel". Used to gather quick input.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

wait = WebDriverWait(driver,5)

# Normal Alert
click_alert = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Click for JS Alert']")))
click_alert.click()

# NOTE : Best Practice--> Always wait for the alert to fully render before switching to it!

wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
alert.accept()

result = driver.find_element(By.ID,"result")
print(result.text)

#Confirm Alert
click_confirm_alert = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Click for JS Confirm']")))
click_confirm_alert.click()

alert.dismiss()
print(result.text)

# Prompt Alert
click_prompt_alert = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Click for JS Prompt']")))
click_prompt_alert.click()
alert.send_keys("Automation is amazing!")
alert.accept()
print(result.text)

# Authentication Popups (Basic Auth)
# Sometimes you navigate to a website and a grey pop-up drops down from the browser's address 
# bar asking for a Username and Password.

# This is a trap for junior engineers. This is not a JavaScript alert. It is a native browser 
# network authentication prompt (Basic Auth).
# If you try to use driver.switch_to.alert on this, your script will fail because the browser 
# itself is generating the popup, not the DOM.

# The Senior QA Solution: URL Injection
# You bypass this popup entirely by injecting the username and password directly into the URL.

# The Syntax:
# [https://username:password@www.domain.com]

# Real-World Practice: Basic Auth
# [https://the-internet.herokuapp.com/basic_auth]
# The required username is admin and the password is admin.

print("Bypassing the authentication popup with URL injection")
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

authentication_success_msg = wait.until(EC.visibility_of_element_located((By.XPATH,"//p[contains(text(),'Congratulations!')]")))
print(authentication_success_msg.text)

time.sleep(1)
driver.quit()
