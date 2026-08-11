# By.ID, By.NAME, By.CLASS_NAME, By.TAG_NAME, By.LINK_TEXT

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
time.sleep(1)

# By.ID
username = driver.find_element(By.ID,"user-name").send_keys("satvik")
time.sleep(1)

# By.NAME
password = driver.find_element(By.NAME,"password").send_keys("123456")
time.sleep(1)

# By.CLASS_NAME
changed_username = driver.find_element(By.CLASS_NAME,"form_input").clear()
changed_username = driver.find_element(By.CLASS_NAME,"form_input").send_keys("Satvik Jayalwal")
time.sleep(1)

# TAG_NAME
driver.find_element(By.TAG_NAME,"input").click()
time.sleep(1)

driver.get("https://www.apple.com/in/")
time.sleep(2)

# By.LINK_TEXT
driver.find_element(By.LINK_TEXT,"Shop").click()
time.sleep(1)

driver.quit()