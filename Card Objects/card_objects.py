#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 10:32:13 2023

@author: casbu
"""
import random

class Card:
    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = value
            
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck():
    
    def __init__(self):
        self.__list = []
        self.dealt_cards = []

        for suit in ["Clubs", "Diamonds", "Hearts", "Spades"]:
            for rank in range(1,14):
                if rank == 1:
                    value = 1
                elif rank == 2:
                    value = 2
                elif rank == 3:
                    value = 3
                elif rank == 4:
                    value = 4
                elif rank == 5:
                    value = 5
                elif rank == 6:
                    value = 6
                elif rank == 7:
                    value = 7
                elif rank == 8:
                    value = 8
                elif rank == 9:
                    value = 9
                elif rank == 10:
                    value = 10
                elif rank == 11:
                    value = 11
                elif rank == 12:
                    value = 12
                elif rank == 13:
                    value = 13
                self.__list.append(Card(rank,suit,value))

    def __iter__(self):
        for card in self.__list:
            yield card
            
    def shuffle(self):
        return random.shuffle(self.__list)
    
    def dealCard(self):
        self.dealt_cards.append(self.__list.pop())
    
    def countCards(self):
        return len(self.__list)
    
    def countHand(self):
        return len(self.dealt_cards)
    
    def totalPoints(self):
        total = 0
        for card in self.dealt_cards:
            total += card.value
        return total
    
# class Hand(Card):
#     def __init__(self):
#         self.__dealt_cards = []
        
#     def addCard(self, card):
#         self.__list.append(Card(rank,suit))
