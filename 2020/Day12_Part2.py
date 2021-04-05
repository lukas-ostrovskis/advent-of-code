file = open("input.txt", "r")

north = 0
east = 0
wpn = 1
wpe = 10

for line in file:
    if 'F' in line:
        north += int(line[1:]) * wpn
        east += int(line[1:]) * wpe
    elif 'N' in line:
        wpn += int(line[1:])
    elif 'S' in line:
        wpn -= int(line[1:])
    elif 'E' in line:
        wpe += int(line[1:])
    elif 'W' in line:
        wpe -= int(line[1:])
    elif ('L' in line or 'R' in line) and int(line[1:])%360 == 180:
        wpn = -wpn
        wpe = -wpe
    elif ('L' in line and int(line[1:])%360 == 90) or ('R' in line and int(line[1:])%360 == 270):
        temp = wpe
        wpe = -wpn
        wpn = temp
    elif ('L' in line and int(line[1:])%360 == 270) or ('R' in line and int(line[1:])%360 == 90):
        temp = wpe
        wpe = wpn
        wpn = -temp

print(abs(abs(north)+abs(east)))