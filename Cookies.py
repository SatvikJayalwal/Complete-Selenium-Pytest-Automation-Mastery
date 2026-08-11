# Cookies

# ==========================================
# COOKIE MANAGEMENT (FAST LOGIN BYPASS)
# ==========================================
# Cookies are small pieces of data stored in your browser. The most important cookie is the 
# Session Cookie. When you log into a website, the server gives you a session cookie. As long 
# as you have that cookie, the website knows you are logged in.

# The Senior QA Trick: Instead of making Selenium type in a username and password for every 
# single test (which takes 5-10 seconds), you can instantly inject a valid session cookie 
# directly into the browser and refresh the page. Boom—you are instantly logged in!

# CORE COMMANDS:
# driver.get_cookies()            -> Returns a list of all cookies for the domain
# driver.get_cookie("name")       -> Returns a specific cookie dictionary
# driver.add_cookie({"name": "k", "value": "v"}) -> Injects a cookie (Logs you in!)
# driver.delete_cookie("name")    -> Deletes a specific cookie
# driver.delete_all_cookies()     -> Wipes browser clean (Instant Logout)
# ==========================================


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

wait = WebDriverWait(driver,10)

wait.until(EC.visibility_of_element_located((By.XPATH,"//div[contains(text(),'Swag Labs')]")))

driver.add_cookie({"name" : "session-username", "value" : "standard_user"})

driver.get("https://www.saucedemo.com/inventory.html")
wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='app_logo']")))

driver.delete_all_cookies()
driver.get("https://www.saucedemo.com/inventory.html")


time.sleep(1)
driver.quit()


