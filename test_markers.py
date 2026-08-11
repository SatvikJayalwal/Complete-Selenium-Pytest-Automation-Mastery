# Tagging / Custom Markers (@pytest.mark.smoke)

# QUICK RECALL: PYTEST MARKERS & TAGGING (@pytest.mark.<tag_name>)

# WHAT IT IS:
# Tagging allows you to categorize ("hashtag") your tests so you can choose 
# exactly which group of tests to execute from the command line.
#
# THE HASHTAG ANALOGY:
# If you have 1,000 tests and a developer makes a tiny update, running all 1,000 
# might take hours. You tag your 10 most critical tests with @pytest.mark.smoke 
# and tell Pytest to ONLY run those 10 tests to verify nothing is "on fire."
#
# COMMON TAG NAMES (You can invent any tag name you want):
# - @pytest.mark.smoke      --> Fast, critical core functionality tests
# - @pytest.mark.regression --> Comprehensive, full deep-dive test suite
# - @pytest.mark.ui         --> Interface, layout, and visual checks
#
# SYNTAX EXAMPLE:
# @pytest.mark.smoke
# @pytest.mark.ui
# def test_homepage():
#     ...
# (Note: You can stack multiple markers on a single test function!)
#
# CLI COMMANDS TO RUN (Terminal):
# - pytest filename.py -m smoke           --> Runs ONLY tests tagged with 'smoke'
# - pytest filename.py -m regression      --> Runs ONLY tests tagged with 'regression'
# - pytest filename.py -m "smoke and ui"  --> Runs tests that have BOTH tags
# - pytest filename.py -m "not smoke"     --> Runs everything EXCEPT 'smoke' tests
#
# REGISTERING MARKERS (Optional - To remove the yellow warning):
# Create a file named `pytest.ini` in your project root folder and add:
#   [pytest]
#   markers =
#       smoke: Critical smoke tests
#       regression: Full regression test suite


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.mark.smoke
def test_smoke_marker():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://duckduckgo.com/")
    title_page = driver.title
    assert driver.title == title_page

@pytest.mark.regression
def test_regression_marker():
    print("Doing regression")

@pytest.mark.ui 
def test_ui_marker():
    print("Doing UI")