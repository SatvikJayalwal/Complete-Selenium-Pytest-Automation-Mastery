# ActionChains Drag and Drop

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/drag_and_drop")
actions = ActionChains(driver)

boxA = driver.find_element(By.XPATH,"//div[@id='column-a']")
boxB = driver.find_element(By.XPATH,"//div[@id='column-b']")

actions.drag_and_drop(boxA,boxB).perform()
time.sleep(2)
driver.quit()