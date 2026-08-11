# Iterating dynamic tables

# Anatomy of an HTML Table
# <table>: The main container for the entire grid.
# <thead>: The header section (contains column names).
# <th>: Table Header cells (e.g., "Name", "Email", "Role").
# <tbody>: The main body where the actual data lives.
# <tr>: Table Row (Horizontal).
# <td>: Table Data / Cell (Vertical columns inside a row).

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/tables")
time.sleep(3)

mytable = driver.find_element(By.ID,"table1")

rows = mytable.find_elements(By.XPATH,"//tbody/tr")

print(f"Found {len(rows)} num of rows")

for row in rows:
    col = row.find_elements(By.TAG_NAME,"td")
    print(col[1].text)



# Send one single command to the browser. The browser's engine searches 
# DOM instantly and clicks the button.
# Reliability: Web pages load dynamically. Looping through elements 
# (Approach A) increases the risk of a StaleElementReferenceException 
# (which happens if the page refreshes or updates slightly while your 
# loop is running).
# Conciseness: Approach B takes one line of code; Approach A takes 
# several.



# parent::tr (or ..): Moves up from the current cell (td) to the entire row (tr). 
# From the row, you can search for anything else inside it.
# following-sibling::td: Searches the cells to the right of your current cell.
# preceding-sibling::td: Searches the cells to the left of your current cell.
dynamic_path_for_edit = "//table[@id='table1']//td[text()='John']/parent::tr//a[text()='edit']"


click_edit = driver.find_element(By.XPATH,dynamic_path_for_edit)
click_edit.click()
print("Edit clicked")


john_email_path = "//table[@id='table1']//td[text()='John']/following-sibling::td[3]"
john_email = driver.find_element(By.XPATH,john_email_path)
print(f"Email of john is : {john_email.text}")

driver.quit()


