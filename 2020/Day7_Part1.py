# Input preprocessed for easier handling:

    # dim silver contain posh fuchsia.
    # wavy olive contain striped olive, dull cyan.
    # dull coral contain dim olive, muted violet, dark gray.
    # bright olive contain light indigo, dark coral.




from string import ascii_lowercase

def bfs(graph, start):
    result = -1
    visited = set()
    queue = []
    queue.append(start)

    while len(queue) > 0:
        curr = queue.pop(0)
        
        if curr in visited:
            continue
        
        result += 1
        visited.add(curr)

        if curr in graph:
            for i in graph[curr]:
                    queue.append(i)
    
    print(result)


file = open("input.txt", "r")

lines = file.readlines()

graph = {}
for i in range(len(lines)):
    bigger = lines[i].split(" contain ")[0]
    smaller = lines[i].split(" contain ")[1][:-2].split(", ")

    for j in smaller:
        if j not in graph:
            graph[j] = []
        graph[j].append(bigger)

bfs(graph, "shiny gold")