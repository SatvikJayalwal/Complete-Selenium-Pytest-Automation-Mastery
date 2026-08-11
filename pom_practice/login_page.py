from selenium import webdriver
from selenium.webdriver.common.by import By
from base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID,"user-name")
    PASSWORD_INPUT = (By.ID,"password")
    SUBMIT_INPUT = (By.ID,"login-button")

    def open_page(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self,username,password):
        self.enter_text(self.USERNAME_INPUT,username)
        self.enter_text(self.PASSWORD_INPUT,password)
        self.click_element(self.SUBMIT_INPUT)