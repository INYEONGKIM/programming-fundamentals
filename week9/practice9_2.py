def load_members():
    file = open("members.txt","r")
    members = {}
    for line in file:
        name, passwd, tries, wins, chips = line.strip('\n').split(',')
        members[name] = (passwd,int(tries),float(wins),int(chips))
    file.close()
    return members

members = load_members()

def show_top5(members):
    print("-----")
    sorted_members = sorted(members.items(), key=lambda x:x[1][3], reverse=True)
    print("All-time Top 5 based on the number of chips earned")
    cnt=1
    for i in sorted_members[:5]:
        if i[1][3] > 0:
            print(cnt,". ",i[0]," : ", i[1][3], sep="")
            cnt+=1
show_top5(members)