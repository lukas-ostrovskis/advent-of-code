file = open("input.txt", "r")

north = 0
east = 0
deg = 90

for line in file:
    if 'N' in line or ('F' in line and deg == 0):
        north += int(line[1:])
    elif 'S' in line or ('F' in line and deg == 180):
        north -= int(line[1:])
    elif 'E' in line or ('F' in line and deg == 90):
        east += int(line[1:])
    elif 'W' in line or ('F' in line and deg == 270):
        east -= int(line[1:])
    elif 'L' in line:
        deg = (deg-int(line[1:])) % 360
    elif 'R' in line:
        deg = (deg+int(line[1:])) % 360


print(abs(abs(north)+abs(east)))