from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")

username_box = driver.find_element(By.ID,"username")
password_box = driver.find_element(By.ID,"password")

# XPATH .... //tagname[@attribute='value'] 
submit_btn = driver.find_element(By.XPATH,"//button[@id='submit']")