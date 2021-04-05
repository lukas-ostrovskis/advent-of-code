from string import ascii_lowercase

def check(group):
    cnt = 0
    for i in ascii_lowercase:
        cnt += all(i in group[j] for j in range(len(group)))
    
    return cnt

file = open("input.txt", "r")

lines = file.readlines()
cnt = 0

group = []
for i in range(len(lines)):
    if(lines[i] != "\n"):
        if(lines[i][:0] == "\n"):
            group.append(lines[i][:-1])
        else:
            group.append(lines[i])
    else:
        cnt += check(group)
        group = []

cnt += check(group)

print(cnt)