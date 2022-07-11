#creating the algorithm to find the path from one vertex to  the other

#using the adjacent matrix
from collections import defaultdict

class Graph: #create a graph
    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = defaultdict(list) 

    #add an edge to the graph
    def add_edge(self, edge, data):
        self.graph[edge].append(data)

    #perfrom the deep first search
    def deepFisrtSearch(self, data, visited_vertex):
        visited_vertex[data] = True
        print(data, end="")
        for i in self.graph[data]:
            if not visited_vertex[i]:
                self.deepFisrtSearch(i, visited_vertex) #recursion 

    def fill_order(self, data, visited_vertex, stack):
        visited_vertex[data] = True
        for i in self.graph[data]:
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex,stack) #recursion 

        stack = stack.append(data)

    #transpose the matrix ==> change the rows into columns and columns into rows
    def transpose(self):
        graph = Graph(self.vertex)

        for i in self.graph:
            for j in self.graph[i]:
                graph.add_edge(j, i)
            print(graph, 'the graph transposed')
        return graph

    #print the stronly connected components

    def printStronglyConnected(self):
        stack = [] #stack to store the components
        visited_vertex = [False] * (self.vertex)
        
        for i in range(self.vertex):
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)

        graph = self.transpose()

        visited_vertex = [False] * ( self.vertex)

        while stack:
            i = stack.pop()
            if not visited_vertex[i]:
                graph.deepFisrtSearch(i, visited_vertex)

        print("***********done**********")
 


mygraph = Graph(8)
mygraph.add_edge(0, 1)
mygraph.add_edge(1, 2)
mygraph.add_edge(2, 3)
mygraph.add_edge(2, 4)
mygraph.add_edge(3, 0)
mygraph.add_edge(4, 5)

mygraph.add_edge(6, 4)
mygraph.add_edge(6, 7)

print("The Strongly connected components are:: ")

mygraph.printStronglyConnected()
        

