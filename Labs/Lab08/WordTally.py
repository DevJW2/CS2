def TallyWords(text):
    words = []
    tallys = []
    count = 0
    text = text.split()
    for i in text:
        i = i.lower().strip(""".,":';()-?!""")
        if i not in words:
            words.append(i)
    for n in words:
        for c in text:
            if n == c.lower().strip(""".,":';()-?!"""):
               count += 1
        tallys.append(count)
        count = 0
    return words,tallys

def printTally(text):
    value = ""
    t = 0
    words,tallys = TallyWords(text)
    while t < len(words):
        value += str(words[t]) + ":" + str(tallys[t]) + "\n"
        t += 1
    return value



filename = "dante.txt"
f = open(filename, 'r')

text = f.read()

print "The WHOLE BOOK:"
print printTally(text[text.index("Canto"):])

print "The list of words:"
print text.split()[:100]

f.close()
