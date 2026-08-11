from selenium import webdriver
import time 

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()


time.sleep(2)
driver.quit()