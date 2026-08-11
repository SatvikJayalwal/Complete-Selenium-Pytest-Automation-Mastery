# try/except/finally, Custom Exceptions, File I/O (.txt, .csv, .json, .xlsx)

# Exception handling catch error, log it and decide what to do next without crashing 

# try: The block of code you want to execute that might fail.
# except: The block of code that runs only if the try block fails. You can specify exactly which error to catch.
# finally: The block of code that runs no matter what (whether the try block succeeded or failed).

# Selenium Context: You will use this to catch 
# NoSuchElementException or TimeoutException and take a screenshot before ending the test


try:
    print("Trying to do some math")
    answer = 10/0
    print(f"The answer is {answer}")

except:
    print("Oops! Something went wrong, but the program did not crash!")

finally:
    print("Done with the math test!")



from selenium.common.exceptions import NoSuchElementException

try:
    print("---------Initiating the test----------")
    ans = 10/0
    print(f"Your answer is {ans}")

except NoSuchElementException:
    print("OOPS! Could not find the login btn")

except ZeroDivisionError:
    print("OOPS! Cant divide by 0")

finally:
    print("Done with the test")


#raise exception 
#for raising unexpected custom errors 
account_balance = 500
if account_balance<0:
    raise Exception(f"Test failed. The account balance {account_balance} is less than 0")

print("this line will not print if the error occurs")

# File I/O (File Input/Output)
# Golden Rule of File I/O: Always use the with statement
# It automatically closes the file when work done, even if an error occurs. 
# If you leave files open, your framework will run out of memory.

#txt
with open("dummy.txt","r") as file:
    content = file.read()
    print(content)

#csv
import csv
with open("dummy2.csv","r") as file:
    csv_content = csv.DictReader(file)

    for row in csv_content:
        print(row)


#json
import json
with open("dummy3.json","r") as file:
    json_content = json.load(file)
    print(json_content)


#xlsx
import openpyxl
workbook = openpyxl.load_workbook("dummy4.xlsx")
sheet = workbook.active
cell_value = sheet.cell(row=2,column=1).value
print(f"the first user is {cell_value}")

for the_row in sheet.iter_rows(values_only = True):
    print(the_row)


    