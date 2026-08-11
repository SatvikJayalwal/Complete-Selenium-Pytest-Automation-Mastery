# conftest.py

# Pytest has a magical, reserved file name: conftest.py.
# If you create a file exactly named conftest.py and put your fixtures inside it, every single 
# test file in your project can instantly use those fixtures without importing them. You do not 
# need to write from conftest import browser. Pytest detects it automatically.



# SCOPES (How often the fixture runs)
# # - scope="function" (Default): Opens/closes browser for EVERY test (Safest, fresh browser).
# # - scope="module": Opens/closes once per test file.
# # - scope="session": Opens/closes once for the entire test run.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.fixture(scope="session")
def browser():

    driver = webdriver.Chrome()               #SETUP :LAUNCH BROWSER
    yield driver                              #YIELD : HAND DRIVER TO TEST AND PAUSE
    driver.quit()                             #TEARDOWN : CLOSE BROSER AFTER TEST


