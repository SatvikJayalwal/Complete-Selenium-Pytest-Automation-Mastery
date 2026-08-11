# "Hey Pytest, wrap yourself around my tests. After a test finishes, pause and get the report 
# card. If the test was in the middle of running and it failed, find the exact web browser that 
# test was using, and use it to take a screenshot named after the test."


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("browser")

        if driver:
            driver.save_screenshot(f"{item.name}_failed.png")
