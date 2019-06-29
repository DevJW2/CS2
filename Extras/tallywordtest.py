def TallyWords1(text):
    t = 0
    words = []
    tallys = []
    count = 0
    text = text.split()
    for i in text:
        i = i.lower().strip(""""'.,?!""")
        if i not in words:
            words.append(i)
    for n in words:
        for c in text:
            if n == c.lower().strip(""""'.,?!"""):
               count += 1
        tallys.append(count)
        count = 0
    while t < len(words):
        print str(words[t]) + ":" + str(tallys[t])
        t += 1



print TallyWords1("""a
b a! C a b!!!! "Fish" happy meal.
fish?""")


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

def totalWords(text, value):
    words,tallys = TallyWords(text)
    oneWord = 0
    oneWordList = []
    topNum = []
    t = 0
    item = 0
    if value == 0:
        return len(text.split())
    elif value == 1:
        return len(words)
    elif value == 2:
        for i in tallys:
            if i == 1:
                oneWord += 1
        return oneWord
    elif value == 3:
        while len(oneWordList) < 100 and t < len(tallys):
            if tallys[t] == 1:
                oneWordList.append(words[t])
            t += 1
        return oneWordList
    elif value == 4:
        while len(topNum) < 10:
            topNum.append(words[tallys.index(max(tallys))])
            words.remove(words[tallys.index(max(tallys))])
            tallys.remove(max(tallys))
        return topNum






