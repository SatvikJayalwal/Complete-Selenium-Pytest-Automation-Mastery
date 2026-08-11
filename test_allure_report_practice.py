# ENTERPRISE REPORTING CHEAT SHEET (THE ALLURE DASHBOARD)
# 📊 Allure = The multi-million dollar restaurant dashboard. Requires a local
#             server to run, but provides beautiful graphs, trends, and logs.
#
# SETUP (One-time only):
# 1. pip install allure-pytest
# 2. scoop install allure (Requires Java/OpenJDK installed via Scoop first)
#
# COMMAND QUICK REFERENCE (The Two-Step Process):
# Step 1: Generate the raw JSON data during your test run
#         pytest --alluredir=allure-results
#
# Step 2: Spin up the local web server to view the dashboard
#         allure serve allure-results
#
# ⚠️ THE GOLDEN RULE / GOTCHA:
# You CANNOT just email the `allure-results` folder to someone. They must also
# have Allure installed on their machine to serve the report, or you must host
# the generated HTML on a real web server (like GitHub Pages or Jenkins).
#
# TO STOP THE SERVER:
# Press Ctrl + C in your terminal when you are done viewing the report.



import time

def test_math_pass():
    # This test will pass
    result = 2 + 2
    assert result == 4

def test_string_pass():
    # This test will pass
    word = "Selenium"
    assert word.upper() == "SELENIUM"

def test_burn_the_burger():
    # This test will FAIL intentionally so we can see the error in the report
    result = 10 * 2
    assert result == 999  # 20 does not equal 999!