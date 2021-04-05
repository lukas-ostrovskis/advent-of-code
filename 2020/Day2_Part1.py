def check(line):
    lineArr = line.split(' ')
    low  = int(lineArr[0])
    high = int(lineArr[1])
    character = lineArr[2]
    psw = lineArr[3]

    if psw.count(character) >= low and psw.count(character) <= high:
        return True
    
    return False


file = open("input.txt", "r")
ans = 0

for line in file:
    if check(line):
        ans = ans+1

print(ans)

