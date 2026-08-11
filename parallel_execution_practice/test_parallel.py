# PARALLEL TESTING CHEAT SHEET (THE KITCHEN ANALOGY)
# 🍔 Tests     = Burgers to cook
# 👨‍🍳 Workers   = Chefs cooking simultaneously
# 🔥 CPU Cores = Stoves available in your computer's kitchen
#
# BASIC COMMANDS:
# * pytest -s              -> 1 Chef cooking 1 burger at a time (Sequential / Slow).
# * pytest -n 4            -> Hire exactly 4 Chefs (Safe mode for local machines).
# * pytest -n auto         -> Hire max Chefs based on CPU (Fast mode for Cloud/Servers).
#
# ADVANCED FILE COMMANDS:
# * Run specific files only :
#   pytest test_file_1.py test_file_2.py -n 4
#
# * Run ALL files EXCEPT specific ones (Ignore flag):
#   pytest -n auto --ignore=test_fragile.py --ignore=test_broken.py
#
# * Grouping: Keep tests from the same file together (Same chef cooks the whole book):
#   pytest -n 4 --dist=loadfile
#
# THE GOLDEN RULE:
# Tests MUST be 100% independent! Because workers run at the exact same 
# millisecond, Test B cannot wait for Test A to finish or create data for it.


from selenium import webdriver
import time

def test_google():
    print("\nLaunching Chrome for Google...")
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    time.sleep(3)  # Pausing so you have time to see it open!
    driver.quit()  # Always clean up and close the browser
    assert True

def test_bing():
    print("\nLaunching Chrome for Bing...")
    driver = webdriver.Chrome()
    driver.get("https://www.bing.com")
    time.sleep(3)
    driver.quit()
    assert True

def test_wikipedia():
    print("\nLaunching Chrome for Wikipedia...")
    driver = webdriver.Chrome()
    driver.get("https://www.wikipedia.org")
    time.sleep(3)
    driver.quit()
    assert True

def test_yahoo():
    print("\nLaunching Chrome for Yahoo...")
    driver = webdriver.Chrome()
    driver.get("https://www.yahoo.com")
    time.sleep(3)
    driver.quit()
    assert True