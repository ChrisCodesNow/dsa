# Kruskal's algorithm for minimum spanning trees
from disjoint_set import DisjointSet
from weighted_graph import Graph

def min_span_tree(g, n):
    edges = get_edges(g)
    edges = sorted(edges, key=lambda edge:edge[2])

    ds = DisjointSet(n)
    min_cost = 0
    for u,v,weight in edges:
        if not ds.are_connected(u, v):
            min_cost += weight
            ds.join(u,v)

    return min_cost

def get_edges(g):
    edges = []
    for (u,v),weight in g.weights.items():
        edges.append((u,v,weight))

    return edges


if __name__ == '__main__':
    # Test
    class Test:
        count = 0
        def run(self, result):
            self.count += 1
            if result:
                print(f"Passed test {self.count}")
            else:
                print(f"Failed test {self.count}")

    t = Test()


    n = 5
    g = Graph(n)

    g.add_edge(0, 1, 1)
    g.add_edge(3, 4, 2)
    g.add_edge(1, 4, 3)
    g.add_edge(1, 3, 4)
    g.add_edge(1, 2, 5)
    g.add_edge(2, 4, 6)
    g.add_edge(0, 2, 7)

    t.run(min_span_tree(g, n) == 11)