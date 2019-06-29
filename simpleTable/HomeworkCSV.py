#!/usr/bin/python
print "content-type: text/html\n"
import cgitb
cgitb.enable()

filename = "table.csv"
f = open(filename, "r")

text = f.read() 
f.close()


def makeTable(allLines):
	ans = "<table>\n"
	data = allLines.split("\n") 
	for each in data: 
		ans += "<tr>"
		for i in each.split(","): 
			ans += "<td>" + str(i) + "</td>"
		ans += "</tr>\n"
	return ans +"<table>\n"

print makeTable(text)
