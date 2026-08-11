# HTML REPORTING 
# 📝 pytest-html = The Health Inspector who hands you a single-page summary 
#                  of passes (perfect burgers) and fails (burned burgers).
#
# SETUP:
# pip install pytest-html
#
# COMMAND QUICK REFERENCE:
# 1. Basic Report (Only works locally on your machine):
#    pytest --html=report.html
# 2. Self-Contained Report (Best Practice for sharing!):
#    pytest --html=report.html --self-contained-html
# 3. Combine with Parallel Execution (Fast execution + Report!):
#    pytest -n auto --html=report.html --self-contained-html
#
# ⚠️ THE GOLDEN RULE / GOTCHA:
# ALWAYS use the `--self-contained-html` flag! If you don't, pytest saves the
# colors/styles in a hidden folder on your computer. If you email the report 
# without that flag, the recipient will just see ugly, broken, plain text.



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