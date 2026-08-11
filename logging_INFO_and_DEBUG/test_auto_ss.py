from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_auto_ss():
    
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    time.sleep(1)

    try:
        print("website opened")
        login_btn = driver.find_element(By.ID,"Wrong_path")
        login_btn.click()

    except Exception as e:
        #this method would only take screenshot of this perticular failure and handle it well
        driver.save_screenshot("error_screenshot.png")
        raise e

    finally:
        print("Quiting driver")
        driver.quit()