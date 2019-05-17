import random

def load_members():
    file = open("members.txt","r")
    members = {}
    for line in file:
        name, passwd, tries, wins, chips = line.strip('\n').split(',')
        members[name] = (passwd,int(tries),float(wins),int(chips))
    file.close()
    return members

def store_members(members):
    file = open("members.txt","w")
    names = members.keys()
    for name in names:
        passwd, tries, wins, chips = members[name]
        line = name + ',' + passwd + ',' + \
               str(tries) + ',' + str(wins) + "," + str(chips) + '\n'
        file.write(line)
    file.close()

def login(members):
    username = input("Enter your name: (4 letters max) ")
    while len(username) > 4:
        username = input("Enter your name: (4 letters max) ")
    trypasswd = input("Enter your password: ")

    if username in members.keys():
        if trypasswd==members[username][0]:
            tries = members[username][1]; wins = members[username][2]; chips = members[username][3]
            # if wins==0 or int(wins) != int(wins-0.5):
            #     print("You played", tries, "games and won", int(wins), "of them.")
            # else:
            #     print("You played",tries,"games and won",wins,"of them.")
            print("You played", tries, "games and won", wins, "of them.")
            print("Your all-time winning percentage is ",end="")
            if tries!=0:
                print("{0:.1f}".format(100*wins/tries)+" %")
            else:
                print("0 %")
            if chips>=0:
                print("You have",chips,"chips.")
            else:
                print("You owe",abs(chips),"chips.")

            return username, tries, wins, chips, members
        else:
            return login(members)
    else:
        return username, 0, 0, 0, members

def show_top5(members):
    print("-----")
    sorted_members = sorted(members.items(), key=lambda x: x[1][3], reverse=True)
    print("All-time Top 5 based on the number of chips earned")
    cnt = 1
    for i in sorted_members[:5]:
        if i[1][3] > 0:
            print(cnt, ". ", i[0], " : ", i[1][3], sep="")

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

# Algorithm 2
username, tries, wins, chips, members = login(load_members())   # members = dict
deck = fresh_deck()
today_tries=0
today_wins=0
while True:
    print("-----")
    tries+=1
    today_tries+=1

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
        wins+=1; today_wins+=1
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
                wins+=1; today_wins+=1
            elif score_dealer == score_player:
                print("We draw.")
                wins+=0.5; today_wins+=0.5
            elif score_player > score_dealer:
                print("You won.")
                chips+=1
                wins+=1; today_wins+=1
            else:
                print("I won.")
                chips-=1
    print("Chips =",chips)

    if not more("Play more? (y/n) "):
        print("Bye!")
        break

# Algorithm 15
pwd = members[username][0]
members[username] = (pwd, tries, wins, chips)
store_members(members)

# Algorithm 16
print("You played",today_tries,"games and won",today_wins,"of them.")
print("Your winning pecentage today is ","{0:.1f}".format(100*today_wins/today_tries),"%.",sep="")

# Algorithm 17
show_top5(members)