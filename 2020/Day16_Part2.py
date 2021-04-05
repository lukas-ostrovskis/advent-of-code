idx = 0
intervals = {}
numbers = {}
fields = []

def intervalSetup(lines):
    global idx
    while idx < len(lines):
        if lines[idx] == '\n':
            idx += 1
            break
        
        field = lines[idx].split(':')[0]
        fields.append(field)
        left1 = int([i.split('-') for i in lines[idx].split(': ')[1].split(' or ')][0][0])
        right1 = int([i.split('-') for i in lines[idx].split(': ')[1].split(' or ')][0][1])
        left2 = int([i.split('-') for i in lines[idx].split(': ')[1].split(' or ')][1][0])
        right2 = int([i.split('-') for i in lines[idx].split(': ')[1].split(' or ')][1][1])

        intervals[field] = []
        intervals[field].append(left1)
        intervals[field].append(right1)
        intervals[field].append(left2)
        intervals[field].append(right2)

        for i in range(left1, right1+1):
            numbers[i] = 1
        for i in range(left2, right2+1):
            numbers[i] = 1

        idx += 1

def readMyTicket(lines):
    global idx
    idx += 1
    return [int(i) for i in lines[idx].split(',')]

def discardInvalid(lines):
    global idx
    validTickets = []
    while idx < len(lines):
        valid = True
        for i in lines[idx].split(','):
            if int(i) not in numbers:
                valid = False
        if valid:
            validTickets.append([int(i) for i in lines[idx].split(',')])
        idx += 1
    return validTickets


file = open("input.txt", "r")

lines = file.readlines()

intervalSetup(lines)
myTicket = readMyTicket(lines)
idx += 3
validTickets = discardInvalid(lines)


possibleFieldPositions = {}
position_fieldArr = []

for field in fields:
    possibleFieldPositions[field] = []
    for i in range(0, len(validTickets[0])):
        valid = True
        for validTicket in validTickets:
            if not ((validTicket[i] >= intervals[field][0] and validTicket[i] <= intervals[field][1]) or (validTicket[i] >= intervals[field][2] and validTicket[i] <= intervals[field][3])):
                valid = False
                break
        if valid:
            possibleFieldPositions[field].append(i)

    position_fieldArr.append((possibleFieldPositions[field], field))
    
position_fieldArr.sort(key=lambda x: len(x[0]))

takenPos = {}
finalPositions = {}

for i in position_fieldArr:
    for j in i[0]:
        if j not in takenPos:
            takenPos[j] = True
            finalPositions[i[1]] = j
            break

departureFieldCounter = 0
result = 1
for field in fields:
    result *= myTicket[finalPositions[field]]
    departureFieldCounter += 1
    if departureFieldCounter == 6:
        break

print(result)


            






