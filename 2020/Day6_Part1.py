def check(group):
    return len(set(group))

file = open("input.txt", "r")

lines = file.readlines()
cnt = 0

group = ""
for i in range(len(lines)):
    if(lines[i] != "\n"):
        group = group + lines[i][:-1]
    else:
        cnt = cnt + check(group)
        group = ""

cnt = cnt + check(group)

print(cnt)