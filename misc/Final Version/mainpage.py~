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

f = open("fooddata.txt", "r") 
data = f.read() 
f.close() 



f1 = open("../data/favorites.txt", "r")
thefavoritesread = f1.read()
f1.close()


f3 = open("../data/loggedin.txt", "r")
users = f3.read()
users = users.split("\n")
if '' in users:
	users.remove('')
if os.stat("../data/loggedin.txt").st_size != 0:
	username1 = users[-1].split(",")[0]

data1 = data.split("\n")
allData = "".join(data1)
sortedData = []
for d in data1:
	if d != "": 
		sortedData.append(d.split(","))
#sortedData.pop()


favoritereadinglist = []
thefavorites = ""
for i in thefavoritesread.split('\n'):
    favoritereadinglist.append(i.split(","))
for z in favoritereadinglist: 
	if os.stat("../data/loggedin.txt").st_size != 0:
		if z[0] == username1: 
			thefavorites += ",".join(z[1:])


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

def loggedinsortSearch(L):
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
		if s[0] in thefavorites:
			styledResults += "<ul id='styledfavorites'>\n" + "<li id='styleName'>" + "<form method='GET' action='mainpage.py'><input type='submit' name='restaurant' value='" + s[0] + "'></form>" + "</li>\n" + "<li id='styleCost'>" + s[1] + "</li>\n" + "<li id='styleDistance'>" + s[2] + "</li>\n" + "<li id='styleFood'>" + s[3] + "</li>\n" + "<li id='styleRating'>" + s[4] + "</li>\n" + "</ul><hr>"
		else:
			styledResults += "<ul id='styledresults'>\n" + "<li id='styleName'>" + "<form method='GET' action='mainpage.py'><input type='submit' name='restaurant' value='" + s[0] + "'></form>" + "</li>\n" + "<li id='styleCost'>" + s[1] + "</li>\n" + "<li id='styleDistance'>" + s[2] + "</li>\n" + "<li id='styleFood'>" + s[3] + "</li>\n" + "<li id='styleRating'>" + s[4] + "</li>\n" + "</ul><hr>"
	return styledResults


def loggedinafterData(L):
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
			if s[0] in thefavorites: 
				afterResults += "<ul id='styledfavorites'>\n" + "<li id='styleName'>" + "<form method='GET' action='mainpage.py'><input type='submit' name='restaurant' value='" + s[0] + "'></form>" + "</li>\n" + "<li id='styleCost'>" + s[1] + "</li>\n" + "<li id='styleDistance'>" + s[2] + "</li>\n" + "<li id='styleFood'>" + s[3] + "</li>\n" + "<li id='styleRating'>" + s[4] + "</li>\n" + "</ul><hr>"
			else:
				afterResults += "<ul id='styledresults'>\n" + "<li id='styleName'>" + "<form method='GET' action='mainpage.py'><input type='submit' name='restaurant' value='" + s[0] + "'></form>" + "</li>\n" + "<li id='styleCost'>" + s[1] + "</li>\n" + "<li id='styleDistance'>" + s[2] + "</li>\n" + "<li id='styleFood'>" + s[3] + "</li>\n" + "<li id='styleRating'>" + s[4] + "</li>\n" + "</ul><hr>"
		return afterResults


def homePage():
	return """
<div id="nav-bar"> 
<h3 id="logo">Food Mining Corporation</h3>
<a href="createaccount.py" class="accountinfo"> Create Account! </a>
<a href="login.py" class="accountinfo"> Login! </a> 
</div>
<a href="mainpage.py" id="goback"> Go Back </a>
<form method="GET" action="mainpage.py" style="text-align:center;">
<p id="homepageform">Restaurant Name:</p><select name="name" size="1">
<option>All</option>
<option>McDonalds</option>
<option>Terrys</option>
<option>Palm</option>
<option>Gourmet Market</option>
<option>Whole Foods</option>
</select>
<p id="homepageform"> Money:</p><select name="money" size="1">
<option>All</option>
<option>$</option>
<option>$$</option>
<option>$$$</option>
</select>
<p id="homepageform">Distance in miles:</p><select name="distance" size="1">
<option>All</option>
<option>&#60; 0.1 miles</option>
<option>0.1-0.4 miles</option>
<option>0.5-1 miles</option>
<option>&#62; 1 mile</option> 
</select>
<p id="homepageform">Type of Food:</p><select name="food" size="1">
<option>All</option>
<option>Fast Food</option>
<option>Diner</option>
<option>Deli</option>
<option>Steakhouse</option>
<option>Grocery Store</option>
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
<p style="text-align:center;font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;"> Time to mine! Insert your preferences and find the restuarants near Stuy that you would want to go to! </p>
<img src="tribecastuy.jpg" style="display: block;margin: 0 auto; width: 75%; height: 500px; border: 3px solid darkgrey">
<form method="GET" action="mainpage.py" style="text-align:center;">
<p style="text-align:center;font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;">Search Keyword:</p><input type="text" name="keyword">

<input type="submit" name="submit">
</form>

<h3 style="text-align:center;color: grey;font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;"> Jeffrey Weng and Derek Tran, just two ordinary compsci students.</h3>

""" 

