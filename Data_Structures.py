# Lists, Tuples, Dictionaries, Sets, Comprehensions

browsers = ["safari","brave","chrome"] #list are mutable/changable
print(browsers)
browsers.append("firefox")
browsers.remove("safari")
print(browsers)

# Tuples
login_locators = ("ID","user_login")
print(login_locators[1])

# Dictionary 
test_user = {
    "username" : "satvik",
    "password" : "xyz",
    "isAdmin" : True
}

print(test_user["username"])
#update something in dict
test_user["username"] = "Satvik Jayalwal"
print(test_user["username"])

#Sets
my_list=[1,2,3,4,4,4,5,6,7,8,8,9]
my_set=set(my_list)
print(my_list)
print(my_set)

#comprehensions 
web_elements = ["<ElementA>","<ElementB>","ElementC"]
element_texts = [element + "_TEXT" for element in web_elements]
print(element_texts)