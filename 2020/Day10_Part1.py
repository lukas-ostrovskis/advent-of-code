file = open("input.txt", "r")

arr = []
arr.append(0)

for i in file:
    arr.append(int(i))

arr.sort()

ones = 0
threes = 1

for i in range(1, len(arr)):
    ones += arr[i]-arr[i-1] == 1
    threes += arr[i]-arr[i-1] == 3


print(ones*threes)



