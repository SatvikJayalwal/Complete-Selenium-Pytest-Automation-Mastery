# PYTEST SKIPPING (@pytest.mark.skip)

# WHAT IT IS:
# Tells Pytest to completely ignore a test during execution. 
# 
# WHY USE IT:
# When a feature is currently broken (and marked as a bug), or a test is still 
# being written, skipping prevents your test report from failing unnecessarily.
#
# SYNTAX:
# @pytest.mark.skip(reason="JIRA-1234: Image search is currently broken")
#
# TERMINAL COMMAND: pytest test_skips.py -v

import pytest

def test_no_skip():
    print("Doing Wrok...")
    assert True

@pytest.mark.skip(reason="Developers are fixing it")
def test_yes_skip():
    print("This will never print becoz it is skipped using pytest skip marker")
    assert True