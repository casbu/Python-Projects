#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 11:09:51 2023

@author: casbu
"""

class Person:
    def __init__(self, firstName="", lastName="", email=""):
      self.__firstName = firstName
      self.__lastName = lastName
      self.__email = email

    def getFirstName(self):
        return self.__firstName
    def setFirstName(self):
        self.__firstName = firstName
    def getLastName(self):
        return self.__lastName
    def setLastName(self):
        self.__lastName = lastName
    def getEmail(self):
        return self.__email
    def setEmail(self):
        self.__email = email
    def getFullName(self):
        return "Full Name: " + self.getFirstName() + " " + self.getLastName() + "\n"
    def getInfo(self):
        return f"Email: {self.getEmail()}"
    def __str__(self):
        return self.getFullName() + self.getInfo()
    
    
class Customer(Person):
    def __init__(self, firstName="", lastName="", email="", number=""):
        Person.__init__(self, firstName, lastName, email)
        self.__number = number
    def getNumber(self):
        return self.__number
    def setNumber(self):
        self.__number = number
    def getInfo(self):
        return f"{Person.getInfo(self)} \nNumber: " + self.__number

class Employee(Person):
    def __init__(self, firstName="", lastName="", email="", ssn=""):
        Person.__init__(self, firstName, lastName, email)
        self.__ssn = ssn
    def getSSN(self):
        return self.__ssn
    def setSSN(self):
        self.__ssn = ssn
    def getInfo(self):
        return f"{Person.getInfo(self)} \nSSN: " + self.__ssn

