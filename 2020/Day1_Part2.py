file = open("input.txt", "r")
array = []

for line in file:
    array.append(int(line))

array.sort()


for x in range(len(array)):
    for y in range(x+1, len(array)):
        for z in range(y+1, len(array)):
            if (array[x]+array[y]+array[z]) == 2020:
                print(array[x]*array[y]*array[z])

