#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 13:45:53 2023

@author: casbu
"""

class Task:
    def __init__(self, taskID=1, description=None, completed=0):
        self.taskID = taskID
        self.description = description
        self.completed = completed
        
    def __str__(self):
        if self.completed != 1:
            return f"{self.taskID}. {self.description}"
        else:
            return f"{self.taskID}. {self.description} (DONE!)"