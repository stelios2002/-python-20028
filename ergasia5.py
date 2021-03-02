import random

SOS = []
print("give height:")
ayis = input()
ayis = int(ayis)
print("give width:")
axis = input()
axis = int(axis)
for f in range(100):
    list1 = []
    list1len = (ayis*axis)
    list1len2 = float(list1len)
    for i in range(list1len):
            if i > list1len2/2:
                list1.append("O")
            else:
                list1.append("S")
    random.shuffle(list1)
    list2 = []
    for y in range(ayis):
        list2.append([])
        for x in range(axis):
                list2[y].append(list1.pop(0))
    SOS.append(0)
    for x in range(axis-2):
        for y in range(ayis):
            if list2[y][x] == "S" and list2[y][x+1] == "O" and list2[y][x+2] == "S":
                SOS[f] += 1
    for x in range(axis):
        for y in range(ayis-2):
            if list2[y][x] == "S" and list2[y+1][x] == "O" and list2[y+2][x] == "S":
                SOS[f] += 1
    for x in range(axis-2):
        for y in range(ayis-2):
            if list2[y][x] == "S" and list2[y+1][x+1] == "O" and list2[y+2][x+2] == "S":
                SOS[f] += 1
    for x in range(axis-2):
        for y in range(ayis-2):
            if list2[y+2][x] == "S" and list2[y+1][x+1] == "O" and list2[y][x+2] == "S":
                SOS[f] += 1

sumSOS=0
for l in range(len(SOS)-1):
    sumSOS += SOS[l]
avSOS = sumSOS/len(SOS)
print("Ο μέσος όρος των SOS είναι για 100 φορές με το ίδιο μέγεθος: ", avSOS)
