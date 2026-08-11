import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest 

logging.basicConfig(
    filename="test_runner.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)

def test_login_button_display():

    driver = webdriver.Chrome()

    logging.info("Starting test, launching saucedemo website")
    driver.get("https://www.saucedemo.com/")

    logging.info("Maximizing window of saucedemo website")
    driver.maximize_window()

    logging.info("Checking if login button is displayed or not")
    lgn_btn = driver.find_element(By.ID,"login-button")
    assert lgn_btn.is_displayed()

    logging.debug("The login button color is #3CDB81.")

    logging.info("Exit website")
    driver.quit()