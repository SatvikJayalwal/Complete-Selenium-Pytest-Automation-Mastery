# Emulating Mobile

# If you want to test how your website looks on an iPhone, you don't need to plug a real phone into your computer. 
# You can use CDP to instantly force the browser to reshape itself, change its pixel density, and even simulate 
# touchscreen taps instead of mouse clicks.

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.execute_cdp_cmd(
    "Emulation.setDeviceMetricsOverride",
    {
        "width": 300,              
        "height": 800,             
        "mobile": True,            
        "deviceScaleFactor": 3     
    }
)

driver.get("https://www.wikipedia.org/")

time.sleep(500) 
driver.quit()