#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 15:14:04 2023

@author: casbu
"""

# This program will display 12 months of sales data from a dictionary, calculate 
# the total yearly sales and average monthly sales. Then it allows the user to 
# edit the sales for any month. 
# This program imports the monthly_sales csv file to be read.
# This program implements exception handling for when the CSV file is missing.
# This program will use a dictionary to store data instead of a list.

## ISSUE: unable to read file properly. Was able to successfully move through
##        program before attempting the read method. I'm able to read the file and see
##        the values but I am not transforming it into a dictionary properly. 

import csv

FILENAME = "monthly_sales.txt"

def read_sales():
    sales_dictionary = {}
    try:
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in file:
                row = row.replace("\n", "")
                monthly_sale = row.split("\t")
                sales_dictionary[monthly_sale[0]] = monthly_sale[1]
            return sales_dictionary
        
    except FileNotFoundError:
        print("Could not find the file named", FILENAME)
        
def display_menu():
    print("COMMAND MENU")
    print("------------")
    print("view - View monthly sales")
    print("edit - Edit sales for a month")
    print("totals - View yearly summary")
    print("exit - Exit program")
    print()

def view_monthly_sales(sales_dictionary):
    for month in sales_dictionary:
        print(f"{month}    {sales_dictionary[month]}")

def view_yearly_sales(sales_dictionary):
    total = 0
    
    for month in sales_dictionary:
        try:
            total += int(sales_dictionary[month])
            print(total)
        except TypeError:
            continue
        except ValueError:
            continue
    print("Yearly total:\t" + str(total))
    average = round(total/len(sales_dictionary),2)
    print("Monthly Average:\t", average)
    print()

def edit_sales(sales_dictionary):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    # input month code
    month_code = input("Three-letter Month:\t")
    
    # month code validation
    if month_code not in months:
        print("You did not enter a valid three-letter abbreviation.")
        print()
        month_code = input("Three-letter Month:\t")
    # input sales value
    sales_value = input("Sales Amount:\t")
    
    # modify dictionary item
    sales_dictionary[month_code] = sales_value
    print()

def main():
    print("Monthly Sales Program")
    print()
    display_menu()
    sales_dictionary = read_sales()
    # sales_dictionary = {"Jan": 1000,
    #                     "Feb": 2000,
    #                     "Mar": 3000}
    while True:
        command = input("Command:\t")
        print()
        
        if command == "view":
            view_monthly_sales(sales_dictionary)
            print()
        elif command == "totals":
            view_yearly_sales(sales_dictionary)
        elif command == "edit":
            edit_sales(sales_dictionary)
        elif command == "exit":
            break
        else:
            print("Not a valid option. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()