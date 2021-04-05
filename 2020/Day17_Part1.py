file = open("input.txt", "r")

map = []

for line in file:
    curr = list(line)
    if '\n' in curr:
        curr.remove('\n')
    map.append(curr)



inactive = set()
active = set()
adjacent = {}
dir = [(0, -1, 0), (0, 1, 0), (-1, 0, 0), (1, 0, 0), (-1, -1, 0), (-1, 1, 0), (1, -1, 0), (1, 1, 0), 
(0, -1, 1), (0, 1, 1), (-1, 0, 1), (1, 0, 1), (-1, -1, 1), (-1, 1, 1), (1, -1, 1), (1, 1, 1), (0, 0, 1),
(0, -1, -1), (0, 1, -1), (-1, 0, -1), (1, 0, -1), (-1, -1, -1), (-1, 1, -1), (1, -1, -1), (1, 1, -1), (0, 0, -1)]

for i in range(0, len(map)):
    for j in range(0, len(map[0])):       
        adjacent[(i,j,0)] = []
        if map[i][j] == '.':
            inactive.add((i,j,0))
            for tuple in dir:
                adjacent[(i,j,0)].append((i+tuple[0], j+tuple[1], tuple[2]))
        elif map[i][j] == '#':
            active.add((i,j,0)) 
            for tuple in dir:
                adjacent[(i,j,0)].append((i+tuple[0], j+tuple[1], tuple[2]))
                inactive.add((i+tuple[0], j+tuple[1], tuple[2]))
                if (i+tuple[0], j+tuple[1], tuple[2]) not in adjacent:
                    adjacent[(i+tuple[0], j+tuple[1], tuple[2])] = []

inactiveCopy = set()
activeCopy = set()

for i in range(6):
    inactiveCopy = inactive.copy()
    activeCopy = active.copy()
    neighboursToAdd = []

    for cube in inactiveCopy:
        if [adj in activeCopy for adj in adjacent[cube]].count(True) == 3:
            inactive.remove(cube)
            active.add(cube)
            for adj in adjacent[cube]:
                neighboursToAdd.append(adj)


    for cube in activeCopy:
        activeNeighbours = [adj in activeCopy for adj in adjacent[cube]].count(True)
        if  activeNeighbours != 2 and activeNeighbours != 3:
            active.remove(cube)
            inactive.add(cube)
    

    for n in neighboursToAdd:
        if n not in active and n not in inactive:
            inactive.add(n)

print((1,1,1) in active)
print(len(active))

    