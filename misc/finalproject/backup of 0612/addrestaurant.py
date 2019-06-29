#!/usr/bin/python
print "content-type: text/html\n"

import cgitb
cgitb.enable()

import cgi
results = cgi.FieldStorage()

form = '''<!DOCTYPE html>
<html>
    <head><title>Add restaurant</title></head>
    <body>
        <h1>Add restaurant:</h1>
        <br>
        <form method="GET" action="addrestaurant.py">
            Name of restaurant:
            <input type="text" name="name" > <br>
            Cost($-least expensive, $$$$-most expensive):
            <select name="cost">
                <option>$</option>
                <option>$$</option>
                <option>$$$</option>
                <option>$$$$</option>
            </select><br>
            Distance from Stuy (Miles): 
            <input type="text" name="distance"><br>
            Type of food:
            <select name="food">
                <option>Fast Food</option>
                <option>Deli</option>
            </select><br>
            Your Rating:
            <input type="radio" name="rate" value="5">5 stars
            <input type="radio" name="rate" value="4">4 stars
            <input type="radio" name="rate" value="3">3 stars
            <input type="radio" name="rate" value="2">2 stars
            <input type="radio" name="rate" value="1">1 stars<br>
            Description:
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

