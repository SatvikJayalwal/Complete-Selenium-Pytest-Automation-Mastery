# Sometimes you need to know if your website breaks when a user has a terrible cell phone connection. CDP lets you 
# artificially strangle the browser's internet speed without affecting the rest of your computer.


# ChromeOptions: Changing settings before the browser opens.

# CDP (execute_cdp_cmd): Pressing buttons on a remote control after the browser is already open.


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.execute_cdp_cmd(
    "Network.emulateNetworkConditions",
    {
        "offline": False,
        "latency": 5000,          # 3000 milliseconds = 3 seconds of lag
        "downloadThroughput": 10000, # Super slow download speed
        "uploadThroughput": 10000    # Super slow upload speed
    }
)

print("Attempting to load Google. Prepare to wait...")

driver.get("https://www.google.com")

print("It finally loaded!")
driver.quit()