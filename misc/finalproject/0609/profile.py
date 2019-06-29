#!/usr/bin/python
print "content-type: text/html\n"

import cgi, cgitb
cgitb.enable()
results=cgi.FieldStorage()


f = open('../data/userinfo.txt','r')
userinfo=f.read()
f = open('../data/loggedin.txt','r')
users=f.read()

#add more fields for info

users=users.split('\n')
if '' in users:
    users.remove('')

username=users[-1].split(',')[0]

if username+',' not in userinfo:
 
    print '''
<form method="GET" action="profile.py">
    Name: <input type="text" name="name" ><br>
    <img src="notw_silhouette-1.jpg"><br>
    Short Bio: <textarea rows="5" name="bio" cols="30"></textarea><br>
    <input type="submit" name="submit" value="save changes">
</form>'''
    if "submit" in results: 
        f=open('../data/userinfo.txt','a')
        f.write(username+','+results.getvalue('name')+','+results.getvalue('bio')+'\n')
        f.close()

else:

    userinfo=userinfo.split('\n')
    
    splitlist=[]
    for each in userinfo:
        each=each.split(',')
        splitlist.append(each)
    for each in splitlist:
        if username in each:
            name=each[1]
            bio=each[2]
            
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
<img src="notw_silhouette-1.jpg">
<table>
<tr><th>MY PROFILE<br>
STUYVESANT/LOCATION<br>
New York City</th><tr>
<tr><td>"""+name+"""</td></tr>
<tr><td>"""+bio+"""</td></tr>
<tr><td>BIRTHDAY</td></tr>
<tr><td>CONTACT</td></tr>
</table>
<p>Favorite Restaurants</p>
<ul>
<li>McDonald's</li>
<li>Ferry's</li>
</ul>
</p>
</body>
</html>
"""
    


    
