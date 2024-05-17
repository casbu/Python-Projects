"""
This module contains functions for calculating the Sales Tax from the sum of items
in the main module. Then returns the Total After Tax.

This function utilizes the global variable:
* Sales Tax

"""

# CONST
SALES_TAX = 0.06

def salesTax(total):
    """
    Accepts total of all item inputs (total argument)
    Rounds sales tax to two decimal places
    Returns sales tax 
    """
    salesTax = total * SALES_TAX
    salesTax = round(salesTax,2)
    return salesTax

def totalAfterTax(total,salesTax):
    """
    Accepts two arguments:
    total and sales tax (total and sales tax arguments)
    Rounds total after tax to two decimal places
    Returns total after tax
    """
    totalAfterTax = total + salesTax
    totalAfterTax = round(totalAfterTax,2)
    return totalAfterTax