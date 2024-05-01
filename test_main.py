import pytest

from main import *
from schema import *

# fit evaluation (customer to size)
# exact match

def test_evaluate_fit():
    # Given 
    customer_measurements = Body ('01','76','58','83.5')
    size_measurements = Size ('UK 4','111','111','76','58','83.5')

    # When 
    fit = evaluate_fit(customer_measurements,size_measurements)

    # Then 
    assert fit == True


def test_evaluate_fit():
    # Given 
    customer_measurements = Body ('01','77','58','83.5')
    size_measurements = Size ('UK 4','111','111','76','58','83.5')

    # When 
    fit = evaluate_fit(customer_measurements,size_measurements)

    # Then 
    assert fit == False