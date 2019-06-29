#!/usr/bin/python
print "content-type: text/html\n"

import cgi, cgitb
cgitb.enable()
formresults = cgi.FieldStorage()


f = open('../data/userinfo.txt','r')
userinfo = f.read()
f.close()
f = open('../data/loggedin.txt','r')
users = f.read()
f.close()
f = open("../data/favorites.txt",'r')
favoritereading = f.read()
f.close()
#add more fields for info

users = users.split('\n')
if '' in users:
    users.remove('')
username = users[-1].split(',')[0]

favoritereadinglist = []
thefavorites = ""
for i in favoritereading.split('\n'):
    favoritereadinglist.append(i.split(","))
for z in favoritereadinglist: 
    if z[0] == username: 
        thefavorites += ",".join(z[1:])

name = ""
bio = ""

if username not in userinfo: 
    print '''
<form method="GET" action="profile.py">
    Name: <input type="text" name="name" ><br>
    Short Bio: <textarea rows="5" name="bio" cols="30"></textarea><br>
    <input type="submit" name="submit" value="save changes">
    <h1> Press Two Times </h1>
</form>'''
    if "submit" in formresults:
        f=open('../data/userinfo.txt','a')
        f.write(username+','+formresults.getvalue('name')+','+formresults.getvalue('bio')+'\n')
        f.close()
else:
    splitlist = []
    for each in userinfo.split("\n"):
        splitlist.append(each.split(','))
    for each in splitlist:
        if username in each:
            print """<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" type="text/css" href="indexpage.css"> 
<title>My Profile</title>
</head>
<body>
<div id="nav-bar"> 
<h3 id="logo">Food Mining Corporation</h3>
<a href="mainpage.py" id="goback" style="float:right;"> Go Back </a>
</div>
<h3>My Profile</h3>
<table>
<tr><th>MY PROFILE<br>
STUYVESANT/LOCATION<br>
New York City</th><tr>
<tr><td>""" + each[1] + """</td></tr>
<tr><td>""" + each[2] + """</td></tr>
</table>
<p>Favorite Restaurants</p>
<h3>""" + thefavorites + """</h3>
</p>
</body>
</html>
"""


    


    
