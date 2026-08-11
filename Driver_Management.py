# Selenium 4 Manager, Launching Browsers

from selenium import webdriver
import time

driver = webdriver.Chrome() #triggers Selenium Manager to download the driver and launch Chrome

driver.get("https://www.google.com")
print("Google launched !")
time.sleep(2)
driver.quit()



