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

seats = []
for line in file:
    curr = check(line)
    seats.append(curr)

seats.sort()

for i in range(1, len(seats)-1):
    if not (seats[i-1]+1 == seats[i] and seats[i]+1 == seats[i+1]):
        print(seats[i])