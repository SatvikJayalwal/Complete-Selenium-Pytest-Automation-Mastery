# Geolocation 
# ChromeOptions: Changing settings before the browser opens.

# CDP (execute_cdp_cmd): Pressing buttons on a remote control after the browser is already open.

# Geolocation Spoofing (Teleportation)
# The Concept: Your browser asks your computer where you are physically located. Using CDP, we 
# can intercept that request and feed it fake GPS coordinates.
# Let's teleport your browser to Tokyo, Japan.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()


driver.execute_cdp_cmd(
    "Emulation.setGeolocationOverride",
    {
        "latitude": 35.6762,   # Tokyo Latitude
        "longitude": 139.6503, # Tokyo Longitude
        "accuracy": 100
    }
)
driver.get("https://the-internet.herokuapp.com/geolocation")

driver.find_element(By.TAG_NAME, "button").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[contains(text(),'See')]").click()
time.sleep(5)

driver.quit()