def loggedinrestaurantPage():
	restaurantValue = ""
	restaurantValue += """<div id="nav-bar"> 
<h3 id="logo">Food Mining Corporation</h3>
<a href="profile.py" class="accountinfo"> Your Profile </a>
</div>"""
	restaurantValue += "<a href='mainpage.py?name=All&money=All&distance=All&food=All&Evaluate=Submit' id='goback'>Go Back! </a>"
	for thing in sortedData: 
		if thing[0] == formresults.getvalue("restaurant"):
			for i in allusersrestaurant: 
				if username1 in i and thing[0] in i: 
					restaurantValue += "<h1 id='textalignthing'>" + thing[0] + "</h1><br>\n"
					restaurantValue += "<h3 id='textalignthing'>COST: " + thing[1] + "</h3>\n"
					restaurantValue += "<h3 id='textalignthing'>DISTANCE: " + thing[2] + "</h3>\n" 
					restaurantValue += "<h3 id='textalignthing'>TYPE OF FOOD: " + thing[3] + "</h3>\n"
					restaurantValue += "<h3 id='textalignthing'>RATING: " + thing[4] + "</h3>\n"
					restaurantValue += "<h3 id='textalignthing'>DESCRIPTION:" + "This is " + thing[0] + "</h3>\n"
					restaurantValue += "<form method='GET' action='mainpage.py' id='textalignthing'><input type='submit' name='" + thing[0] + "' value='unfavorite'></form>"					
					break
			else:	 
				restaurantValue += "<h1 id='textalignthing'>" + str(formresults.getvalue("restaurant")) + "</h1><br>\n"
				restaurantValue += "<h3 id='textalignthing'>COST: " + thing[1] + "</h3>\n"
				restaurantValue += "<h3 id='textalignthing'>DISTANCE: " + thing[2] + "</h3>\n" 
				restaurantValue += "<h3 id='textalignthing'>TYPE OF FOOD: " + thing[3] + "</h3>\n"
				restaurantValue += "<h3 id='textalignthing'>RATING: " + thing[4] + "</h3>\n"
				restaurantValue += "<h3 id='textalignthing'>DESCRIPTION:" + "This is " + thing[0] + "</h3>\n"
				restaurantValue += "<form method='GET' action='mainpage.py' id='textalignthing'><input type='submit' name='"+ thing[0]+ "'value='favorite'></form>"
	return restaurantValue

def restaurantPage():
	restaurantValue = ""
	restaurantValue += """<div id="nav-bar"> 
<h3 id="logo">Food Mining Corporation</h3>
<a href="createaccount.py" class="accountinfo"> Create Account! </a>
<a href="login.py" class="accountinfo"> Login! </a> 
</div>"""
	restaurantValue += "<a href='mainpage.py?name=All&money=All&distance=All&food=All&Evaluate=Submit' id='goback'>Go Back! </a>"
	for thing in sortedData: 
		if thing[0] == formresults.getvalue("restaurant"):
			restaurantValue += "<h1 id='textalignthing'>" + str(formresults.getvalue("restaurant")) + "</h1><br>\n"
			restaurantValue += "<h3 id='textalignthing'>COST: " + thing[1] + "</h3>\n"
			restaurantValue += "<h3 id='textalignthing'>DISTANCE: " + thing[2] + "</h3>\n" 
			restaurantValue += "<h3 id='textalignthing'>TYPE OF FOOD: " + thing[3] + "</h3>\n"
			restaurantValue += "<h3 id='textalignthing'>RATING: " + thing[4] + "</h3>\n"
			restaurantValue += "<h3 id='textalignthing'>DESCRIPTION:" + "This is " + thing[0] + "</h3>\n"
	return restaurantValue

def restaurantSelect(L):
	L=L.split('\n')
	select=''
	for each in L:
		each=each.split(',')
		select+='<option>'
		select+=each[0]
		select+='</option>'
	return select


