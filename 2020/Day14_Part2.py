file = open("input.txt", "r")

lines = file.readlines()

sum = 0
visited = {}
combs = []


def combinations(bitmask, pos):
    if(pos == len(bitmask)):
        combs.append(''.join(bitmask))
    elif bitmask[pos] == 'X':
        bitmask[pos] = '0'
        combinations(bitmask, pos+1)
        bitmask[pos] = '1'
        combinations(bitmask, pos+1)
        bitmask[pos] = 'X'
    else:
        combinations(bitmask, pos+1)
    

for line in lines:
    if 'mask' in line:
        curr = list(line[7:])
        orChange = int(line[7:].replace('X', '0'), 2)
    else:
        memLoc = int(line[4:].split(']')[0])
        memLoc |= orChange
        
        memLocBin = list(bin(memLoc)[2:])
        while len(memLocBin) < 36:
            memLocBin.insert(0, '0')

        for i in range(0, 36):
            if(curr[i] == 'X'):
                memLocBin[i] = 'X'
        
        combs.clear()
        combinations(memLocBin, 0)

        num = int(line.split(' ')[2])

        for c in combs:
            if c not in visited:
                visited[c] = num
                sum += num
            else:
                sum += (num - visited[c])
                visited[c] = num

print(sum)





    