#!/usr/bin/python
print "content-type: text/html\n"

import cgitb
cgitb.enable()

import cgi
results = cgi.FieldStorage()

form = '''<!DOCTYPE html>
<html>
    <head><title>Add restaurant</title>
    <link rel="stylesheet" type="text/css" href="indexpage.css"> 
    </head>
    <body>
        <div id="nav-bar"> 
        <h3 id="logo">Food Mining Corporation</h3>
        <a href="createaccount.py" class="accountinfo"> Create Account! </a>
        <a href="login.py" class="accountinfo"> Login! </a> 
        </div>
        <a href="profile.py" id="goback"> Go Back </a>
        <h1 id="textalignthing">Add Restaurant:</h1>
        <form method="GET" action="addrestaurant.py" id="textalignthing">
            <p id="textalignthing">Name of Restaurant:</p>
            <input type="text" name="name" > <br>
            <p id="textalignthing" style="display: inline;">Cost ($-least expensive, $$$$-most expensive)</p>:
            <select name="cost">
                <option>$</option>
                <option>$$</option>
                <option>$$$</option>
                <option>$$$$</option>
            </select><br>
            <p id="textalignthing">Distance from Stuy (Miles):</p>
            <input type="text" name="distance"><br><br>
            <p id="textalignthing" style="display: inline;">Type of food:</p>
            <select name="food">
                <option>Fast Food</option>
                <option>Deli</option>
                <option>Grocery Store</option>
                <option>Steakhouse</option>
                <optioN>Diner</option>
            </select><br>
            <p id="textalignthing">Your Rating:</p>
            <input type="radio" name="rate" value="5">5 stars
            <input type="radio" name="rate" value="4">4 stars
            <input type="radio" name="rate" value="3">3 stars
            <input type="radio" name="rate" value="2">2 stars
            <input type="radio" name="rate" value="1">1 stars<br>
            <p id="textalignthing">Description:</p>
            <textarea rows="5" name="description" cols="30"></textarea><br>
            <input type="submit" name="submit" value="Create">
        </form>
    </body>
</html>
'''

f=open('fooddata.txt','r')
restaurants=f.read()

if len(results)>0:
    if results.getvalue('name')+',' in restaurants:
        print 'This restaurant is already added.'
        print ''
        print '<a href="mainpage.py">Go Back</a>'
    else:
        f=open('fooddata.txt','a')
        f.write(results.getvalue('name')+','+results.getvalue('cost')+','+results.getvalue('distance')+','+results.getvalue('food')+','+results.getvalue('rate')+'\n')
        f.close()
        print 'Restaurant added!'
        print '<a href="mainpage.py?name=All&money=All&distance=All&food=All&Evaluate=Submit">Go Back</a>'
else:
    print form

