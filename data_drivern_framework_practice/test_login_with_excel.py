import pandas as pd
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import configparser


def get_data_from_excel():
    return pd.read_excel("users.xlsx").to_dict(orient="records")


@pytest.mark.parametrize("user", get_data_from_excel())
def test_login_using_excel(user):
    driver = webdriver.Chrome()

    config = configparser.ConfigParser()
    config.read("config.ini")
    target_url = config["QA Testing"]["url"]
    driver.get(target_url)

    user_input = driver.find_element(By.ID, "user-name")
    user_input.send_keys(user["username"])

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(user["password"])

    submit = driver.find_element(By.ID, "login-button")
    submit.click()

    driver.quit()
