#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 17:14:16 2023

@author: casbu
"""

class Customer:
    def __init__(self, id, firstName, lastName, company, address, city, state, zip):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.company = company
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        
    def getInformation(self):
        fullAddress = return self.firstName + " " + self.lastName + "\n" + self.company + "\n" + self.address + "\n" + self.city + ", " + self.state + " " + self.zip
        
        if self.company != "":
            return fullAddress += self.company + "/n"
        else:
            return fullAddress