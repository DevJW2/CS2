#!/usr/bin/python
print 'content-type: text/html'
print ''

import cgitb,cgi,hashlib
cgitb.enable()

form = cgi.FieldStorage()

head = '''
<html>
<head>
</head>
<body>
   '''
body = ""
foot = '''
</body>
</html>
'''


if len(form)==0:
    body = '''
    <h1>Create account:</h1>
    <form action="createaccount.py">

    Username: <input type="text" name="username"><br>
    Password: <input type="password" name="password"><br>
    <input type="submit" value="create account">
    '''
else:
    if 'username' in form and 'password' in form:
        users = open('../data/users.txt','r').read().split('\n')
        users = [each.split(',') for each in users]
        users.remove( [""])
        username = form.getvalue('username')
        password = form.getvalue('password')
        #nice python features that I do not teach...
        if not username in [a[0] for a in users]:
            f = open('../data/users.txt','a')
            f.write(username+","+hashlib.sha256(password).hexdigest()+"\n")
            f.close()
            body += 'Successfully added. <a href="foodProcessor.py"> Click here to go back</a>.<br>'
        else:
            body += 'Username already taken!'
    else:
        body += "Please use the form!"

print head
print body
print foot
