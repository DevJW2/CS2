f = open("values.txt", "r")
values = f.read()
f.close()

f1 = open("operations.txt", "r")
operations = f1.read()
f1.close()

values = values.split("\n")
operations = operations.split("\n")
count = 0

for i in operations:
    count += 1
    operations[operations.index(i)] = i.split("+-/*")
    if i in values[0]:
        operations[operations.index(i)] = values[count][values[0].find(i)]