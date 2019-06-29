#!/usr/bin/python
print "content-type: text/html\n"
import cgitb, random
cgitb.enable()

filename = "othello.txt"
filename1 = "hamlet.txt"
f = open(filename, "r")
f1 = open(filename1, "r")
text = f.read()
text1 = f1.read()


def TallyWords(text):
    words = {}
    text =" ".join(text.split("--"))
    text = text.split()
    for i in text:
        i = i.lower().strip(""".,":';()-?!""")
        if len(i) > 0:
            if i in words:
                words[i] += 1
            else:
                words[i] = 1
    return words

def printTally(text):
    value = ""
    words = TallyWords(text)
    for t in words:
        value += str(t) + ":" + str(words[t]) + "\n"
    return value


def totalWords(text, value):
    words = TallyWords(text)
    oneWord = 0
    oneWordList = []
    tempValue = ""
    t = 0
    if value == 0:
        return sum(words.values()) #Total number of words 
    elif value == 1:
        return len(words)
    elif value == 2:
        for i in words.values():
            if i == 1:
                oneWord += 1
        return oneWord
    elif value == 3:
        while len(oneWordList) < 100 and t < len(words.values()):
            for c in words:
                if words[c] == 1:
                    oneWordList.append(c)
            t += 1
        for i in oneWordList: 
            tempValue += str(i) + "<br>\n" 
        return tempValue




