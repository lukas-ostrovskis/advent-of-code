file = open("input.txt", "r")

lines = file.readlines()

sum = 0
visited = {}

for line in lines:
    if 'mask' in line:
        andChange = int(line[7:].replace('1', '0').replace('X', '1'), 2)
        orChange = int(line[7:].replace('X', '0'), 2)
    else:
        memLoc = int(line[4:].split(']')[0])
        num = int(line.split(' ')[2])
        num &= andChange
        num |= orChange

        if memLoc not in visited:
            visited[memLoc] = num
            sum += num
        else:
            sum += (num - visited[memLoc])
            visited[memLoc] = num

print(sum)





    