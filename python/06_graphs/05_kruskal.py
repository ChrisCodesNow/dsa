# Kruskal's algorithm for minimum spanning trees
from disjoint_set import DisjointSet
def min_span_tree(g, n):
    edges = get_edges(g)
    edges = sorted(edges, key=lambda edge:edge[2])

    ds = DisjointSet(n)
    min_cost = 0
    for u,v,weight in edges:
        if not ds.are_connected(u, v):
            cost += weight
            ds.join(u,v)

    return cost


if __name__ == '__main__':
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