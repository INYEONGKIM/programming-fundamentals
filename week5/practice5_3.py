def findAllNCount(filename,key):
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    position = text.find(key)
    count = 0
    if position==-1:
        outfile.write(key+" is not found.")
        print("Done")
    else:
        outfile.write("at ")
        while 0<position<len(text):
            count+=1
            outfile.write(str(position))
            position=text.find(key, position+len(key))
            if position==-1:
                outfile.write(".\n")
            else:
                outfile.write(", ")
        outfile.write(key + " is found " + str(count) + " times.")
    outfile.close()
    infile.close()
    print("Done")


# findAllNCount('article.txt','computer') # computer is found 6 times.
# findAllNCount('article.txt','Whole Earth') # Whole Earth is found 2 times.
findAllNCount('article.txt','Apple') # Apple is found 9 times.
# findAllNCount('article.txt','commencement') # commencement is found 1 time.
# findAllNCount('article.txt','apple') # apple is not found