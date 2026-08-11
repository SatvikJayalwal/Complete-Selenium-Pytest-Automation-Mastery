from selenium import webdriver
import time 

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()

page1title = driver.title
print(page1title)
current_url_1= driver.current_url
print(current_url_1)

driver.get("https://www.geeksforgeeks.org")
page2title=driver.title
print(page2title)
current_url_2= driver.current_url
print(current_url_2)

driver.back()
driver.forward()
driver.refresh()

time.sleep(2)
driver.quit()