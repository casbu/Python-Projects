#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 10:32:11 2023

@author: casbu
"""

# This OOP displays a deck of cards where each card has a value. This program 
# creates 2 classes that represent a card and a deck using composition.
# It then prints all cards within the deck, assignes values depending on the 
# rank, and prints the points and deck/hand information (card count).


from card_objects import Card, Deck
   
def main():
    print("Cards - Tester")
    print()
    print("DECK")
    
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    
    #create deck object
    deck = Deck()
        
    # print all cards in deck as a string
    for card in deck:
        print(str(card))
    print()
    
    # shuffle deck
    deck.shuffle()
    
    # print size of the deck
    print("Shuffled Deck Count: ", deck.countCards())
    print()
    
    # deal hand with five cards
    for i in range(5):
        deck.dealCard()
    
    # print cards of hand
    print("HAND")
    for i in deck.dealt_cards:
        print(i)
    print()
    
    # print total value of hand
    print("Hand points: ", deck.totalPoints())
    # print number of cards in the hand
    print("Hand count: ", deck.countHand())
    # print number of cards in deck
    print("Deck Count: ", deck.countCards())

if __name__ == "__main__":
    main()