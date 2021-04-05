file = open("input.txt", "r")

lines = file.readlines()
visited = set()
idx = 0
acc = 0

while(1):
    if idx in visited:
        break
    visited.add(idx)

    inst = (lines[idx].split(" ")[0], int(lines[idx].split(" ")[1]))
    
    if inst[0] == "acc":
        acc += inst[1]
        idx += 1
    elif inst[0] == "jmp":
        idx += inst[1]
    else:
        idx += 1

