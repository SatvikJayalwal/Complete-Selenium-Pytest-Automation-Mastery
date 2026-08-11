# Parameterization 

# Data-Driven Testing (DDT). It allows you to write a single test function 
# and run it multiple times with different sets of data. This prevents code 
# duplication (e.g., writing 50 separate tests for 50 different search words).
#
# THE CALCULATOR ANALOGY:
# If you are testing a calculator, you don't write one test for 2+2=4, a 
# separate test for 5+5=10, and a third test for 10+20=30. You write ONE test 
# that says "Check if Number A + Number B = Total" and feed it a list of numbers.
#
# THE "BUCKET" CONCEPT (How the Syntax Works):
#
# @pytest.mark.parametrize("word, title", [
#     ("dog", "dog at DuckDuckGo"),  <-- Run 1
#     ("cat", "cat at DuckDuckGo")   <-- Run 2
# ])
#
# 1. The first string ("word, title") creates empty "buckets" (variables).
# 2. The list of tuples contains the data to fill those buckets.
# 3. On Run 1: Pytest puts "dog" into the 'word' bucket and "dog at DuckDuckGo" 
#    into the 'title' bucket, then runs the test.
# 4. On Run 2: Pytest empties the buckets, fills them with the "cat" data, 
#    and runs the test again.


from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from selenium.webdriver.common.keys import Keys

@pytest.mark.parametrize("word,title",[
    ("dog","dog at DuckDuckGo"),
    ("cat","cat at DuckDuckGo")
])

def test_search(word,title):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://duckduckgo.com/")

    text_box = driver.find_element(By.NAME,"q")
    text_box.send_keys(word)
    text_box.send_keys(Keys.ENTER)
    print("Text Entered")
    time.sleep(2)

    assert driver.title == title, "Wrong title"
    print("Assertion passed, Correct Title")

    driver.quit()
