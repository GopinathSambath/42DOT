import pytest
from Diag_Automation import main,request1,request2,request3
from io import StringIO
import sys


def test_Diag_Request_one():
    try:
        main()
        request1()

    except Exception as e:
        pytest.fail(f"Test failed due to an exception: {str(e)}")

def test_Diag_Request_two():
    try:
        request2()

    except Exception as e:
        pytest.fail(f"Test failed due to an exception: {str(e)}")

def test_Diag_Request_Three():
    try:
        request3()

    except Exception as e:
        pytest.fail(f"Test failed due to an exception: {str(e)}")