def loggedhomePage():
	return """
<div id="nav-bar"> 
<h3 id="logo">Food Mining Corporation</h3>
<a href="profile.py" class="accountinfo"> Your Profile </a>
</div>
<a href="mainpage.py" id='goback'> Go Back </a>
<form method="GET" action="mainpage.py" style="text-align:center;">
<p id="homepageform">Restaurant Name:</p><select name="name" size="1">
<option>All</option>
"""+restaurantSelect(data)+"""
</select>
<p id="homepageform">Money:</p><select name="money" size="1">
<option>All</option>
<option>$</option>
<option>$$</option>
<option>$$$</option>
</select>
<p id="homepageform">Distance in miles:</p><select name="distance" size="1">
<option>All</option>
<option>&#60; 0.1 miles</option>
<option>0.1-0.4 miles</option>
<option>0.5-1 miles</option>
<option>&#62; 1 mile</option> 
</select>
<p id="homepageform">Type of Food:</p><select name="food" size="1">
<option>All</option>
<option>Fast Food</option>
<option>Diner</option>
<option>Deli</option>
<option>Steakhouse</option>
<option>Grocery Store</option>
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
<a href="profile.py" class="accountinfo"> Your Profile </a>
</div>
<p style="text-align:center; font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;"> Time to mine! Insert your preferences and find the restuarants near Stuy that you would want to go to! </p>
<img src="tribecastuy.jpg" style="display: block;margin: 0 auto; width: 75%; height: 500px; border: 3px solid darkgrey;">
<form method="GET" action="mainpage.py" style="text-align:center;">
<p style="text-align:center; font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;">Search Keyword:</p><input type="text" name="keyword">

<input type="submit" name="submit">
</form>

<h3 style="text-align:center;color:darkgrey;font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;"> Jeffrey Weng and Derek Tran, just two ordinary compsci students.</h3>

""" 

#Get Username








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
			temp_list = []
			allusersrestaurant = thefavoritesread.split("\n")
			for temp in formresults: 
				temp_list.append(formresults.getvalue(temp))
			if formresults.getvalue("submit") == "Submit":
				body += loggedhomePage() + str(loggedinsortSearch(sortedData))
			elif formresults.getvalue("Evaluate") == "Submit":
				body += loggedhomePage() + str(loggedinafterData(sortedData))
			elif "restaurant" in formresults: 
				body += loggedinrestaurantPage() #CHANGE THIS TO HAVE THE FAVORITING SYSTEM
		#FAVORITING
			elif "favorite" in temp_list:
				for fav in formresults: 
					if formresults.getvalue(fav) == "favorite":
						if os.stat("../data/favorites.txt").st_size == 0:
							f2 = open("../data/favorites.txt", "a")
							f2.write(str(username1) + "," + str(fav) + "\n")
							f2.close()
						else: 
							testinuser = []
							item_list = []
							item_print_string = ""
							item_print_list = []
							new_favorites = thefavoritesread.split("\n")
							new_favorites.pop()
							for smallerfav in new_favorites: 
								item_list.append(smallerfav.split(","))
							for testfav in item_list:
								if testfav[0] == username1: 
									testinuser.append(testfav[0])
									testfav.append(str(fav))
									for joinstring in item_list: 
										item_print_string += ",".join(joinstring) + "\n"
									f2 = open("../data/favorites.txt","w")
									f2.write(item_print_string)
									f2.close()
							if username1 not in testinuser:								
								f3 = open("../data/favorites.txt", "a")
								f3.write(str(username1) + "," + str(fav) + "\n")
								f3.close()
				body += loggedinrestaurantPage()
			elif "unfavorite" in temp_list: 
				for fav in formresults: 
					if formresults.getvalue(fav) == "unfavorite":
						item_list = []
						item_print_string = ""
						item_print_list = []
						new_favorites = thefavoritesread.split("\n")
						new_favorites.pop()
						for smallerfav in new_favorites: 
							item_list.append(smallerfav.split(","))
						for testfav in item_list:
							if testfav[0] == username1: 
								testfav.remove(str(fav))
								for joinstring in item_list: 
									item_print_string += ",".join(joinstring) + "\n"
								f2 = open("../data/favorites.txt","w")
								f2.write(item_print_string)
								f2.close()

				body += loggedinrestaurantPage() 
		#FAVORITING
			else: 
				body += loggedsearchPage()
		else:
			body+="Failed to Authenticate cookie<br>\n"
			if formresults.getvalue("submit") == "Submit":
				body += homePage() + str(sortSearch(sortedData))
			elif formresults.getvalue("Evaluate") == "Submit":
				body += homePage() + str(afterData(sortedData))
			elif "restaurant" in formresults:
				body += restaurantPage()
			else: 
				body += searchPage()
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

print 'content-type: text/html'
print ''
print head
print body
print foot
