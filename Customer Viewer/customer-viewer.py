#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 17:13:16 2023

@author: casbu
"""

# This program takes a csv file, converts that data to a list, creates objects from this data, and calls data dependant on input attribute value.

import csv
from customer_class import Customer

def read_customers():
    with open('customers.csv') as file:
        reader = csv.reader(file)
        return list(reader)

def create_objects(data):
    customer_list = []
    
    for row in data:
        customer_list.append(Customer(id=row[0],firstName=row[1],lastName=row[2],company=row[3],address=row[4],city=row[5],state=row[6],zip=row[7]))
    return customer_list
    
def get_customer(customer_objects):
    cust_id = input("Enter customer ID: ")
    
    for customer in customer_objects:
        if customer.id == cust_id:
            print()
            customer.getInformation()
            break
    else:
        print("No customer with that ID.")
        

def main():
    print()
    print("Customer Viewer")
    print("Enter the customer ID to view the customer address.")
    print()
    
    data = read_customers()
    customer_objects = create_objects(data)
    get_customer(customer_objects)

    while True:
        print()
        command = input("Continue? (y/n): ")
        
        if command.lower() == 'y':
            print()
            get_customer(customer_objects)
        elif command.lower() == 'n':
            break
        else:
            print("You entered an invalid command.")
    
    print("Bye!")

if __name__ == "__main__":
    main()