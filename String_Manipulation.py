# Slicing, Splitting, Regex (re module)

# The Slicing Syntax: string[start : stop : step]
# start: The index where the slice begins (inclusive).
# stop: The index where the slice ends (exclusive).
# step: The increment between each index (defaults to 1).


ui_message = "Order #12345 confirmed"

#print only number
order_num = ui_message[7:12]
print(order_num)

# print only last 9 letters
status = ui_message[-9:]
print(status)


#splitting
my_str = "Satvik,Jayalwal"
my_list_of_str = my_str.split(",")
print(type(my_str))
print(type(my_list_of_str))
print(my_list_of_str)


# replace
price = "$5.98"
replace_in_price = price.replace("98","55")
print(price)
print(replace_in_price)

#strip removes unwanted spaces in end and start

messey_text = "     Hello       "
print(messey_text)
striped_text = messey_text.strip()
print(striped_text)


messy_web_data = "  $10, $20, $30  "
# Step 1: Strip the outside spaces
# Step 2: Replace the spaces next to the numbers
# Step 3: Replace the dollar signs
# Step 4: Split by comma

clean_messy_web_data = messy_web_data.strip().replace(" ","").replace("$","").split(",")
print(clean_messy_web_data)


raw_price = "  $1,299.99  \n"
clean_raw_price = raw_price.strip().replace("$","").replace(",","")
final_price = float(clean_raw_price)
print(raw_price)
print(final_price)


# re example 
import re
pagination_text = "Showing 15 to 30 of 500 entries"

list_of_numbers = re.findall(r'\d+',pagination_text)
print(list_of_numbers)
last_num = int(list_of_numbers[-1])
print(last_num)