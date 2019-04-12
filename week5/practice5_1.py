# rfind 사용 버전
#
# def findLast(filename,key):
#     file = open(filename, "r")
#     rawData = file.read()
#     idx = rawData.rfind(key)
#     file.close()
#     if idx==-1:
#         return key+" is not found."
#     return key+" is at "+str(idx)+" the last time."

def findLast(filename,key):
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    position = text.find(key)

    if position==-1:
        outfile.write(key+" is not found.")
    else:
        while 0<position<len(text):
            prev = position
            position=text.find(key, position+len(key))
            if position==-1:
                outfile.write(key+" is at "+str(prev)+" the last time.")

    outfile.close()
    infile.close()
    print("Done")


# print(findLast('article.txt','computer')) # computer is at 10926 the last time.
# print(findLast('article.txt','Whole Earth')) # Whole Earth is at 11231 the last time.
# print(findLast('article.txt','Apple')) # Apple is at 6557 the last time.
print(findLast('article.txt','apple')) # apple is not found.