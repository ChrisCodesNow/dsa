# Iterative approach
from graph import Graph
from collections import defaultdict, deque

def bfs(g, src):
    visited = set([src])
    traversal = []
    
    Q = deque([src])
    while Q:
        u = Q.popleft()
        traversal.append(u)
        for v in g[u]:
            if v not in visited:
                Q.append(v)
                visited.add(v)

    return traversal


if __name__ == "__main__":
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

    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    src = 2
    print(bfs(g, src))
    t.run(bfs(g, src) == [2, 0, 3, 1])