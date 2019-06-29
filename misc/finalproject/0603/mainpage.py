#!/usr/bin/python

import Cookie,os

import cgitb,hashlib,cgi
cgitb.enable()

head = '''
<html>
<head><title>Login page</title>
</head>
<body>
   '''
body = ""
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
#MERGED


def authenticate(u,ID,IP):
    loggedIn = open('../data/loggedin.txt','r').read().split('\n')
    loggedIn = [each.split(',') for each in loggedIn]
    loggedIn.remove([''])
    for a in loggedIn:
        if a[0] == username:
            return a[1]==str(ID) and a[2]==IP
    return False

def makePage():
    return """Place your website here

""" 


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
            body+=makePage()
        else:
            body+="Failed to Authenticate cookie<br>\n"
            body+='Go Login.. <a href="foodProcessor.py">here</a><br>'
    else:
        body+= "Your information expired<br>\n"
        body+= 'Go here!<a href="foodProcessor.py">here</a><br>'
else:
    #MERGED

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
        body += """
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
    #MERGED
    body+= 'You seem new<br>\n'
    body+='Go here! <a href="foodProcessor.py">here</a><br>'

print 'content-type: text/html'
print ''
print head
print body
print foot
