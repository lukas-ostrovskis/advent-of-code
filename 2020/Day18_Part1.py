def calculate(line, pos):
    result = 0
    operator = ''
    i = pos
    while i < len(line):
        if line[i] in ['+','*']:
            operator = line[i]
        elif line[i] not in ['(',')']:
            if operator == '':
                result = int(line[i])
            else:
                if operator == '+':
                    result += int(line[i])
                else:
                    result *= int(line[i])
        elif line[i] == '(':
            recAns = calculate(line, i+1)
            if operator == '':
                result = recAns[0]
            elif operator == '+':
                result += recAns[0]
            else:
                result *= recAns[0]
            i = recAns[1]   
        elif line[i] == ')':
            break
        i += 1
    return (result, i)

        


file = open("input.txt", "r")

lines = file.readlines()

sum = 0
for line in lines:
    sum += calculate(list(line.replace(' ', '').replace('\n','')), 0)[0]

print(sum)

