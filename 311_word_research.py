import sys
import math
import time
import random
import pandas as pd



def main():
    #load csv of 311
    dat = open("./Data/Citizen311Data_STD.csv")
    csvDat = pd.read_csv(dat)
    dat.close()
    complaintText = csvDat.description

    #everything already in all caps
    #so, remove all punctuation
    purifiedText = []
    punctuation = ["\\", "," , ".", "'", "/", "(", ")", "-", "&"]
    for item in complaintText:
        temp = item
        for punc in punctuation:
            temp=temp.replace(punc, "")
        purifiedText.append(temp)


    #get all the text in a string
    fullText = ""
    for line in purifiedText:
        fullText += " " + line

    #delete huge useless stuff
    del(purifiedText)
    del(complaintText)

    #get unique tokens
    tokens = fullText.split()
    uniqTok = set(tokens)
    uniqueTokens = list(uniqTok)
    del(uniqTok)
    uniqueTokens.sort()

    #count up occurrences
    utokdict = {}
    for u in uniqueTokens:
        utokdict[u] = 0

    for t in tokens:
        utokdict[t] +=1

    output = open("./Data/311_keyword_results.txt", "w+")
    for u in uniqueTokens:
        output.write(u + " " + str(utokdict[u]) + "\n")
    output.close()

if __name__ == "__main__":
    main()
