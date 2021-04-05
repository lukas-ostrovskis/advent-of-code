def calc(slopeDown, slopeRight):
    ans = 0
    i = 0
    j = 0

    while i < len(map):
        if(map[i][j] == '#'): 
            ans = ans+1
        
        i = i+slopeDown
        j = (j+slopeRight) % len(map[0])
    
    return ans



file = open("input.txt", "r")

map = []

for line in file:
    map.append(line[:-1])

a = calc(1,1)
b = calc(1,3)
c = calc(1,5)
d = calc(1,7)
e = calc(2,1)


print(a*b*c*d*e)