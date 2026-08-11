# PYTEST ORDERING (@pytest.mark.run)

# Forces Pytest to execute tests in a specific numeric order, rather than the 
# default alphabetical order.
# 
# PREREQUISITE:
# You must install the plugin via terminal: pip install pytest-ordering
#
# SYNTAX:
# @pytest.mark.run(order=1) 
# (Negative numbers like order=-1 mean "run this absolutely last")
#
# TERMINAL COMMAND: pytest test_ordering.py -v -s


import pytest

@pytest.mark.run(order=2)
def test_edit_user():
    print("This will run second.")

@pytest.mark.run(order=1)
def test_create_user():
    print("This will run first, regardless of where it is in the file!")

@pytest.mark.run(order=-1)
def test_delete_user():
    print("Negative numbers mean run at the very end. This runs last.")