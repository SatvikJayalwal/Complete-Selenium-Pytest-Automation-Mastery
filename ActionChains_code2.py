# Keyboard Combinations

# Sometimes you need to simulate a user holding down CTRL (or COMMAND on Mac) while pressing 
# another key. You achieve this by chaining .key_down() and .send_keys() together.

# NOTE: When using modifier keys, always remember to release them using .key_up(), 
# otherwise Selenium will act as if the key is permanently held down for the rest of the test!


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
driver.maximize_window()
actions = ActionChains(driver)

text_input = driver.find_element(By.XPATH,"//input[@id='my-text-id']")
text_input.send_keys("Testing Action Chains")

actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

time.sleep(1)

textarea = driver.find_element(By.XPATH,"//textarea[@class='form-control']")
textarea.click()

actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()


time.sleep(2)
driver.quit()
