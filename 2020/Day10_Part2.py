visited = set()
value = {}

def sol(arr, currIdx, prevEl):
    if arr[currIdx] - prevEl > 3:
        return 0
    elif currIdx == len(arr)-1:
        return 1
    elif (currIdx, prevEl) in visited:
        return value[(currIdx, prevEl)]
    
    visited.add((currIdx, prevEl))

    value[(currIdx, prevEl)] = sol(arr, currIdx+1, prevEl) + sol(arr, currIdx+1, arr[currIdx])

    return value[(currIdx, prevEl)]


file = open("input.txt", "r")

arr = []

for i in file:
    arr.append(int(i))

arr.sort()

_max = arr[len(arr)-1]
arr.append(_max+3)


print(sol(arr, 0, 0))



