#!/usr/bin/python

import Cookie,os

import cgitb,hashlib,cgi
cgitb.enable()

#ADDED CSS LINK
head = '''
<!DOCTYPE html>
<html>
<head><title>Login page</title>
<link rel="stylesheet" type="text/css" href="indexpage.css"> 
</head>
<body>
   '''
body = """ """
foot = '''
</body>
</html>
'''

#MERGED
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
    styledResults = ""
    for i in L:
        if formresults.getvalue("keyword") == None:
            return "<h3 style='text-align:center;'>No Search Results</h3>"
        elif formresults.getvalue("keyword") in allData.lower():
            if formresults.getvalue("keyword") in "".join(i).lower():
                keywordResults.append(i)
        else:
            return "<h3 style='text-align:center;'>No Search Results</h3>"
    for s in keywordResults: 
    	styledResults += "<ul id='styledresults'>\n" + "<li id='styleName'>" + "<form method='GET' action='mainpage.py'><input type='submit' name='restaurant' value='" + s[0] + "'></form>" + "</li>\n" + "<li id='styleCost'>" + s[1] + "</li>\n" + "<li id='styleDistance'>" + s[2] + "</li>\n" + "<li id='styleFood'>" + s[3] + "</li>\n" + "<li id='styleRating'>" + s[4] + "</li>\n" + "</ul><hr>"
    return styledResults


def afterData(L):
    searchResults = [] 
    afterResults = ""
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
        return "<h3 style='text-align:center;'>No Search Results</h3>"
    else: 
        for s in searchResults: 
        	afterResults += "<ul id='styledresults'>\n" + "<li id='styleName'>" + "<form method='GET' action='mainpage.py'><input type='submit' name='restaurant' value='" + s[0] + "'></form>" + "</li>\n" + "<li id='styleCost'>" + s[1] + "</li>\n" + "<li id='styleDistance'>" + s[2] + "</li>\n" + "<li id='styleFood'>" + s[3] + "</li>\n" + "<li id='styleRating'>" + s[4] + "</li>\n" + "</ul><hr>"
    	return afterResults


def homePage():
	return """
<div id="nav-bar"> 
    <h3 id="logo">Food Mining Corporation</h3>
    <a href="createaccount.py" class="accountinfo"> Create Account! </a>
    <a href="login.py" class="accountinfo"> Login! </a> 
</div>
<a href="mainpage.py"> Go Back </a>
    <form method="GET" action="mainpage.py">
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
</form><br> <br>

<ul id="title-bar"> 
	<li id="liName">Name</li>
	<li id="liCost">Cost</li>
	<li id="liDistance">Distance</li>
	<li id="liFood">Food</li>
	<li id="liRating">Rating</li>
</ul>

"""
def searchPage():
	return """
<div id="nav-bar"> 
    <h3 id="logo">Food Mining Corporation</h3>
    <a href="createaccount.py" class="accountinfo"> Create Account! </a>
    <a href="login.py" class="accountinfo"> Login! </a> 
</div>
<p> Time to mine! Insert your preferences and find the restuarants near Stuy that you would want to go to! </p>
<h1> THIS IS GOING TO BE IMAGES </h1> 
<form method="GET" action="mainpage.py">
    Search Keyword:<input type="text" name="keyword">

    <input type="submit" name="submit">
</form>

<h1> This is going to the about us and the project and stuff </h1>

""" 

def restaurantPage():
	restaurantValue = ""
	restaurantValue += "<h1>" + formresults.getvalue("restaurant") + "</h1><br>\n"
	for thing in sortedData: 
		if thing[0] == formresults.getvalue("restaurant"):
			restaurantValue += "<img src='' alt='ITS AN IMAGE HERE'><br>\n" 
			restaurantValue += "<h3>COST: " + thing[1] + "</h3>\n"
			restaurantValue += "<h3>DISTANCE: " + thing[2] + "</h3>\n" 
			restaurantValue += "<h3>TYPE OF FOOD: " + thing[3] + "</h3>\n"
			restaurantValue += "<h3>RATING: " + thing[4] + "</h3>\n"
			restaurantValue += "<h3>DESCRIPTION:" + "This is " + thing[0] + "</h3>\n"
	return restaurantValue


