file = open("input.txt", "r")

map = []

for line in file:
    map.append(line[:-1])


ans = 0
i = 0
j = 0

while i < len(map):
    if(map[i][j] == '#'): 
        ans = ans+1
    
    i = i+1
    j = (j+3) % len(map[0])
    

print(ans)