def loop(x):
    while x >= 0:
        print x,
        x -= 1

loop(90)

def multipleloop(y):
    while y + 13 < 500:
        y += 13
        print y,
print ""
multipleloop(0)

def sumPerfect(z):
    total = 0
    while z ** 2 < 1000:
        total += z ** 2
        z += 1
    print total

sumPerfect(0)
    
def htmlprint(printingloop):
    print """
<!DOCTYPE html>
<html>
<head>
</head>
<body>
<table>
"""
    while printingloop < 15:
        printingloop += 1
        print "<tr><td>Something</td></tr> \n"


    print """   
</table>
</body>
</html>
"""
htmlprint(0)

def multi(x):
    total = 0
    while x <= 1000: #including 1000, Question wasn't clear 
        if x % 3 == 0 or x % 5 == 0:
            total += x
        x += 1

    return total

print multi(0)


def bigTable(printloop):
    print """
<!DOCTYPE html>
<html>
<head>
</head>
<body>
<table border="1">
<tr>
    <th> value </th>
    <th> value^2 </th>
</tr>
"""
    while printloop < 100:
        printloop += 1
        print "<tr><td>" + str(printloop) + "</td><td>" + str(printloop ** 2) + "</td></tr>\n"


    print """
</table>
</body>
</html>
"""
bigTable(0)
