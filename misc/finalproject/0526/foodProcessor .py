#!/usr/bin/python
print "content-type: text/html\n"
import cgitb, cgi

cgitb.enable()
formresults = cgi.FieldStorage()

f = open("fooddata.csv", "r")
data = f.read()
f.close()

data1 = data.split("\n")
sortedData = []
for d in data1:
    if d != "": 
        sortedData.append(d.split(","))
sortedData.pop()
print sortedData


