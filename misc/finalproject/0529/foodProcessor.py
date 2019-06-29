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


def afterData(L):
	searchResults = [] 
	for i in L: 
		if formresults.getvalue("keyword") == None:
			if (formresults.getvalue("name") == i[0] or formresults.getvalue('name') == "All") and (formresults.getvalue('money') == i[1] or formresults.getvalue("money") == "All") and (formresults.getvalue("distance") == i[2] or formresults.getvalue("distance") == "All") and (formresults.getvalue("food") == i[3] or formresults.getvalue("food") == "All"):
				searchResults.append(i)
				#fix distance and your basically done.
		elif formresults.getvalue("keyword") in allData.lower(): 
			return "hi"
		else:
			return "bye"
	return searchResults
		

if formresults.getvalue("submit") == "Submit":
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
	Keyword:<input type="text" name="keyword">

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
		<option>0.1-0.5 miles</option>
		<option>0.5-1 miles</option>
		<option>&#62; 1 mile</option> 
	</select>
	Type of Food:<select name="food" size="1">
		<option>All</option>
		<option>Food1</option>
		<option>Food2</option>
	</select>
	<input type="submit" name="submit">
</form>

<h1> This is going to the about us and the project and stuff </h1>

</body>

</html>

"""



