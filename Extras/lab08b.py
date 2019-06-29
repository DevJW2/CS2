#!/usr/bin/python
print "content-type: text/html\n"
import cgitb, random
cgitb.enable()

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

if random.randint(1,2) == 1:
    filename = "dante.txt"
else:
    filename = "bigmac.txt"
f = open(filename, 'r')

text = f.read()


print"""
<!DOCTYPE html>
<html>
<head> 
<style>
tr,td {
    padding-right: 15px;
    vertical-align: top;
}
h1,h2 {
    font-family: "Verdana", Geneva, sans-serif
}

table {
    border-collapse: collapse;
}

</style>
</head>
<body> \n
<h1> Word Counts of """ + str(filename) + "</h1>"

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
#topWord,topNum = totalWords(text,4)
#z = 0
#while z < len(topWord):
#    print "<tr><td>" + str(topNum[z]) + "</td><td>" + str(topWord[z]) + "</td></tr>"
#    z += 1
print "</table></td><td><h2> Tally of ALL words:</h2>\n" + '<table border="1">'
print "<tr>\n<th> frequency</th>\n<th>word</th>\n</tr>"
words = TallyWords(text)
for i in words:
    print "<tr><td>" + str(words[i]) + "</td><td>" + str(i) + "</td></tr>"


print "</table></td></tr>"
print """
</table>
</body>
</htmL>
"""
f.close()
