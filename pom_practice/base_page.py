from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)

    def enter_text(self,locator,text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def click_element(self,locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.click()




    