# Use DFS to sort topologically

# g is an adj list
from collections import deque, defaultdict
def top_sort(g):
    g_in = in_deg(g)
    g_in_zero = [v for v in g_in if g_in[v] == 0]

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
    for u in g:
        for v in g[u]:
            g_in[v] += 1

    return g_in