from collections import defaultdict
class Graph:
    def __init__(self, num_vertices):
        self.g = defaultdict(set)
        for i in range(num_vertices):
            self.g[i]
    
    def add_edge(self, u, v):
        self.g[u].add(v)

    def remove_edge(self, u, v):
        if u in self.g.keys():
            if v in self.g[u]:
                g[u].remove(v)

    def print(self):
        for u in self.g:
            print(f'{u} -> {self.g[u]}')

if __name__ == "__main__":
    g = Graph(3)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)

    g.print()