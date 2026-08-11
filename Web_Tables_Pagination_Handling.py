# Pagination handling

# Pagination Handling (The while Loop)
# What if "John Doe" is on page 4 of the table? If you just scrape the first page, your test 
# will fail. You must build a script that reads the table, checks for your target, and if it 
# is not there, clicks the "Next Page" button until it finds it or runs out of pages.

# This requires a Python while loop.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://datatables.net/examples/basic_init/zero_configuration.html")
time.sleep(2)

page_num = 1
while True :
    print(f"----Searching page {page_num}----")
    name_elements = driver.find_elements(By.XPATH,"//table[@id='example']/tbody/tr/td[1]")

    for name in name_elements:
        print(name.text)

    next_btn = driver.find_element(By.XPATH,"//button[@data-dt-idx='next']")

    if "disabled" in next_btn.get_attribute("class"):
        print("\nReached the last page. Pagination complete!")
        break 

    next_btn.click()

    page_num +=1

    time.sleep(1)

driver.quit()