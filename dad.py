# student_form = {}

# while True:
#     ask1 = input("Enter student name : ")
#     ask2 = input("Enter student roll : ")

#     student_form[ask1] = ask2

#     print(student_form)


from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "input[id='username']").send_keys("student")
driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys("Password123")
driver.find_element(By.CSS_SELECTOR,"button[id='submit']").click()
time.sleep(1)

