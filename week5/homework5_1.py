import random

# test code
def testSearchWidestGap():
    db = random.sample(range(500),100)
    print("Searching the widest gap...")
    db.sort()
    print(db)
    index, gap = searchWidestGap(db)
    print("The widest gap is:", gap)
    print("between", db[index], "and", db[index+1])
    print("at", index)


def searchWidestGap(db):
    if db==[]:
        return (0, -1)
    if len(db)==1:
        return (0, 0)
    idx=0
    max=db[1]-db[0]
    for i in range(2, len(db)):
        if db[i]-db[i-1]>max:
            max=db[i]-db[i-1]
            idx=i-1
    return (max, idx)
print(searchWidestGap([3,5,8,20,22]))