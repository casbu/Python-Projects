#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 08:15:37 2023

@author: casbu
"""
# Cass Burleson
# July 6, 2023
# This program calculates sales by row(region) and column(quarter) from a list of lists (sales), 
# prints totals for each, as well as calculates total for entire sales list. 

import locale as lc
lc.setlocale(lc.LC_ALL, "en_US")

DASHES = "-" * 60

def display_sales(sales):
    i = 0
    
    print(f"{'Region':9} {'Q1':>10} {'Q2':>10} {'Q3':>10} {'Q4':>10}")
    
    for row in sales:
        i += 1
        currency_sales = [lc.currency(sale, grouping=True) for sale in row]
        print(f"{i:<10} {currency_sales[0]:10} {currency_sales[1]:10} {currency_sales[2]:10} {currency_sales[3]:10}")
    print(DASHES)
        
def total_sales_by_region(sales):
    print("Total Sales by region:")
    i = 0
    for row in sales:
        total = 0
        for sale in row:
            total += sale
        i += 1
        total = lc.currency(total, grouping=True)
        print(f"Region {i}: {total}")
    print(DASHES)
    
def total_sales_by_quarter(sales):
    print("Total Sales by quarter:") 
    i = 0
    for quarter_sales in zip(*sales):
        total = 0
        i += 1
        total += sum(quarter_sales)
        total = lc.currency(total, grouping=True)
        print(f"Q{i}: {total}")
    print(DASHES)
    
def total_annual_sales(sales):
    for row in sales:
        total = 0
        total += sum(row)
    total = sum(sum(row) for row in sales)
    total = lc.currency(total, grouping=True)
    print(f"Total annual sales, all regions: {total}")

def main():
    print(DASHES)
    print("Sales Report")
    print(DASHES)
    
    sales = [[1540.0, 2010.0, 2450.0, 1845.0], # Region 1
            [1130.0, 1168.0, 1847.0, 1491.0], # Region 2
            [1580.0, 2305.0, 2710.0, 1284.0], # Region 3
            [1105.0, 4102.0, 2391.0, 1576.0]] # Region 4
       
    display_sales(sales)
    total_sales_by_region(sales)
    total_sales_by_quarter(sales)
    total_annual_sales(sales)

if __name__ == "__main__":
    main()