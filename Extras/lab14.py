#!/usr/bin/python
print "content-type: text/html\n"
import cgitb, random, cgi
cgitb.enable()




formresults = cgi.FieldStorage()

f=open('othello.txt', 'r')
f1=open('hamlet.txt', 'r')
text=f.read()
text1=f1.read()

if formresults.getvalue('book1') == 'Hamlet':
   f=open('hamlet.txt', 'r')
   text=f.read()
if formresults.getvalue('book1') == 'Othello':
   f=open('othello.txt', 'r')
   text=f.read()
if formresults.getvalue('book2') == 'Hamlet':
   f1=open('hamlet.txt', 'r')
   text1=f1.read()
if formresults.getvalue('book2') == 'Othello':
   f1=open('othello.txt', 'r')
   text1=f1.read()


def TallyWords(text):
    words = {}
    text =" ".join(text.split("--"))
    text = text.split()
    for i in text:
        i = i.lower().strip(""".,":&[]12345';()-?!""")
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
            if words.values()[t] == 1:
                oneWordList.append(words.keys()[t])
            t += 1
        for i in oneWordList: 
            tempValue += str(i) + "<br>\n" 
        return tempValue
    #elif value == 4:
#        while len(topWord) < 10:
#            topWord.append(words[tallys.index(max(tallys))])
#            topNum.append(max(tallys))
#            words.remove(words[tallys.index(max(tallys))])
#            tallys.remove(max(tallys))
#        return topWord,topNum


item1 = TallyWords(text)
item2 = TallyWords(text1)
for keys in item1:
    if str(keys) not in item2.keys():
        item2[keys] = 0
for keys1 in item2:
    if str(keys1) not in item1.keys():
        item1[keys1] = 0


print """
<!DOCTYPE html>
<html>
<head> 
<style>
	table td{
		vertical-align: top;
	}
	table {
		margin-right: 5em;
		width: 350px;
		}
	h2 {
		display: inline;
		margin-right: 5em;
	}
	div {
		display: inline;
		width: 200px;
		float: left;
	}
	
</style>
</head>
<body>
<a href="http://marge.stuy.edu/~leila.storkamp/labs/lab14/lab14.py">Leila</a>
<a href="http://marge.stuy.edu/~nishchay.bajaj/labs/lab14/lab14final.py">Nishchay</a><br><br>
<h2>Jeffrey Weng, Nishchay Bajaj, Leila Storkamp</h2>
<form method="GET" action="lab14.py">
<br>
Book 1: <select name="book1" size="1">
  <option>Hamlet</option>
  <option selected>Othello</option>
</select>
<br>
Book 2: <select name="book2" size="1">
  <option selected>Hamlet</option>
  <option>Othello</option>
</select>


<input type="submit" name="submit" value="done"><br> <br>
"""


tempitem = item1
tempitem2 = item2
templist = []
templist1 = []
tp2 = []
tp3 = []
temptimer = 0
tptimer = 0


print "<div><h2>"  
print formresults.getvalue('book1')
print"</h2><br>"
print str(totalWords(text,0)) + " unique words"
print "<h3>Top 15 words</h3><br>"

while len(templist) < 16: 
	templist.append(tempitem.keys()[tempitem.values().index(max(tempitem.values()))])
	templist1.append(max(tempitem.values()))
	tempitem.pop(tempitem.keys()[tempitem.values().index(max(tempitem.values()))])
while temptimer < 16: 
	print str(templist[temptimer]) + " : " + str(templist1[temptimer]) + "<br>"
	temptimer += 1
print "<br>(NISHCHAY)" +"<h5>Total 'words':</h5>" + str(totalWords(text,0)) + "\n<br>"
print "<br>(LEILA)" +"<h5>Number of words that occur once:</h5>" + str(totalWords(text,2)) + "\n<br>"
print "<br>(JEFFREY)" + "<h5>First 100 words:</h5><br> " + totalWords(text, 3)
print"</div>"

print "<div><h2>" 
print formresults.getvalue('book2')
print "</h2><br>"
print str(totalWords(text1, 0)) + " unique words"
print "<h3>Top 15 words</h3><br>"
while len(tp2) < 16: 
	tp2.append(tempitem2.keys()[tempitem2.values().index(max(tempitem2.values()))])
	tp3.append(max(tempitem2.values()))
	tempitem2.pop(tempitem2.keys()[tempitem2.values().index(max(tempitem2.values()))])
while tptimer < 16: 
	print str(tp2[tptimer]) + " : " + str(tp3[tptimer]) + "<br>"
	tptimer += 1
print "<br>(NISHCHAY)" + "<h5>Total 'words':</h5>" + str(totalWords(text1,0)) + "\n<br>"
print "<br>(LEILA)" +"<h5>Number of words that occur once:</h5>" + str(totalWords(text1,2)) + "\n<br>"
print "<br>(JEFFREY)" + "<h5>First 100 words:</h5><br> " + totalWords(text1, 3)
print "</div>"
print """
<table>
<tr>
<td>
    <table border= "1">
        <tr><td>Word</td><td>
"""
print formresults.getvalue('book1')
print " count</td><td>%</td></tr>"

word1 = item1
for i in sorted(word1): 
    print "<tr><td>" + str(word1[i]) + "</td><td>" + str(i) + "</td><td>" + str(round(word1[i]/27330.0,5) * 100) + "%</td></tr>"
print """    
    </table>
</td>
<td>
    <table border="1">
        <tr><td>Word</td><td>
"""
print formresults.getvalue('book2') 
print " count</td><td>%</td></tr>"

word2 = item2
for z in sorted(word2): 
    print "<tr><td>" + str(word2[z]) + "</td><td>" + str(z) + "</td><td>" + str(round(word2[z]/31900.0,5) * 100) + "%</td></tr>"

print """
    </table>
</td>
<td>
    <table border="1">
        <tr><td>BiggerBook</td><td>difference</td></tr>
"""


g = 0
morewords = []
for u in sorted(word1): 
	morewords.append(word1[u])
morewords1 = []
for p in sorted(word2):
	morewords1.append(word2[p])
while g < len(word1): 
	if int(morewords[g]) > int(morewords1[g]): 
		print "<tr><td>"+ formresults.getvalue('book1')+ "</td><td>" + str(abs(round(morewords[g]/27330.0,5) * 100 - round(morewords1[g]/31900.0,5) * 100)) + "%</td></tr>"
	else:
		print "<tr><td>" + formresults.getvalue('book2') + "</td><td>" + str(abs(round(morewords1[g]/31900.0,5) * 100 - round(morewords[g]/27330.0,5) * 100)) + "%</td></tr>"
	g += 1

print """
    </table>
</td>


</tr>
"""

print """
</table>
</body>
</html>
"""


f.close()
f1.close()











