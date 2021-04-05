file = open("input.txt", "r")

numbers = file.readline().split(',')
numbers = [int(i) for i in numbers]

visited = {}

for i in range(0, len(numbers)):
    visited[numbers[i]] = i


prev = 0
curr = 0

part1 = 2020
part2 = 30000000

# Here either part1 or part2 is chosen for the right range limit

for i in range(len(numbers)+1, part2):
    if prev in visited:
        curr = (i-1) - visited[prev]
    else:
        curr = 0

    visited[prev] = i-1
    prev = curr
print(prev)



