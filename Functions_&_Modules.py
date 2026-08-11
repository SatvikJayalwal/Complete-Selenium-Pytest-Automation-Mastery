# def, parameters, *args, **kwargs, return, Lambda, custom modules

def welcome_message():
    print("Welcome to the selenium")

def get_discounted_price(original_price,discount):
    final_price = original_price-discount
    return final_price

welcome_message()
values = get_discounted_price(100,20)
print(f"the discounted price is {values}")


#parameters

def login_to_portal(username,browser="Chrome"):
    print(f"Logging in {username} using {browser}")

login_to_portal("Admin_user")
login_to_portal("test_user","brave")

#args - use when you do not know how many arguments you need to pass to a function
# The * gathers multiple positional arguments into a Tuple.

def sum_of_all_prices(*args): #args is treated as a tuple
    total = 0 
    for price in args:
        total+=price
    return total

print(sum_of_all_prices(10,20,30,40))


# The ** gathers multiple keyword arguments into a Dictionary

def configure_browser(**kwargs):
    #kwargs is treated as a dictionary
    for key,value in kwargs.items():
        print(f"setting {key} to {value}")

configure_browser(headless=True,maximize=True,incognito=False)


# Lambda functions
#one-line function that does not have a name used when you need a simple function 
# for a short period of time

#Syntax: lambda arguments: expression

#NORMAL FUNCTION 
def square_number(x):
    return x*x

#LAMBDA FUNCTION
square_lambda = lambda x : x*x
print(square_lambda(5))



#calling modules
# Approach 1: Import the whole module
import wait_helpers
wait_helpers.wait_for_element()

# Approach 2: Import specific functions (Most Common)
from wait_helpers import wait_for_element, wait_for_page_load
wait_for_element()

# Approach 3: Import everything using * (Not recommended, can cause naming conflicts)
from wait_helpers import *
wait_for_page_load()