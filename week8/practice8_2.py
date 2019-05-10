import random

def fresh_deck():
    suits = {"Spade", "Heart", "Diamond", "Club"}
    ranks = {"A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"}
    deck = []
    for i in suits:
        for j in ranks:
            deck.append({"suit":i, "rank":j})
    random.shuffle(deck)
    return deck

def hit(deck):
    if deck==[]:
        deck = fresh_deck()
    return (deck[0], deck[1:])
