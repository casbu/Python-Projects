#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 16:01:54 2023

@author: casbu
"""

# This program manages a team by storing data in a list of players. Data is stored in a text file.
# This program adds IO functionality, importing the BaseballPlayers csv file, which is called from the FileIO module. 

import FileIO as IO
import copy
import sys

## CONST
CROSSES = "+" * 50
DIVIDER = "-" * 50
positions = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")

        
def display_menu():
    print(CROSSES)
    print("        Baseball Team Management Program")
    print()
    print("MENU OPTIONS")
    print("1 - Display lineup")
    print("2 - Add player")
    print("3 - Remove Player")
    print("4 - Move player")
    print("5 - Edit player position")
    print("6 - Edit player stats")
    print("7 - Exit program")
    print()

def display_positions(positions):
    print("POSITIONS")
    print(*positions, sep=", ")
    
def display_lineup(aLineupListVariable):
    i = 0
    print("    Player     POS   AB    H    AVG")
    print(DIVIDER)
    for row in aLineupListVariable:
        i += 1
        print(f"{i}   " + "{: <10} {: <5} {: <5} {: <5}".format(*row))
    
    # averages tuple
    # I can't figure out how to call this variable in display_menu. 
    # I'm wanting to zip playerAverages with aPlayerVariable
    # I am also not sure where to place it...maybe in main? so it can be called in the display lineup?
    # try:
    #     average = round(hits/at_bats,3)
    # except ZeroDivisionError:
    #     average = 0
    # playerAverages = [average]
    
    # for stat, average in zip (aPlayerListVariable, playerAverages):
    #     # print lineup zipped with playerAverages
        
def add_player(aLineupListVariable):
    # inputs for inner list
    name = input("Name: ")
    position = input("Position: ")
    if position not in positions:
        print("That is not a valid position. Try again.")
        print(DIVIDER)
        print("Valid positions: ", *positions)
        print(DIVIDER)
        position = input("Position: ")
    # position validation
    while True:
        if position in positions:
            
            check = position in (stat for aPlayerListVariable in aLineupListVariable for stat in aPlayerListVariable)
            
            if check == True:
                print("This position is already filled.")
                position = input("Enter a new position:\t")
            else: break
        else:
            print("You did not enter a valid position.")
            position = input("Enter a new position:\t")
            
    # at_bats validation
    while True:
        at_bats = input("At bats: ")
        try:
            at_bats = int(at_bats)
            
            if at_bats < 0:
                print("Your at bats cannot be less than 0.")
                continue
            else: 
                break
            
        except ValueError:
            print("Value must be an integer.")
            continue
        
    # hits validation
    while True:
        hits = input("Hits: ")
        try:
            hits = int(hits)
            
            if hits < 0:
                print("Your hits cannot be less than 0.")
                continue
            elif hits > at_bats:
                print("Hits cannot be greater than at bats.")
                continue
            else:
                break
        except ValueError:
            print("Value must be an integer.")
    
    # create inner list
    aPlayerListVariable = [name, position, at_bats, hits]
    aLineupListVariable.append(aPlayerListVariable)
    #! IO
    IO.write_lineup(aLineupListVariable)
    print()
    print(name + " was added.\n")
    

def remove_player(aLineupListVariable):
    
    name = input("Enter Player Name:\t")
    i = 0
    list_index = -1
    
    while i < len(aLineupListVariable):
        if aLineupListVariable[i][0].lower() == name.lower():
            list_index = i
            break
        i += 1
        
    if list_index != -1:
        player = aLineupListVariable.pop(list_index)
        #! IO 
        IO.write_lineup(aLineupListVariable)
        print("'" + player[0] + "' was deleted.\n")
    else:
        print("No player with the name '" + name + "' was found.\n")
        
def move_player(aLineupListVariable):
    
    numberOfPlayers = len(aLineupListVariable)
    numberOfPlayers = str(numberOfPlayers)
    
    while True:
        try:
            # get index from effected players
            movedPlayer = int(input("Player to move:\t"))
            
            if 0 >= movedPlayer > numberOfPlayers:
                print("You must enter a number between 1 and " + numberOfPlayers)
                movedPlayer = int(input("Player to move:\t"))
            else:
                moving = aLineupListVariable[movedPlayer-1]
                print(f"{moving[0]} was selected.")
            break
        except IndexError as e:
            print("IndexError: ", e)
        except ValueError as e:
            print("ValueError: ", e)
        except TypeError as e:
            print("TypeError: ", e)
    
    while True:
        try:
            replacedPlayer = int(input("Enter a new lineup number:\t"))
            replacing = aLineupListVariable[replacedPlayer-1]
            
            if 0 >= replacedPlayer > numberOfPlayers:
                print("You must enter a number between 1 and " + numberOfPlayers)
                replacedPlayer = int(input("Enter a new lineup number:\t"))
            else:
                print(f"{moving[0]} was moved.")
            aLineupListVariable.remove(moving)
            aLineupListVariable.insert(replacedPlayer-1, moving)
            #! IO
            IO.write_lineup(aLineupListVariable)
            break
        except IndexError as e:
            print(replacing)
            print("IndexError: ", e)
        except ValueError as e:
            print("ValueError: ", e)
        except TypeError as e:
            print("TypeError: ", e)
            

def edit_player_position(aLineupListVariable):
    
    number = int(input("Enter a lineup number to edit:\t"))
    playerList = aLineupListVariable[number-1]
    playerName = aLineupListVariable[number-1][0]
    print(f"You selected {playerList[0]}: Position = {playerList[1]}")
    
    newPosition = input("Enter a new position:\t")
    
    while True:
        if newPosition in positions:
            
            check = newPosition in (stat for sublist in aLineupListVariable for stat in sublist)
            
            if check == True:
                print("This position is already filled.")
                newPosition = input("Enter a new position:\t")
            else: break
        else:
            print("You did not enter a valid position.")
            newPosition = input("Enter a new position:\t")
        
    
    edit_position = f"{newPosition}"
    
    new_player = (aLineupListVariable[number-1][0], edit_position, aLineupListVariable[number-1][2], aLineupListVariable[number-1][3])
    aLineupListVariable.remove(playerList)
    aLineupListVariable.insert(number-1, new_player)
    #! IO
    IO.write_lineup(aLineupListVariable)
    print()

def edit_player_stats(aLineupListVariable):
    
    number = int(input("Enter a lineup number to edit:\t"))
    playerList = aLineupListVariable[number-1]
    stat_change = input("Enter stat to change (name, position, atbats, hits):\t")
    
    valid_stats = ("name", "position", "atbats", "hits")
    
    if stat_change not in valid_stats:
        print("You did not enter a valid stat name.")
        stat_change = input("Enter stat to change (name, position, atbats, hits):\t")
    else:
        pass
    
    changed_stat = input("Change it to: ")
    
    while True:
        if stat_change == "name":
            edit_stat = f"{changed_stat}"
            new_player = (edit_stat, aLineupListVariable[number-1][1], aLineupListVariable[number-1][2], aLineupListVariable[number-1][3])
            break
        elif stat_change == "position":
            if changed_stat in positions:
                edit_stat = f"{changed_stat}"
                new_player = (aLineupListVariable[number-1][0], edit_stat, aLineupListVariable[number-1][2], aLineupListVariable[number-1][3])
                break
            else:
                print("You did not enter a valid position.")
                changed_stat = input("Change it to: ")
        elif stat_change == "atbats":
            try:
                changed_stat = int(changed_stat)
                value = int(playerList[3])
                if changed_stat < 0:
                    print("Your at bats cannot be less than 0.")
                    changed_stat = input("Change it to: ")
                elif changed_stat < value:
                    print("Your atbats cannot be less than your hits.")
                    changed_stat = input("Change it to: ")
                else: 
                    edit_stat = changed_stat
                    new_player = (aLineupListVariable[number-1][0], aLineupListVariable[number-1][1], edit_stat, aLineupListVariable[number-1][3])
                    break
            except ValueError:
                print("Value must be an integer.")
        elif stat_change == "hits":
            try:
                changed_stat = int(changed_stat)
                value = int(playerList[2])
                if changed_stat < 0:
                    print("Your hits cannot be less than 0.")
                    changed_stat = input("Change it to: ")

                elif changed_stat > value:
                    print("Hits cannot be greater than at bats.")
                    changed_stat = input("Change it to: ")

                else:
                    edit_stat = changed_stat
                    new_player = (aLineupListVariable[number-1][0], aLineupListVariable[number-1][1], aLineupListVariable[number-1][2], edit_stat)
                    break
            except ValueError:
                print("Value must be an integer.")
        else:
            print("You did not enter a valid stat to change.")
            stat_change = input("Enter stat to change (name, position, atbats, hits):\t")
            
    aLineupListVariable.remove(playerList)
    aLineupListVariable.insert(number-1, new_player)
    #! IO
    IO.write_lineup(aLineupListVariable)
    print()

def main():
    #! IO
    aLineupListVariable = IO.read_lineup()
    
    # the list of inner lists - aPlayerListVariable -- name, position, at_bats, hits
    # aLineupListVariable = [['Trevor', 'SS', '588', '173'],
    #                        ['Garrett', '2B', '299', '74'], 
    #                        ['Cass', '1B', '10', '10']]
    
    display_menu()
    display_positions(positions)
    print(CROSSES)
    print()
    
    # menu validation
    while True:
        command = input("Menu option: ")
        print()
        
        if command == "1":
            display_lineup(aLineupListVariable)
            print()
        elif command == "2":
            add_player(aLineupListVariable)
        elif command == "3":
            remove_player(aLineupListVariable)
        elif command == "4":
            move_player(aLineupListVariable)
        elif command == "5":
            edit_player_position(aLineupListVariable)
        elif command == "6":
           edit_player_stats(aLineupListVariable)
        elif command == "7":
            print("Program ended.")
            break
        else: 
            print("You entered an invalid menu option. Please try again.")
            main()
    
if __name__ == "__main__":
    main()