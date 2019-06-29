#!/usr/bin/python
print "content-type: text/html\n"
import cgitb, cgi
from math import *
cgitb.enable()
formresults = cgi.FieldStorage()

value = True
temp = []
page = 0
linesperpage = 10
extra = ''

f = open("MOCK_DATA.csv", "r")
data = f.read()
f.close()

split_data = []
for i in data.split("\n"):
    split_data.append(i.split(","))
split_data.pop()
split_data.pop(0)

if 'page' in formresults:
    page = formresults.getvalue('page')
if 'linesperpage' in formresults:
    linesperpage = formresults.getvalue('linesperpage')


def pop_data(L):
    new_list = []
    if "substring" in formresults and "selectState" in formresults:
        if formresults.getvalue("searchType") == "first":
            for item in L:
                if str(formresults.getvalue("query")) in str(item[1]).lower() and str(formresults.getvalue("state")) in str(item[4]):
                    new_list.append(item)
        elif formresults.getvalue("searchType") == "last":
            for item in L:
                if str(formresults.getvalue("query")) in str(item[2]).lower() and str(formresults.getvalue("state")) in str(item[4]):
                    new_list.append(item)
        elif formresults.getvalue("searchType") == "email":
            for item in L:
                if str(formresults.getvalue("query")) in str(item[3]).lower() and str(formresults.getvalue("state")) in str(item[4]):
                    new_list.append(item)
        return new_list
    elif "substring" in formresults:
        if formresults.getvalue("searchType") == "first":
            for item in L:
                if str(formresults.getvalue("query")).lower() in str(item[1]).lower():
                    new_list.append(item)
        elif formresults.getvalue("searchType") == "last":
            for item in L:
                if str(formresults.getvalue("query")).lower() in str(item[2]).lower():
                    new_list.append(item)
        elif formresults.getvalue("searchType") == "email":
            for item in L:
                if str(formresults.getvalue("query")).lower() in str(item[3]).lower():
                    new_list.append(item)
        return new_list
    elif "selectState" in formresults:
        for item in L:
            if str(formresults.getvalue("state")) in str(item[4]):
                new_list.append(item)
        return new_list
    return L

if "selectState" in formresults and "substring" in formresults: 
    extra += "&submit=Submit&selectState=on&state=" + str(formresults.getvalue("state")) + "&substring=bysub&query=" + str(formresults.getvalue("query")) + "&searchType=" + str(formresults.getvalue("searchType"))
elif "substring" in formresults: 
    extra += "&submit=Submit&substring=bysub&query=" + str(formresults.getvalue("query")) + "&searchType=" + str(formresults.getvalue("searchType"))
elif "selectState" in formresults: 
    extra += "&submit=Submit&selectState=on&state=" + str(formresults.getvalue("state"))

def makeTable(data):
    output = ""
    output += "<table border='1px'>\n<tr>"
    output += "<th></th><th>first_name</th><th>last_name</th><th>email</th><th>State of Residence</th>"
    output += "</tr>\n"
    for c in data:
        output += "<tr>"
        for x in c:
            output += "<td>" + str(x) + "</td>"
        output += "</tr>\n"

    output += "</table>\n"
    return output

print """
<!DOCTYPE html>
<html>
<head>
</head>
<body style="background-color:cyan">
<form method="GET" action="lab13.py">
<input type="checkbox" name="substring" value="bysub">Search by String <input type="text" name="query">
<select name="searchType"> 
    <option> first </option>
    <option> last </option> 
    <option> email </option> 
</select> 
<br>
<input type="checkbox" name="selectState" value="on">Search by state
    <select name="state" size="1">
	<option>Alabama</option>
	<option>Alaska</option>
	<option>Arizona</option>
	<option>Arkansas</option>
	<option>California</option>
	<option>Colorado</option>
	<option>Connecticut</option>
	<option>Delaware</option>
	<option>Florida</option>
	<option>Georgia</option>
	<option>Hawaii</option>
	<option>Idaho</option>
	<option>Illinois</option>
	<option>Indiana</option>
	<option>Iowa</option>
	<option>Kansas</option>
	<option>Kentucky</option>
	<option>Louisiana</option>
	<option>Maine</option>
	<option>Maryland</option>
	<option>Massachusetts</option>
	<option>Michigan</option>
	<option>Minnesota</option>
	<option>Mississippi</option>
	<option>Missouri</option>
	<option>Montana</option>
	<option>Nebraska</option>
	<option>Nevada</option>
	<option>New Hampshire</option>
	<option>New Jersey</option>
	<option>New Mexico</option>
	<option>New York</option>
	<option>North Carolina</option>
	<option>North Dakota</option>
	<option>Ohio</option>
	<option>Oklahoma</option>
	<option>Oregon</option>
	<option>Pennsylvania</option>
	<option>Rhode Island</option>
	<option>South Carolina</option>
	<option>South Dakota</option>
	<option>Tennessee</option>
	<option>Texas</option>
	<option>Utah</option>
	<option>Vermont</option>
	<option>Virginia</option>
	<option>Washington</option>
	<option>West Virginia</option>
	<option>Wisconsin</option>
	<option>Wyoming</option>
	<option>District of Columbia</option>
    </select>

<br><br>
<input type="submit" name="submit"><input type="text" name="linesperpage" value="10" size="3">results per page
</form>
<br><br>

</body>
</html>   

"""





if "submit" in formresults:
    linesperpage = int(linesperpage)
    page = int(page)
    results = 0
    totalresults = 0
    for y in pop_data(split_data)[linesperpage*page:linesperpage*page + linesperpage]: 
        results += 1 
    for z in pop_data(split_data):
        totalresults += 1
    print "page: " + str(page) + "&nbsp;&nbsp;&nbsp;"
    print "max_page: " + str(int(ceil(float(totalresults)/linesperpage) - 1)) + "&nbsp;&nbsp;&nbsp;" 
    print "linesperpage: " + str(linesperpage) + "&nbsp;&nbsp;&nbsp;"
    print "totalresults: " + str(totalresults) + "<br><br>"
    print "shown results: " + str(results)
    if page == 0 and results == totalresults:
        print ""
    elif page == int(ceil(float(totalresults)/linesperpage) - 1) and results * (page + 1) == totalresults:
        print """<a href="lab13.py?page=""" + str(page-1) + "&submit=Submit&linesperpage=" + str(linesperpage) + str(extra) + """">previous!</a>""" 
    elif page == 0: 
        print """<a href="lab13.py?page=""" + str(page+1) + "&submit=Submit&linesperpage=" + str(linesperpage) + str(extra) + """">next!</a>""" 
    elif results != linesperpage:
        print """<a href="lab13.py?page=""" + str(page-1) + "&submit=Submit&linesperpage=" + str(linesperpage) + str(extra) + """">previous!</a>""" 
    else:
        print """<a href="lab13.py?page=""" + str(page+1) + "&submit=Submit&linesperpage=" + str(linesperpage) + str(extra) + """">next!</a>""" 
        print """<a href="lab13.py?page=""" + str(page-1) + "&submit=Submit&linesperpage=" + str(linesperpage) + str(extra) + """">previous!</a>""" 

    print makeTable(pop_data(split_data)[linesperpage*page:linesperpage*page + linesperpage])




