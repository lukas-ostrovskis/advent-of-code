def test(lines):
    visited = set()
    idx = 0
    acc = 0


    while(1):
        if idx in visited:
            break
        elif idx == len(lines):
            print(acc)
            break

        visited.add(idx)

        inst = lines[idx]
        
        if inst[0] == "acc":
            acc += inst[1]
            idx += 1
        elif inst[0] == "jmp":
            idx += inst[1]
        else:
            idx += 1


file = open("input.txt", "r")

lines = [(line.split(" ")[0], int(line.split(" ")[1])) for line in file.readlines()]

for i in range(len(lines)):
    if lines[i][0] == "nop":
        lines[i] = ("jmp", lines[i][1])
        test(lines)
        lines[i] = ("nop", lines[i][1])
    elif lines[i][0] == "jmp":
        lines[i] = ("nop", lines[i][1])
        test(lines)
        lines[i] = ("jmp", lines[i][1])
