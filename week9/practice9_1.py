def load_members():
    file = open("members.txt","r")
    members = {}
    for line in file:
        name, passwd, tries, wins, chips = line.strip('\n').split(',')
        members[name] = (passwd,int(tries),float(wins),int(chips))
    file.close()
    return members

members = load_members()

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
login(members)