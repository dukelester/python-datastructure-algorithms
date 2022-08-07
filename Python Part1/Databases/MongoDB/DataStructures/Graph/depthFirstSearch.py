def depthFirstSearch(graph, startPoint):
    if startPoint is None:
        return 0
    stack = [ startPoint ]

    while len(stack) > 0:
        current = stack[-1]
        stack.pop()
        print(current)
        for point in graph[current]:
            stack.append(point)
        print(stack)

graph ={
    "a":['i','n'],
    'b':[], 
    'c':['h', 'k']

}

depthFirstSearch(graph, 'a')

