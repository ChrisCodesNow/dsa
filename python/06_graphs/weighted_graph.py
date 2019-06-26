from collections import defaultdict

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

        print('Weights:')
        for u in self.g:
            for v in self.g[u]:
                print(f'Edge {u} -- {v} \t weight = {self.weights[u, v]}')


    def __getitem__(self, u):
        return self.g[u]


    def vertices(self):
        return self.num_vertices


    def edge_weight(self, u, v):
        return self.weights[u, v]

if __name__ == '__main__':
    g = Graph(5)

    g.add_edge(0, 1, 1)
    g.add_edge(3, 4, 2)
    g.add_edge(1, 4, 3)
    g.add_edge(1, 3, 4)
    g.add_edge(1, 2, 5)
    g.add_edge(2, 4, 6)
    g.add_edge(0, 2, 7)

    g.print()