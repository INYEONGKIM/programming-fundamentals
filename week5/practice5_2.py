def findAll(filename,key):
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    position = text.find(key)

    if position==-1:
        outfile.write(key+" is not found.\n")
    else:
        while 0<position<len(text):
            outfile.write(key + " is at " + str(position) + ".\n")
            position=text.find(key, position+len(key))

    outfile.close()
    infile.close()
    print("Done")

# print(findAll('article.txt','computer')) # at 3222, 3310, 3554, 3678,6162, 10928.
# print(findAll('article.txt','Whole Earth')) # at 10688, 11233.
# print(findAll('article.txt','Apple')) # at 4333, 4408, 4695, 5539, 5718, 6299, 6332, 6398, 6557.
print(findAll('article.txt','apple')) # apple is not found