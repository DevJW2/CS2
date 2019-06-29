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
print formresults




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
	<p> Brief description of what website does </p>
	<h1> THIS IS GOING TO BE IMAGES </h1> 
<form method="GET" action="processdata.py">
	Keyword:<input type="text" name="keyword">

	Name:<select name="name" size="1">
		<option>All</option>
		<option>McDonald's</option>
		<option>Ferry's</option>
	</select>
	Money:<select name="money" size="1">
		<option>All</option>
		<option>$</option>
		<option>$$</option>
		<option>$$$</option>
	</select>
	Distance:<select name="distance" size="1">
		<option>All</option>
		<option>1-5 miles</option>
		<option>6-10 miles</option>
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
