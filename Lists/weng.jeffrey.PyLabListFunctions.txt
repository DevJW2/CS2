def removeValuesFromXtoYList(L,x,y):
    i = 0
    while i < len(L) :
        if L[i] > x and L[i] < y:
            L.remove(L[i])
            i = 0
        i += 1
    

L=[1, 3, -5, 10, -2, 0, -6.0, 0 , 1]
removeValuesFromXtoYList(L,-3,3)
print L

L=[ 1, 3, -5, 10, -2, 0, 2, 2, 3, -6.0]
removeValuesFromXtoYList(L,0,10)
print L

def moveNegativeToEnd(L):
    i = 0
    while i < len(L):
        if L[i] < 0:
            L.append(L[i])
            L.remove(L[i])
        i += 1


x=[ 1, 3, -5, 10, -2, 0, -6.0]
moveNegativeToEnd(x)
print x

y=[0, 1 , -3, 4.5]
moveNegativeToEnd(y)
print y

def reverseWordsWithCapitals(L):
    i = 0
    c = 0
    while i < len(L):
        while c < len(L[i]):
            if L[i][c] > "A" and L[i][c] < "Z":
                L[i] = L[i][::-1]
                c += len(L[i])
            c += 1
        c = 0
        i += 1


x = ["thing","Fish","lie","whaTever"]
reverseWordsWithCapitals( x )
print x

def matching(listA, listB):
    i = 0
    count = 0
    while i < len(listA) and i < len(listB):
        if listA[i] == listB[i]:
            count += 1
        i += 1
    return count 

print matching([1,2,3],[2,3,4])
print matching([1,2,3],[2,2,3])
print matching([4,1,9,2,3],[2,1,9,2,3,3,3,3])

def stringToList(s):
    i = 0
    newList = []
    while i < len(s):
        newList.append(s[i])
        i += 1
    return newList

print stringToList("bob")

def noDupeMatch(listA, listB):
    i = 0
    count = 0
    alreadyCounted = []
    while i < len(listA):
        if listA[i] in listB and listA[i] not in alreadyCounted:
            alreadyCounted.append(listA[i])
            count += 1
        i += 1
    return count

print noDupeMatch( [5,6,2,8] , [8,6,5,4,2,5,8] )
        
             
