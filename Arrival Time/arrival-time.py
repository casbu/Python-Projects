#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 09:18:38 2023

@author: casbu
"""

# This program takes user input variables and converts them into a date-time
# object to calculate the estimated duration of a trip in hours and minutes.

from datetime import datetime, timedelta
    
def calc_travel(departure, miles, mph):
    hours = miles // mph
    r = miles % mph
    minutes = int((r/mph)*60)
    print("Hours: ", hours)
    print("Minute: ", minutes)
    
    arrival = departure + timedelta(hours=hours, minutes=minutes)
    arrival_date = arrival.date()
    arrival_time = arrival.time()
    date_format = "%Y-%m-%d"
    time_format = "%I:%M %p"
    
    print(f"Estimated date of arrival: {arrival_date:{date_format}}")
    print(f"Estimated time of arrival: {arrival_time:{time_format}}")
    print()
    
def main():
    print("Arrival Time Estimator")
    print()
    
    again = "y"
    
    while again.lower() == "y":
        # user inputs
        date_str = input("Enter date of departure (YYYY-MM-DD): ")
        time_str = input("Enter time of departure (HH:MM AM/PM): ")
        miles = int(input("Enter miles: "))
        mph = int(input("Enter miles per hour: "))
        print()
        
        departure = datetime.strptime(date_str + " " + time_str, "%Y-%m-%d %I:%M %p")
        
        #calculate travel time
        calc_travel(departure, miles, mph)
        print()
        print("Estimated travel time")
        print()
        
        again = input("Continue? (y/n): ")
        print()
        
    print("Bye!")
    
if __name__ == "__main__":
    main()