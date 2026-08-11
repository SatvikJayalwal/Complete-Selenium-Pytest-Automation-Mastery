from selenium import webdriver
import time

def test_google():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    time.sleep(2)
    driver.quit()
    assert True

def test_bing():
    driver = webdriver.Chrome()
    driver.get("https://www.bing.com")
    time.sleep(2)
    driver.quit()
    assert True