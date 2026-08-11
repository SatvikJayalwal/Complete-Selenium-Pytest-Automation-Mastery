# find_elements() vs find_element(), Iterating lists

# find_element() (Singular)
# It returns: A single WebElement object.
# If multiple match: Returns only the first one it finds on the DOM & ignores the rest.
# If ZERO match: Crashes the script and throws a NoSuchElementException.

# find_elements() (Plural)
# It returns: A Python List [] containing multiple WebElement objects.
# If multiple match: Returns all matching elements inside the list.
# If ZERO match (Important!): Does not crash. Simply returns an empty Python list: [].


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
time.sleep(3)

product_titles = driver.find_elements(By.CLASS_NAME,"card-title")
length_of_list = len(product_titles)
print(f"Found {length_of_list} products")

count = 0

for product in product_titles:

    # (to print all products)    
    # print(f"The product number {count} is : {product.text}") 
    # count += 1

    #to print a specific product
    if count==2:
        print(f"The product number {count+1} is : {product.text}")
        break
    count += 1

driver.quit()