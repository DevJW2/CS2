#!/usr/bin/python
print "content-type: text/html\n"

import cgitb
cgitb.enable()

filename = "SAT.csv"
f = open(filename, 'r')
text = f.read()
text = text.split("\n")

def fixCommas(L):
	for inner in L:
		i=0
		while i < len(inner):
			res = ''
			#if you see an open double quote pop and
			#concatenate them until you see a close quote.
			if inner[i][0]=='"':
				while inner[i][-1] != '"' and i<len(inner):
					res += inner[i]+","
					inner.pop(i)
				#when you find the close quote,
				#replace it with the completed string.
				inner[i]=(res+inner[i]).strip('"')
			i+=1

def makeList(t):
	newList = []
	for i in t:
		newList.append(i.split(","))
	if [""] in newList:
		newList.remove([""])
	fixCommas(newList)

	return newList


def makeTableBody(item):
	output = ""
	for L in item:
		output += "<tr>"
		for n in L:
			output += "<td>" + n + "</td>" 
		if L[2] != "s" and L[3] != "s" and L[4] != "s" and L[5] != "s":
			output += "<td>" + str(int(L[3]) + int(L[4]) + int(L[5])) + "</td>"
		output += "</tr>\n"
	return output

def getTests(x):
	testsTaken = 0
	for y in x:
		if y[2] != "s":
			testsTaken += int(y[2])
	return testsTaken

def getTotal(x):
	totalPoints = 0
	for y in x:
		if y[2] != "s" and y[3] != "s" and y[4] != "s" and y[5] != "s":
			totalPoints += int(y[2]) * (int(y[3]) + int(y[4]) + int(y[5]))
	return totalPoints



print """
<!DOCTYPE html>
<html>
<head>
</head>
<body>
"""
print "<h3> Number of tests taken: " + str(getTests(makeList(text[1:]))) + "</h3>"
print "<h3> Total Points: " + str(getTotal(makeList(text[1:]))) + "</h3>"
print "<h3> Average Score:" + str(getTotal(makeList(text[1:]))/getTests(makeList(text[1:]))) + "</h3>"

print """
<table border = "1">
<tr><th>DBN</th><th> SCHOOL NAME</th><th> Num of SAT Test Takers </th> <th>SAT Critical Reading Avg. Score</th>
	<th> SAT Math Avg. Score </th><th> SAT Writing Avg. Score </th><th> Total Score</th>
</tr>
"""
print makeTableBody(makeList(text[1:]))



print """
</table>
</body>
</html>
"""
   

