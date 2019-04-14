def findAllSentences(filename,key) :
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()

    line = []
    l = text.split(".")
    for i in range(len(l)):
        l[i] = l[i].strip()
        # print(i,":",l[i])
        a, b, c = map(str, l[i].partition("?"))
        if len(a)>0 and len(c):
            if a[0] == "\"":
                a = a[1:]
            a = a.strip()
            if c[0] == "\"":
                c = c[1:]
            c = c.strip()
            if a.find("\"") > 0:
                line += [a+"?\""]
            else:
                line += [a+"?"]
            if c.find("\"") > 0:
                line += [c + ".\""]
            else:
                line += [c + "."]
        else:
            if len(a) > 0:
                if a[0] == "\"":
                    a = a[1:]
                a = a.strip()
                if a.find("\"") > 0:
                    line += [a+".\""]
                else:
                    line += [a+"."]
            if len(c) > 0:
                if c[0] == "\"":
                    c = c[1:]
                c = c.strip()
                if c.find("\"") > 0:
                    line += [c + "?\""]
                else:
                    line += [c + "?"]
    # print("=====FIN=====")
    # cnt=0
    # for j in line:
    #     print(cnt,":",j)
    #     cnt+=1

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
    outfile.write("'"+key+"' appears "+str(tot)+" times in "+str(sentenceCount)+" sentences.\n")


    outfile.close()
    infile.close()

print(findAllSentences("article.txt","computer"))