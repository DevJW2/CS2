#!/usr/bin/python
print "content-type: text/html\n"
import cgitb, cgi
cgitb.enable()
formresults = cgi.FieldStorage()

value = True

f = open("MOCK_DATA.csv", "r")
data = f.read()
f.close()

split_data = []
for i in data.split("\n"):
    split_data.append(i.split(","))
split_data.pop()

def pop_data(L):
    temp_things = []
    new_list = []
    for thing in formresults:
        temp_things.append(thing)
    if "substring" in temp_things and "selectState" in temp_things:
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
    elif "substring" in temp_things:
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
    elif "selectState" in temp_things:
        for item in L:
            if str(formresults.getvalue("state")) in str(item[4]):
                new_list.append(item)
        return new_list
    return L


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

    output += "</table>"
    return output


print makeTable(pop_data(split_data))






