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


def count_score(cards):
    score = 0
    number_of_ace = 0
    for card in cards:
        if type(card['rank'])==int:
            score+=card['rank']
        elif card['rank']=="A":
            score+=11
            number_of_ace+=1
        else:
            score+=10

    # score가 21이 넘고 A가 있으면 score를 재조정함
    while score>21 and number_of_ace>0:
        score-=10
        number_of_ace-=1

    return score
deck = fresh_deck()
a=[]
(c, deck) = hit(deck)
a.append(c)
a.append({'suit': 'Club', 'rank': 'A'})
a.append({'suit': 'Club', 'rank': 'A'})
a.append({'suit': 'Club', 'rank': 'A'})

print(a)
print(count_score(a))