from selenium import webdriver
import time

def test_python_org():
    driver = webdriver.Chrome()
    driver.get("https://www.python.org")
    time.sleep(2)
    driver.quit()
    assert True

def test_selenium_dev():
    driver = webdriver.Chrome()
    driver.get("https://www.selenium.dev")
    time.sleep(2)
    driver.quit()
    assert True