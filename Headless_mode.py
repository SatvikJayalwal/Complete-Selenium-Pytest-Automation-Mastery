# Why use Headless Mode?
# CI/CD Compatibility: Required for running tests on cloud servers (Jenkins, Docker).
# Speed: Headless tests run slightly faster and consume less CPU/RAM.
# Multitasking: You can continue working on your computer while a suite of 100 tests in background.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options() #create options object
chrome_options.add_argument("--headless=new")
print("Chrome will now run headless")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.com")

print(f"The page launched! The title of the page is {driver.title}")

driver.quit()