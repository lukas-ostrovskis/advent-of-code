# Input preprocessed for easier handling:
    # dim silver contain 3 posh fuchsia.
    # wavy olive contain 1 striped olive, 1 dull cyan.
    # dull coral contain 1 dim olive, 5 muted violet, 2 dark gray.
    # bright olive contain 3 light indigo, 3 dark coral.


import string

visited = set()
value = {}

def rec(graph, start):
    result = 1
    if start not in graph:
        return 1
    elif start in visited:
        return value[start]

    for i in graph[start]:
        result += i[0] * rec(graph, i[1])

    visited.add(start)
    value[start] = result

    return result



file = open("input.txt", "r")

lines = file.readlines()

graph = {}
for i in range(len(lines)):
    bigger = lines[i].split(" contain ")[0]
    smaller = lines[i].split(" contain ")[1][:-2].split(", ")
    
    sep = " "
    for i in range(len(smaller)):
        smaller[i] = (int(smaller[i].split(" ")[0]), sep.join(smaller[i].split(" ")[1:]))


    if bigger not in graph:
        graph[bigger] = []

    for i in smaller:
        graph[bigger].append(i)

print(rec(graph, "shiny gold")-1)
