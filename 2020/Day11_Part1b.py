file = open("input.txt", "r")

map = []

for line in file:
    curr = list('.' + line + '.')
    if '\n' in curr:
        curr.remove('\n')

    map.append(curr)

map.insert(0, list("." * len(map[0])))
map.append(list('.' * len(map[0])))

empty = set()
occupied = set()
adjacent = {}
dir = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
cnt = -1

for i in range(1, len(map)):
    for j in range(1, len(map[0])):
        if map[i][j] == 'L':
            empty.add((i,j))
            adjacent[(i,j)] = []
            for pair in dir:
                adjacent[(i,j)].append((i+pair[0], j+pair[1]))

emptyCopy = set()
occupiedCopy = set()

while cnt != len(occupied):
    cnt = len(occupied)
    
    emptyCopy = empty.copy()
    occupiedCopy = occupied.copy()

    for seat in emptyCopy:
        if not any(adj in occupiedCopy for adj in adjacent[seat]):
            empty.remove(seat)
            occupied.add(seat)

    for seat in occupiedCopy:
        if [adj in occupiedCopy for adj in adjacent[seat]].count(True) >= 4:
            occupied.remove(seat)
            empty.add(seat)

print(len(occupied))

    