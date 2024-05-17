#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 15:21:14 2023

@author: casbu
"""

import sqlite3
from contextlib import closing

from business import Task

conn = None

def connect():
    global conn
    if not conn:
        DB_FILE = "task_list_db.sqlite"
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row

def close():
    if conn:
        conn.close()

def make_task(row):
    return Task(row["taskID"], row["description"], row["completed"])

def view_tasks():
    # execute SELECT statement - with exception handling
    try:
        query = '''SELECT * FROM Task 
                    WHERE completed = 0'''
        with closing(conn.cursor()) as c:
            #! comma is necessary when we have single query variable
            c.execute(query)
            results = c.fetchall()
            
        tasks = []
        for row in results:
            tasks.append(make_task(row))
        return tasks
            
    except sqlite3.OperationalError as e:
        task = None
        print("Error reading database -", e)

def view_history():
    # execute SELECT statement - with exception handling
    try:
        query = '''SELECT * FROM Task 
                    WHERE completed = 1'''
        with closing(conn.cursor()) as c:
            #! comma is necessary when we have single query variable
            c.execute(query)
            results = c.fetchall()
            
        tasks = []
        for row in results:
            tasks.append(make_task(row))
        print()
        return tasks
            
    except sqlite3.OperationalError as e:
        task = None
        print("Error reading database -", e)

def add_task(task):
    sql = '''INSERT INTO Task (description, completed) 
             VALUES (?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (task.description, task.completed))
        conn.commit()

def update_task(task):
    # execute UDPATE statement
    sql = '''UPDATE Task
                SET completed = 1
                WHERE taskID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (task.taskID,))
        conn.commit()

def delete_task(task):
    # execute DELETE FROM statement
    sql = '''DELETE FROM Task 
            WHERE taskID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (task.taskID,))
        conn.commit()