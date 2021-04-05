# Example input: 7,13,x,x,59,x,31,19
# t mod 7 = 0
# t+1 mod 13 = 0
# t+4 mod 59 = 0
# t+6 mod 31 = 0
# t+7 mod 19 = 0

def chineseRemainder(buses, remainder):
    res = 0
    N = 1
    for x in buses:
        N *= x

    for i in range(0, len(buses)):
        pp = N // buses[i]
        res += remainder[i] * pow(pp, -1, buses[i]) * pp
    
    return res % N

file = open("input.txt", "r")

buses = file.readline().split(",")
remainder = [-i for i in range(0, len(buses)) if buses[i] != 'x']
buses = [int(x) for x in buses if x != 'x']

print(chineseRemainder(buses, remainder))





    