from collections import defaultdict

# class Edge:
#     def __init__(self, u, v, weight):
#         self.u = u
#         self.v = v
#         self.weight = weight

#     def __str__(self):
#         return f'Edge: {self.u} - {self.v} \t weight = {self.weight}'


class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.g = defaultdict(set)
        self.weights = dict()
    
    def add_edge(self, u, v, weight):
        self.g[u].add(v)
        self.weights[(u,v)] = weight

    def remove_edge(self, u, v):
        if u in self.g.keys():
            if v in self.g[u]:
                self.g[u].remove(v)
                del weights[(u, v)]

    def print(self):
        for u in self.g:
            print(f'{u} -> {self.g[u]}')


    def __getitem__(self, u):
        return self.g[u]

    def vertices(self):
        return self.num_vertices