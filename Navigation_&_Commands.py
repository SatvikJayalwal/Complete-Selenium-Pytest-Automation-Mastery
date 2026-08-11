# get(), back(), forward(), refresh(), title, window sizing, close vs quit

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.google.com")
print(f"The title of the page is : {driver.title}")
print(f"The current url is : {driver.current_url}")

time.sleep(1)

driver.get("https://www.wikipedia.org/")
print(f"The title of the page is {driver.title}")
print(f"The current url is : {driver.current_url}")

time.sleep(1)

driver.back()
driver.minimize_window()
time.sleep(2)

driver.fullscreen_window()
driver.refresh()
time.sleep(1)

driver.maximize_window()
driver.forward()
time.sleep(1)


driver.get("https://www.youtube.com/")
driver.set_window_position(375,500)
time.sleep(1)

driver.get("https://www.python.org")
driver.fullscreen_window()
print(f"The page source is : {driver.page_source}")
time.sleep(1)

driver.quit()   