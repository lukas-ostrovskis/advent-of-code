idx = 0
numbers = {}

def intervalSetup(lines):
    global idx
    while idx < len(lines):
        if lines[idx] == '\n':
            idx += 1
            break

        left1 = int([i.split('-') for i in lines[idx].split(': ')[1].split(' or ')][0][0])
        right1 = int([i.split('-') for i in lines[idx].split(': ')[1].split(' or ')][0][1])
        left2 = int([i.split('-') for i in lines[idx].split(': ')[1].split(' or ')][1][0])
        right2 = int([i.split('-') for i in lines[idx].split(': ')[1].split(' or ')][1][1])

        for i in range(left1, right1+1):
            numbers[i] = 1
        for i in range(left2, right2+1):
            numbers[i] = 1

        idx += 1

def readMyTicket(lines):
    global idx
    idx += 1
    return [int(i) for i in lines[idx].split(',')]

def checkNearbyTickets(lines):
    global idx
    result = 0
    while idx < len(lines):
        for i in lines[idx].split(','):
            if int(i) not in numbers:
                result += int(i)
        idx += 1
    return result


file = open("input.txt", "r")

lines = file.readlines()

intervalSetup(lines)
myTicket = readMyTicket(lines)
idx += 3
print(checkNearbyTickets(lines))




