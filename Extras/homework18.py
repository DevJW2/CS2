t = """1,2,3
4,5,6
8,fish,10"""

def makeList(t):
	newList = []
	t = t.split("\n")
	for i in t:
		newList.append(i.split(","))

	return newList

print makeList(t)

def makeTableBody(item):
	output = ""
	for L in item:
		output += "<tr>"
		for n in L:
			output += "<td>" + n + "</td>"
		output += "</tr>\n"
	return output

print makeTableBody(makeList(t))

