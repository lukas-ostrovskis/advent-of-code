file = open("input.txt", "r")

earliest = int(file.readline())
buses = file.readline().split(",")
buses = [int(x) for x in buses if x != 'x']

minBus = buses[0]
minDiff = (int((earliest/buses[0]))+1)*buses[0] - earliest

for i in range(1, len(buses)):
    curr = (int((earliest/buses[i]))+1)*buses[i] - earliest
    if minDiff > curr:
        minDiff = curr
        minBus = buses[i]

    

print(minBus*minDiff)