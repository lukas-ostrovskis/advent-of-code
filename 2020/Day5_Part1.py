def check(line):
    rowL = 0
    rowH = 127
    colL = 0
    colH = 7

    for i in range(7):
        if line[i] == 'F':
            rowH = int((rowL+rowH)/2)
        else:
            rowL = int(((rowL+rowH)/2)+1)
    
    for i in range(3):
        if line[i+7] == 'L':
            colH = int((colL+colH)/2)
        else:
            colL = int(((colL+colH)/2)+1)

    return rowL*8 + colL


file = open("input.txt", "r")

_max = -1
for line in file:
    curr = check(line)
    _max = max(_max, curr)

print(_max)