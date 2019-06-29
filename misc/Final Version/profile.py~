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
<!DOCTYPE html>
<html>
<head><link rel="stylesheet" type="text/css" href="indexpage.css"> </head>
<body>
<h1 id="textalignthing"> Create a Profile </h1>
<form method="GET" action="profile.py" id="textalignthing">
    <h3 id="textalignthing"> Name: </h3><input type="text" name="name" ><br>
    <h3 id="textalignthing"> Birthday: </h3>
    <p id="textalignthing" style='display: inline;'> Month: </p><select name="month">
    <option>January</option>
    <option>February</option>
    <option>March</option>
    <option>April</option>
    <option>May</option>
    <option>June</option>
    <option>July</option>
    <option>August</option>
    <option>September</option>
    <option>October</option>
    <option>November</option>
    <option>December</option>
    </select>
    <p id="textalignthing" style="display: inline;"> Day: </p><select name="day">
    <option>1</option>
    <option>2</option>
    <option>3</option>
    <option>4</option>
    <option>5</option>
    <option>6</option>
    <option>7</option>
    <option>8</option>
    <option>9</option>
    <option>10</option>
    <option>11</option>
    <option>12</option>
    <option>13</option>
    <option>14</option>
    <option>15</option>
    <option>16</option>
    <option>17</option>
    <option>18</option>
    <option>19</option>
    <option>20</option>
    <option>21</option>
    <option>22</option>
    <option>23</option>
    <option>24</option>
    <option>25</option>
    <option>26</option>
    <option>27</option>
    <option>28</option>
    <option>29</option>
    <option>30</option>
    <option>31</option>
    </select>
    <p id="textalignthing" style='display: inline;'> Year: </p><input type="text" name="year" size="4"><br>
    <h3 id="textalignthing"> Email: </h3><input type="text" name="email"><br>
    <input type="submit" name="submit" value="save changes">
    <h3 id="textalignthing"> Press Two Times </h3>
</form></body> </html>'''
    if "submit" in formresults:
        f=open('../data/userinfo.txt','a')
        f.write(username+','+formresults.getvalue('name')+','+formresults.getvalue('month')+'/'+formresults.getvalue('day')+'/'+formresults.getvalue('year')+','+formresults.getvalue('email')+',http://www.clker.com/cliparts/Z/J/g/U/V/b/avatar-male-silhouette-hi.png'+'\n')
        f.close()
else:
    splitlist = []
    for each in userinfo.split("\n"):
        splitlist.append(each.split(','))
    for each in splitlist:
        if username in each:
            print '''<!DOCTYPE html>
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
<h3 id="textalignthing">My Profile</h3>
<a href="profileedit.py" id='textalignthing' style = 'display: block;color: darkcyan; text-decoration: none;'>Edit your profile</a>
<table style='margin: auto;padding: 10px;'>
<tr><th>MY PROFILE<br>
STUYVESANT<br>
New York City</th><tr>
<tr><td><img src="'''+each[4]+'''" style="width: 250px; height: 250px;"></td></tr>
<tr><td id='textalignthing'>Name:''' + each[1] + """</td></tr>
<tr><td id='textalignthing'>Birthday:""" + each[2] + """</td></tr>
<tr><td id='textalignthing'>Email:""" + each[3] + """</td></tr>
</table>
<p id='textalignthing'>Favorite Restaurants</p>
<h3 id='textalignthing'>""" + thefavorites + """</h3>
</p>
<p id='textalignthing'> Find a new restaurant? <a href="addrestaurant.py" style="color: darkcyan; text-decoration: none;">Add it here!</a></p>
</body>
</html>
"""


    


    
