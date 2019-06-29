#!/usr/bin/python
print "content-type: text/html\n"
import cgitb, cgi, hashlib
cgitb.enable()

formresults = cgi.FieldStorage()

directory = "data/"
f = open(directory + "users.txt", "a")
data = open(directory + "users.txt", "r")
text = data.read()


print """
<!DOCTYPE html>
<html>
<head>
</head>
<body>
<h1> Make an account! </h1>
<form method="GET" action="createaccount.py">
Username: <br><input type="text" name="createuser"><br>
Password: <br><input type="password" name="createpass"> <br>
<input type=submit name="createAccount" value="Create Account"> 
</form>

<h1> Login! </h1>
<form method="GET" action="createaccount.py">
Username: <br><input type="text" name="username"><br>
Password: <br><input type="password" name="password"><br>
<input type=submit name="login" value="Login">
</form> <br>

</body>
</html>
"""
 
def remove_duplicate(x):
	x = x.split("\n")
	for i in x:
		if formresults.getvalue("createuser").strip().lower() == i[:i.find(",")].strip(): 
			return False
	return True

if "createuser" in formresults and "createpass" in formresults and remove_duplicate(text):
	if formresults.getvalue("createuser").strip().lower() == "terminate" and formresults.getvalue("createpass").strip() == "wipe": 
		wipe = open(directory + "users.txt", "w")
		wipe.write("")
		wipe.close()
	else:
		f.write(formresults.getvalue("createuser").strip().lower() + "," + hashlib.sha256(str(formresults.getvalue("createpass").strip())).hexdigest() + "\n") 


if "username" in formresults and "password" in formresults:
        if "" == text:
                print "<h2>Go create an account!</h2>"
        elif formresults.getvalue("username").strip().lower() + "," + hashlib.sha256(str(formresults.getvalue("password").strip())).hexdigest() in text.split("\n"):
                print "<h2>Success!</h2>"
        else:                
                print "<h2>Login Failed</h2>"

f.close()
data.close()


