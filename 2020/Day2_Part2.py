def check(line):
    lineArr = line.split(' ')
    first  = int(lineArr[0])
    second = int(lineArr[1])
    character = lineArr[2]
    psw = lineArr[3]

    if (psw[first-1] == character and not psw[second-1] == character) or (psw[second-1] == character and not psw[first-1] == character):
        return True

    return False


file = open("input.txt", "r")
ans = 0

for line in file:
    if check(line):
        ans = ans+1

print(ans)

