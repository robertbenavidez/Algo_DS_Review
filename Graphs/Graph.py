class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)
    # Time O(V + E) Space O(V + E)
    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            dequeueVertex = queue.pop(0)
            print(dequeueVertex)
            for adjacentVertex in self.gdict[dequeueVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex) 
                    queue.append(adjacentVertex)
    # Time O(V + E) Space O(V + E)
    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            popVertex = stack.pop()
            print(popVertex)
            for adjacentVertex in self.gdict[popVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)


customDict = {
    "a" : ["b", "c"],
    "b" : ["a", "d", "e"],
    "c" : ["a", "e"],
    "d" : ["b", "e", "f"],
    "e" : ["d", "f"],
    "f" : ["d", "e"],
}
graph = Graph(customDict)
# graph.bfs("a")
graph.dfs("a")