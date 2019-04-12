def oneSentencePerLine(filename):
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    count = 0

    l = text.split(".")
    for i in range(len(l)):
        a,b,c = map(str, l[i].partition("?"))
        if len(a)>0:
            a = a.strip()
            count+=1
            if a[0]=="\"":
                a=a[1:]
            a = a.strip()
            if a.find("\"")>0:
                outfile.write(a + ".\"\n\n")
            else:
                outfile.write(a + ".\n\n")
        if len(c)>0:
            c = c.strip()
            count+=1
            if c[0]=="\"":
                c=c[1:]
            c = c.strip()
            if c.find("\"")>0:
                outfile.write(c + "?\"\n\n")
            else:
                outfile.write(c + "?\n\n")

    outfile.write("There are " + str(count) + " sentences in total.\n")
    outfile.close()
    infile.close()
    print("Done")
print(oneSentencePerLine("article.txt"))