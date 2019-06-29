def bondify(name):
    i = 0
    while i < len(name):
        if name[i] == " ":
            return name[i+1:] + ", " + name
        else:
            i += 1
    return name

print bondify("Xiao-Xiao Zhou")

def upper(s):
    i = 0
    x = ""
    while i < len(s):
        if s[i] >= "a" and s[i] <= "z":
            x += chr(ord(s[i]) - (ord("a") - ord("A")))
        elif s[i] >= "A" and s[i] <= "Z": 
            x += s[i]
        else:
            x += s[i]
        i += 1
    return x

print upper("Bing! Wah?")

def reverse(s):
    i = len(s)
    x = ""
    while i > 0:
        x += s[i-1]
        i -= 1
    return x

print reverse("hello")

def countCharInString(s,c):
    i = 0
    count = 0
    while i < len(s):
        if s[i] == c:
            count += 1
            i += 1
        else:
            i += 1
    return count

print countCharInString("Bobby","b")

def stringToInt(s):
    total = 0
    i = 0
    while i < len(s):
        total += int(s[i]) * (10 ** (len(s) - i - 1))
        i += 1
    return total

print stringToInt("9024")

def makeBoxOfNumbers(rows,cols):
    i = 0
    x = 0
    num = 0
    totalString = ""
    while x < rows: 
        while i < cols:
            totalString += str(num)[-1]
            i += 1
            num += 1
        totalString += "\n"
        i = 0
        x += 1
    return totalString
print makeBoxOfNumbers(20,29)

def findInString(part,target):
    i = 0
    if part in target:
        while i < len(target):
            if target[i:len(part) + i] == part:
                return i
            i += 1
    else:
        return -1

print findInString("by", "Abbye by bye")
print findInString('bob', 'bobby')

def removeFromString(s,c):
    i = 0
    newString = ""
    while i < len(s):
        if s[i] != c:
            newString += s[i]
        i += 1
    return newString

print removeFromString('ich bin ein holtzfaller', ' ')
    



    

