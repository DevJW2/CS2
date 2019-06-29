def pigLatin(c):
    i = 0
    while i < len(c):
        if c[0] in "aeiouAEIOU":
                return c + "hay"
        elif c[i] in "aeiouAEIOU":
                return c[c.index(c[i]):] + c[:c.index(c[i])] + "ay"
        i += 1
    return c

word = pigLatin("By")
print(word)