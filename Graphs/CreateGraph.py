class Graph:
    def __init__(self, graph_dictonary=None):
        if graph_dictonary is None:
            graph_dictonary = {}
        self.graph_dictonary = graph_dictonary

    def addEdge(self, edge, vertex):
        self.graph_dictonary[vertex].append(edge)

    def breathFisrtTraversal(self, vertex):  # O(V + E)
        visited = [vertex]
        queue = [ vertex ]

        while queue:
            current_vertext = queue.pop(0)
            print(current_vertext)

            for adj in self.graph_dictonary[current_vertext]:
                if adj not in visited:
                    visited.append(adj)
                    queue.append(adj)



    def depthFirstSearch(self, vertex):
        visited = [ vertex]
        stack = [ vertex]

        while stack:
            current_vertex  = stack.pop()
            print(current_vertex)
            for adj in self.graph_dictonary[current_vertex]:
                if adj not in visited:
                    visited.append(adj)
                    stack.append(adj)



customDict = { "a" : ["b","c"],
            "b" : ["a", "d", "e"],
            "c" : ["a", "e"],
            "d" : ["b", "e", "f"],
            "e" : ["d", "f", "c"],
            "f" : ["d", "e"]
               }


graph = Graph(customDict)
graph.addEdge("a", "a")
graph.breathFisrtTraversal("a" )
graph.depthFirstSearch('f')