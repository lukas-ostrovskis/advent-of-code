def invalid(arr):
    curr = set()
    for i in range(25):
        curr.add(arr[i])

    for i in range(25, len(arr)):

        valid = False
        for j in curr:
            if (arr[i]-j) in curr:
                valid = True
                curr.add(arr[i])
                break
    
        if not valid:
            return arr[i]
            break

        curr.remove(arr[i-25])



file = open("input.txt", "r")

arr = []

for i in file:
    arr.append(int(i))

invalidNumber = invalid(arr)
print(invalidNumber)

prefixSum = []
prefixSum.append(arr[0])

for i in range(1, len(arr)):
    prefixSum.append(prefixSum[i-1] + arr[i])

found = False
for i in range(len(prefixSum)):

    if found:
        break

    if prefixSum[i] == invalidNumber:
        print(i)
        found = True
        break
    
    for j in range(i):
        if prefixSum[i]-prefixSum[j] == invalidNumber:
            left = j+1
            right = i
            found = True
            break

_min = 100000000000000000
_max = -1

for i in range(left, right+1):
    _min = min(_min, arr[i])
    _max = max(_max, arr[i])

print(_min+_max)

