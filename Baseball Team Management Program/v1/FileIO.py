#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 08:00:06 2023

@author: casbu
"""
import csv

FILENAME = "BaseballPlayers.csv"

def write_lineup(aLineupListVariable):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(aLineupListVariable)
        print("The ", FILENAME, "file was updated.")

def read_lineup():
    aLineupListVariable = []
    try:
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                aLineupListVariable.append(row)
        return aLineupListVariable
        print("The lineup list was updated.")
    except FileNotFoundError:
        print("Could not find the file named", FILENAME)
        sys.exit()