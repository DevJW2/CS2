#!/usr/bin/python
print "content-type: text/html\n"
import cgitb, cgi
cgitb.enable()
formresults = cgi.FieldStorage()

total = 0
for each in formresults:
    if each == "value1":
        print str(each) + "= " +  str(formresults.getvalue(each)) 
        total += int(formresults.getvalue(each))
    if each == "value2":
        print str(each) + "= " +  str(formresults.getvalue(each)) + "<br>" 
        total += int(formresults.getvalue(each))

for each in formresults:
     if each == "sqrt":
        total = total ** .5      
    
print "<br>"        
print "total= " + str(total)
