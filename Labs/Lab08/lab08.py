#!/usr/bin/python
print "content-type: text/html\n"
import cgitb
cgitb.enable() 

def TallyWords(text):
    words = []
    tallys = []
    text =" ".join(text.split("--"))
    text = text.split()
    for i in text:
        i = i.lower().strip(""".,":';()-?!""")
        if len(i) > 0:
            if i in words:
                tallys[words.index(i)] += 1
            else:
                words.append(i)
                tallys.append(1)
    return words,tallys

def printTally(text):
    value = ""
    t = 0
    words,tallys = TallyWords(text)
    while t < len(words):
        value += str(words[t]) + ":" + str(tallys[t]) + "\n"
        t += 1
    return value


def totalWords(text, value):
    words,tallys = TallyWords(text)
    oneWord = 0
    oneWordList = []
    tempValue = ""
    topWord = []
    topNum = []
    t = 0
    item = 0
    if value == 0:
        return sum(tallys)
    elif value == 1:
        return len(words)
    elif value == 2:
        for i in tallys:
            if i == 1:
                oneWord += 1
        return oneWord
    elif value == 3:
        while len(oneWordList) < 100 and t < len(tallys):
            if tallys[t] == 1:
                oneWordList.append(words[t])
            t += 1
        for i in oneWordList: 
            tempValue += str(i) + "<br>\n" 
        return tempValue
    elif value == 4:
        while len(topWord) < 10:
            topWord.append(words[tallys.index(max(tallys))])
            topNum.append(max(tallys))
            words.remove(words[tallys.index(max(tallys))])
            tallys.remove(max(tallys))
        return topWord,topNum
    
filename = "dante.txt"
f = open(filename, 'r')

text = f.read()


print"""
<!DOCTYPE html>
<html>
<head> 
<style>
td {
    padding-right: 50px;
    vertical-align: top;
}
</style>
</head>
<body> \n
<h1> Word Counts of dante.txt </h1>
"""
print "<p>Total 'words':" + str(totalWords(text,0)) + "</p>\n"
print "<p>Distint 'words':" + str(totalWords(text,1)) + "</p>\n"
print "<p>Number of words that occur once:" + str(totalWords(text,2)) + "</p>\n"

print """
<table>
<tr> \n
"""
print "<td><h2> First 100 words that <br> appear only once: </h2>" + str(totalWords(text,3)) 
print '<br>\n</td>\n<td> <h2> Most Common Words:</h2><table border="1">\n'
print"""
<tr> 
    <th> Tally </th>
    <th> Word </th>
</tr>
"""
topWord,topNum = totalWords(text,4)
z = 0
while z < len(topWord):
    print "<tr><td>" + str(topNum[z]) + "</td><td>" + str(topWord[z]) + "</td></tr>"
    z += 1 
print "</table></td><td><h2> Tally of ALL words:</h2>\n" + '<table border="1">'
print "<tr>\n<th> frequency</th>\n<th>word</th>\n</tr>"
word,frequency = TallyWords(text)
w = 0
while w < len(word): 
    print "<tr><td>" + str(frequency[w]) + "</td><td>" + str(word[w]) + "</td></tr>"
    w += 1

print "</table></td></tr>"
print """
</table>
</body>
</htmL>
"""
f.close()
