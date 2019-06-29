#!/usr/bin/python
print "content-type: text/html\n"
import random

text ='''To VERB, or not to VERB--that is the NOUN:
Whether 'tis nobler in the NOUN to VERB
The NOUNs and NOUNs of ADJECTIVE fortune
Or to take NOUNs against a sea of NOUNs
And by opposing end them. To VERB, to VERB--
No more--and by a VERB to say we end
The heartache, and the thousand ADJECTIVE VERB
That flesh is heir to. '''

nouns=['fish','computer','Iphone','jaguar','mapo tofu']
verbs=['run','spin','talk','hit','jig','shave','cut','rap']
adjectives=['silent','big','small','hairy','rich','amazing','outrageous','preposterous']

def pickOne(nouns):
    return nouns[random.randint(0,len(nouns)-1)]

def madlibs(storyString, nounList, verbList, adjectiveList):
    data = storyString.split()
    for i in data:
    	if "NOUN" in i:
            data[data.index(i)] = i.replace("NOUN",pickOne(nounList))
    		#data[data.index(i)] = pickOne(nounList)
        elif "VERB" in i:
            data[data.index(i)] = i.replace("VERB",pickOne(verbList))
            #data[data.index(i)] = pickOne(verbList)
        elif "ADJECTIVE" in i:
            data[data.index(i)] = i.replace("ADJECTIVE", pickOne(adjectiveList))
            #data[data.index(i)] = pickOne(adjectiveList)
    return data



print madlibs(text,nouns,verbs,adjectives)
