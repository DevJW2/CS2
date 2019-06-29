#!/usr/bin/python
print "content-type: text/html\n"
import random


f = open("Story1","r")
story1 = f.read()
f.close()
f2 = open("Story2", "r")
story2 = f2.read()
f2.close()
f3 = open("Story3","r")
story3 = f3.read()
f3.close()

nouns=['minotaur','mouse','Knight','rose','computer','keyboard','pizza','gum','books','zombie','vampire',
'ghoul','table','human','worm','teacher','chips','sushi','water','earth','hurricane','tornado','game','government',]
verbs=['run','spin','talk','hit','jig','shave','cut','rap','expose','scream','sit','create','chew','gargle','poop','destroy',
'drink','digest','hug','kiss','jump','push','pull','expand','kick','transform','fly','study','headbutt']
adjectives=['silent','big','small','hairy','rich','amazing','outrageous','preposterous','awesome','sticky','ugly',
'beautiful','cute','foolish','loyal','smelly','brave','selfish','lazy','cranky','calm','starving']


def pickOne(nouns):
    return nouns[random.randint(0,len(nouns)-1)]

def madlibs(storyString, nounList, verbList, adjectiveList):
    data = storyString.split()
    data = data[:-1]
    for i in data:
        if "NOUN" in i:
            data[data.index(i)] = i.replace("NOUN",pickOne(nounList))
        elif "VERB" in i:
            data[data.index(i)] = i.replace("VERB",pickOne(verbList))
        elif "ADJECTIVE" in i:
            data[data.index(i)] = i.replace("ADJECTIVE", pickOne(adjectiveList))
    stringData = " ".join(data)
    return stringData

print """
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="mystyle.css">
</head>
<body>
"""
print "<h1 id='p1'> Story1 </h1>"
print "<p id='p1'>" + str(madlibs(story1, nouns, verbs, adjectives)) +"</p>\n"
print "<h1 id='p2'> Story2 </h1>"
print "<p id='p2'>" + str(madlibs(story2, nouns, verbs, adjectives)) + "</p>\n"
print "<h1 id='p3'> Story3 </h1>"
print "<p id='p3'>" + str(madlibs(story3, nouns, verbs, adjectives)) + "</p>\n"


print """
</body>
</html>
"""












            
            
        
