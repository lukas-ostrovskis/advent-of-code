def find(map, i, j, adjacent):
    for l in range(j-1, 0, -1):
        if map[i][l] == 'L':
            adjacent[(i,j)].append((i,l))
            break
    for r in range(j+1, len(map[0])-1):
        if map[i][r] == 'L':
            adjacent[(i,j)].append((i,r))
            break
    for u in range(i-1, 0, -1):
        if map[u][j] == 'L':
            adjacent[(i,j)].append((u,j))
            break
    for d in range(i+1, len(map)-1):
        if map[d][j] == 'L':
            adjacent[(i,j)].append((d,j))
            break
    for lu in range(1, min(i,j)):
        if map[i-lu][j-lu] == 'L':
            adjacent[(i,j)].append((i-lu,j-lu))
            break
    for ru in range(1, min(i,len(map[0])-1-j)):
        if map[i-ru][j+ru] == 'L':
            adjacent[(i,j)].append((i-ru,j+ru))
            break
    for ld in range(1, min(len(map)-1-i, j)):
        if map[i+ld][j-ld] == 'L':
            adjacent[(i,j)].append((i+ld,j-ld))
            break
    for rd in range(1, min(len(map)-1-i, len(map[0])-1-j)):
        if map[i+rd][j+rd] == 'L':
            adjacent[(i,j)].append((i+rd,j+rd))
            break

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
            find(map, i, j, adjacent)

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
        if [adj in occupiedCopy for adj in adjacent[seat]].count(True) >= 5:
            occupied.remove(seat)
            empty.add(seat)

print(len(occupied))

    