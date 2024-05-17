#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 11:09:48 2023

@author: casbu
"""

# This program stores user input into Customer and Employee subclasses of Person, stores each Person into the company_list variable, and prints the subclass stored.

from company_objects import Person, Customer, Employee

def createPerson(company_list):
    while True:
        command = input("Customer or employee? (c/e): ")
        print()
        
        print("DATA ENTRY")
        firstName = input("First Name: ")
        lastName = input("Last Name: ")
        email = input("Email: ")
        
        if command == "c":
            number = input("Number: ")
            person_object = Customer(firstName=firstName, lastName=lastName, email=email, number=number)
            break
        elif command == "e":
            ssn = input("SSN: ")
            person_object = Employee(firstName=firstName, lastName=lastName, email=email, ssn=ssn)
            break
        else:
            print("Not a valid option. Please try again.\n")
    
    company_list.append(person_object)
    show_person(person_object)

    
def show_person(person_object):
    customerString = ""
    employeeString = ""
    personString = ""
    print()
    if isinstance(person_object, Customer):
        print("CUSTOMER")
        customerString += (str(person_object) + "\n")
        print(customerString)
    elif isinstance(person_object, Employee):
        print("EMPLOYEE")
        employeeString += (str(person_object) + "\n")
        print(employeeString)
    else:
        print("PERSON")
        personString += (str(person_object) + "\n")
        print(personString)
        
def main():
    print("Customer/Employee Data Entry")
    print()
    
    company_list = []
    
    createPerson(company_list)
    
    while True:
        command = input("Continue? (y/n): ")
        if command == "y":
           createPerson(company_list)
        elif command == "n":
            break
        else:
            print("Not a valid option. Please try again.\n")
            command = input("Continue? (y/n): ")
            print()
    
    print("Bye!")
    
if __name__ == "__main__":
    main()
