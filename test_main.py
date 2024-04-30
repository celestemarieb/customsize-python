import pytest

from main.py import evaluateFit, createCustomer

def test_evaluateFit(monkeypatch):
    # Given 
    customer_measurements.id_input = '01'
    customer_measurements.customerID = '01'
    customer_measurements.bust = 'dbust' 
    size_measurements.bust = 'dbust' 
    customer_measurements.waist = 'dwaist' 
    size_measurements.waist = 'dwaist'
    customer_measurements.hip = 'dhip'
    size_measurements.hip = 'dhip'

    # When 
    fit = evaluateFit(customer_measurements,size_measurements)

    # Then 
    assert fit == True