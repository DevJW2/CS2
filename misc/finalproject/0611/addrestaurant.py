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
            Distance from Stuy:
            <select name="distance">
                <option>All</option>
                <option>< 0.1 miles</option>
                <option>0.1-0.4 miles</option>
                <option>0.5-1 miles</option>
                <option>> 1 mile</option>
            </select><br>
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

f=open('test.txt','r')
restaurants=f.read()

if results.getvalue('name')+',' in restaurants:
    print 'This restaurant is already added.'

if len(results)>0:
    f=open('test.txt','a')
    f.write(results.getvalue('name')+','+results.getvalue('cost')+','+results.getvalue('distance')+','+results.getvalue('food')+','+results.getvalue('rate')+'\n')
    f.close()
    print '<a href="mainpage.py?name="'+results.getvalue('name')+'">FIXTHIS go to mainpage and display the same restaurant page</a>'
else:
    print form

