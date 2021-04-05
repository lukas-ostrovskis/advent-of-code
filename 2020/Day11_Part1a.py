file = open("input.txt", "r")

map = []

for line in file:
    curr = list('.' + line + '.')
    if '\n' in curr:
        curr.remove('\n')

    map.append(curr)

map.insert(0, list("." * len(map[0])))
map.append(list('.' * len(map[0])))

dir = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

oldCnt = -1
cnt = 0
mapCopy = []

for i in range(len(map)):
    mapCopy.append(map[i].copy())

while oldCnt != cnt:
    oldCnt = cnt

    for i in range(len(map)):
        mapCopy[i] = map[i].copy()

    for i in range(1, len(map)-1):
        for j in range(1, len(map[1])-1):
            if mapCopy[i][j] == 'L' and not '#' in [mapCopy[i+pair[0]][j+pair[1]] for pair in dir]:
                map[i][j] = '#'
                cnt += 1
            elif mapCopy[i][j] == '#' and "".join([mapCopy[i+pair[0]][j+pair[1]] for pair in dir]).count('#') >= 4:
                map[i][j] = 'L'
                cnt -= 1
print(cnt)
        
    