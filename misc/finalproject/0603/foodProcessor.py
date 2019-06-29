#!/usr/bin/python
print "content-type: text/html\n"
import cgitb, cgi

cgitb.enable()
formresults = cgi.FieldStorage()

f = open("fooddata.csv", "r")
data = f.read()
f.close()

data1 = data.split("\n")
allData = "".join(data1)
sortedData = []
for d in data1:
    if d != "": 
        sortedData.append(d.split(","))
sortedData.pop()

def sortSearch(L):
    keywordResults = []
    for i in L:
        if formresults.getvalue("keyword") == None:
            return "No Search Results"
        elif formresults.getvalue("keyword") in allData.lower():
            if formresults.getvalue("keyword") in "".join(i).lower():
                keywordResults.append(i)
        else:
            return "No Search Results"
    return keywordResults


def afterData(L):
    searchResults = [] 
    for i in L: 
        if (formresults.getvalue("name") == i[0] or formresults.getvalue('name') == "All") and (formresults.getvalue('money') == i[1] or formresults.getvalue("money") == "All") and (formresults.getvalue("food") == i[3] or formresults.getvalue("food") == "All"):
            if (formresults.getvalue("distance") == "< 0.1 miles" and (float(i[2]) < 0.1)) or formresults.getvalue("distance") == "All":
                searchResults.append(i)
            elif (formresults.getvalue("distance") == "0.1-0.4 miles" and (float(i[2]) <= 0.4 and float(i[2]) >= 0.1)) or formresults.getvalue("distance") == "All":
                searchResults.append(i)
            elif (formresults.getvalue("distance") == "0.5-1 miles" and (float(i[2]) <= 1 and float(i[2]) >= 0.5)) or formresults.getvalue("distance") == "All":
                searchResults.append(i)
            elif (formresults.getvalue("distance") == "> 1 mile" and (float(i[2]) > 1)) or formresults.getvalue("distance") == "All":
                searchResults.append(i)
    if searchResults == []:
        return "No Search Results"
    else: 
        return searchResults

            


if formresults.getvalue("submit") == "Submit":
    print """
    <!DOCTYPE html>
    <html>
    <head>
        <link rel="stylesheet" type="text/css" href="indexpage.css">
    </head>
    <body>
    	<div id="nav-bar"> 
		<h3 id="logo">Food Mining Corporation</h3>
		<a href="createaccount.py" class="accountinfo"> Create Account! </a>
		<a href="login.py" class="accountinfo"> Login! </a> 
	</div>
	<a href="foodProcessor.py"> Go Back </a>
        <form method="GET" action="foodProcessor.py">
        Restaurant Name:<select name="name" size="1">
		<option>All</option>
		<option>McDonalds</option>
		<option>Terrys</option>
	</select>
	Money:<select name="money" size="1">
		<option>All</option>
		<option>$</option>
		<option>$$</option>
		<option>$$$</option>
	</select>
	Distance in miles:<select name="distance" size="1">
		<option>All</option>
		<option>&#60; 0.1 miles</option>
		<option>0.1-0.4 miles</option>
		<option>0.5-1 miles</option>
		<option>&#62; 1 mile</option> 
	</select>
	Type of Food:<select name="food" size="1">
		<option>All</option>
		<option>Food1</option>
		<option>Food2</option>
	</select><br> 
        <input type="submit" name="Evaluate">
        </form>
    </body>

    </html>

"""
    print sortSearch(sortedData)
elif formresults.getvalue("Evaluate") == "Submit":
    print afterData(sortedData)
else: 
    print """
<!DOCTYPE html> 
<html>
<head> 
	<link rel="stylesheet" type="text/css" href="indexpage.css">
</head>
<body>
	<div id="nav-bar"> 
		<h3 id="logo">Food Mining Corporation</h3>
		<a href="createaccount.py" class="accountinfo"> Create Account! </a>
		<a href="login.py" class="accountinfo"> Login! </a> 
	</div>
	<p> Time to mine! Insert your preferences and find the restuarants near Stuy that you would want to go to! </p>
	<h1> THIS IS GOING TO BE IMAGES </h1> 
<form method="GET" action="foodProcessor.py">
	Search Keyword:<input type="text" name="keyword">

	<input type="submit" name="submit">
</form>

<h1> This is going to the about us and the project and stuff </h1>

</body>

</html>

"""

    