def loggedhomePage():
	return """
<div id="nav-bar"> 
    <h3 id="logo">Food Mining Corporation</h3>
 	<a href="https://www.google.com" class="accountinfo"> Your Profile </a>
</div>
<a href="mainpage.py"> Go Back </a>
    <form method="GET" action="mainpage.py">
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
</form><br> <br>

<ul id="title-bar"> 
	<li id="liName">Name</li>
	<li id="liCost">Cost</li>
	<li id="liDistance">Distance</li>
	<li id="liFood">Food</li>
	<li id="liRating">Rating</li>
</ul>

"""

def loggedsearchPage():
	return """
<div id="nav-bar"> 
    <h3 id="logo">Food Mining Corporation</h3>
    <a href="https://www.google.com" class="accountinfo"> Your Profile </a>
</div>
<p> Time to mine! Insert your preferences and find the restuarants near Stuy that you would want to go to! </p>
<h1> THIS IS GOING TO BE IMAGES </h1> 
<form method="GET" action="mainpage.py">
    Search Keyword:<input type="text" name="keyword">

    <input type="submit" name="submit">
</form>

<h1> This is going to the about us and the project and stuff </h1>

""" 


#MERGED


def authenticate(u,ID,IP):
    loggedIn = open('../data/loggedin.txt','r').read().split('\n')
    loggedIn = [each.split(',') for each in loggedIn]
    loggedIn.remove([''])
    for a in loggedIn:
        if a[0] == username:
            return a[1]==str(ID) and a[2]==IP
    return False


if 'HTTP_COOKIE' in os.environ:
    cookie_string=os.environ.get('HTTP_COOKIE')
    c = Cookie.SimpleCookie()
    c.load(cookie_string)
    ##print all the data in the cookie
    #body+= "<h1>cookie data</h1>"
    #for each in c:
    #    body += each+":"+str(c[each].value)+"<br>"


    
    if 'username' in c and 'ID' in c:
        username = c['username'].value
        ID = c['ID'].value
        IP = os.environ['REMOTE_ADDR']
        
        ##print all the users logged in
        #body += "<h1>userstuff</h1>"
        #body += str(loggedIn)
        #body += "<br>"
        if authenticate(username,ID,IP): # change here
			if formresults.getvalue("submit") == "Submit":
				body += loggedhomePage() + str(sortSearch(sortedData))
			elif formresults.getvalue("Evaluate") == "Submit":
				body += loggedhomePage() + str(afterData(sortedData))
			elif "restaurant" in formresults: 
				body += restaurantPage() #CHANGE THIS TO HAVE THE FAVORITING SYSTEM
			else: 
				body += loggedsearchPage()

        else:
            body+="Failed to Authenticate cookie<br>\n"
            body+='Go Back to Website.. <a href="mainpage.py">here</a><br>'
    else:
    	#MERGED
    	if formresults.getvalue("submit") == "Submit":
        	body += homePage() + str(sortSearch(sortedData))
    	elif formresults.getvalue("Evaluate") == "Submit":
        	body += homePage() + str(afterData(sortedData))
        elif "restaurant" in formresults: 
			body += restaurantPage() 
    	else: 
        	body += searchPage()
    	#MERGED
        # GOT RID OF THIS  body+= "Your information expired<br>\n"
        # GOT RID OF THIS  body+= 'Go here!<a href="mainpage.py">here</a><br>'
else:
    #MERGED
    if formresults.getvalue("submit") == "Submit":
        body += homePage() + str(sortSearch(sortedData))
    elif formresults.getvalue("Evaluate") == "Submit":
        body += homePage() + str(afterData(sortedData)) 
    elif "restaurant" in formresults: 
		body += restaurantPage() 
    else: 
        body += searchPage()
    #MERGED
    # GOT RID OF THIS  body+= 'You seem new<br>\n'
    # GOT RID OF THIS  body+='Go here! <a href="mainpage.py">here</a><br>'

print 'content-type: text/html'
print ''
print head
print body
print foot
