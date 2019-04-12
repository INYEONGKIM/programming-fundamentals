def findAllSentences(filename,key) :
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()

    line = []
    l = text.split(".")
    for i in range(len(l)):
        a, b, c = map(str, l[i].partition("?"))
        if len(a) > 0:
            a = a.strip()
            if a[0] == "\"":
                a = a[1:]
            a = a.strip()
            if a.find("\"") > 0:
                line += [a+".\""]
            else:
                line += [a+"."]
        if len(c) > 0:
            c = c.strip()
            if c[0] == "\"":
                c = c[1:]
            c = c.strip()
            if c.find("\"") > 0:
                line += [c + "?\""]
            else:
                line += [c + "?"]

    sentenceCount = 0
    tot = 0
    for i in line:
        wordCount = 0
        position = i.find(key)
        if position>0:
            sentenceCount+=1
            wordCount+=1
            while 0<position<len(i):
                position = i.find(key, position+len(key))
                if position>0:
                    wordCount+=1

            outfile.write("'"+key+"' appears "+str(wordCount)+" time.\n"+i+"\n\n")
        tot+=wordCount
    outfile.write("'"+key+"' appears "+str(tot)+" times in "+str(sentenceCount)+" sentences.")
    outfile.close()
    infile.close()
    print("done")

print(findAllSentences("article.txt","computer"))