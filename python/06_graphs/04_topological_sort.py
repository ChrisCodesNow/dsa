from graph import Graph
# Use DFS to sort topologically

# g is an adj list
from collections import deque, defaultdict
def top_sort(g):
    g_in = in_deg(g)
    g_in_zero = [v for v in g_in if g_in[v] == 0]

    print(g_in)
    visited = set(g_in_zero)
    order = []

    Q = deque(g_in_zero)
    while Q:
        u = Q.popleft()
        order.append(u)

        for v in g[u]:
            if v not in visited:
                Q.append(v)
                visited.add(v)

    return order


# In degree count of input adjacency list
def in_deg(g):
    g_in = defaultdict(int)
    for u in range(g.vertices()):
        g_in[u] += 0
        for v in g[u]:
            g_in[v] += 1

    return g_in


if __name__ == '__main__':
    g = Graph(6)
    g.add_edge(5, 0)
    g.add_edge(5, 2)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    print(top_sort(g))