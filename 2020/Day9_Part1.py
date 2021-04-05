file = open("input.txt", "r")

arr = []

for i in file:
    arr.append(int(i))

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
        print(arr[i])
        break

    curr.remove(arr[i-25])

