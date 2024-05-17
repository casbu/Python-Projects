#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 13:45:01 2023

@author: casbu
"""

# This program manages a task list that's stored in a database.


import database
from business import Task

def display_title():
    print("Task List")
    print()
    display_menu()
    
def display_menu():
    print("COMMAND MENU")
    print("view     - View pending tasks")
    print("history  - View completed tasks")
    print("add      - Add a task")
    print("complete - Complete a task")
    print("delete   - Delete a task")
    print("exit     - Exit program")
    print()

def view_tasks(tasks):
    for task in tasks:
        print(str(task))
    print()

def view_pending_tasks():
    tasks = database.view_tasks()
    view_tasks(tasks)
        
def view_completed_tasks():
    tasks = database.view_history()
    view_tasks(tasks)

def add_task():
    description      = input("Description: ")
    
    task = Task(description=description, completed=0)
    database.add_task(task)   
    print(description + " was added to database.\n")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid whole number. Please try again.\n")

def complete_task():
    taskID = get_int("Task ID: ")
    
    task = Task(taskID=taskID)
    database.update_task(task)
    print("Task ID " + str(taskID) + " was updated.\n")

def delete_task():
    taskID = get_int("Task ID: ")
    
    task = Task(taskID=taskID)
    database.delete_task(task)
    print("Task ID " + str(taskID) + " was deleted from database.\n")

def main():
    database.connect()
    
    display_title()
    
    while True:
        command = input("Command: ")
        if command == "view":
            view_pending_tasks()
        elif command == "history":
            view_completed_tasks()
        elif command == "add":
            add_task()
            pass
        elif command == "complete":
            complete_task()
            pass
        elif command == "delete":
            delete_task()
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
            display_menu()
    database.close()
    print("Bye!")

if __name__ == "__main__":
    main()