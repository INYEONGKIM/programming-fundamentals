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

    while score>21 and number_of_ace>0:
        score-=10
        number_of_ace-=1

    return score

def show_cards(cards, message):
    print(message)
    for card in cards:
        print("\t", card['suit'], card['rank'])

def more(message):
    answer = input(message)
    while not (answer=="y" or answer=="n"):
        answer = input(message)
    return answer=="y"


print("Welcome to SMaSH Casino!")
deck = fresh_deck()
chips = 0

while True:
    print("-----")
    dealer = []
    player = []

    card, deck = hit(deck)
    player.append(card)
    card, deck = hit(deck)
    dealer.append(card)
    card, deck = hit(deck)
    player.append(card)
    card, deck = hit(deck)
    dealer.append(card)

    show_cards(dealer[1:], "My cards are:\n\t **** **")
    show_cards(player, "Your cards are:")

    score_dealer = count_score(dealer)
    score_player = count_score(player)

    if score_player == 21:
        print("Blackjack! Yon won.")
        chips+=2
    else:
        while score_player<21 and more("hit? (y/n) "):
            card, deck = hit(deck)
            print("\t",card['suit'],card['rank'])
            player.append(card)
            score_player = count_score(player)
        if score_player > 21:
            print("You bust! I won.")
            chips-=1
        else:
            while score_dealer <= 16:
                card, deck = hit(deck)
                dealer.append(card)
                score_dealer = count_score(dealer)

            show_cards(dealer, "My cards are:")

            if score_dealer > 21:
                print("I bust! You won.")
                chips+=1
            elif score_dealer == score_player:
                print("We draw.")
            elif score_player > score_dealer:
                print("You won.")
                chips+=1
            else:
                print("I won.")
                chips-=1
    print("Chips =",chips)

    if more("Play more? (y/n) "): continue
    print("Bye!")
    break