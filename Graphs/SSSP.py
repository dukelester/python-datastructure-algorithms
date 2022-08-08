class Graph:
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def addEdge(self, vertex, edge):
        self.graph_dict[vertex] = edge


    def breadhFirstSearch(self, start, end):
        queue = [ ]
        queue.append([ start ])

        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            else:
                for adj in self.graph_dict.get(node, []):
                    new_path = list(path)
                    new_path.append(adj)
                    queue.append(new_path)

customDict = { "a" : ["b", "c"],
               "b" : ["d", "g"],
               "c" : ["d", "e"],
               "d" : ["f"],
               "e" : ["f"],
               "g" : ["f"]
            }


graph = Graph(customDict)
print(graph.breadhFirstSearch('a','g'))
print(graph.breadhFirstSearch('g','d'))