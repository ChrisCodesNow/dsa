from graph import Graph
from collections import defaultdict

# Recursive depth first search
# def dfs(g, src):
#     visited = set()
#     previous = defaultdict(set)
#     previous[src] = None
#     dfs_r(g, src, visited, previous)
#     return previous


def dfs_r(g, src, visited, previous):
    visited.add(src)
    for v in g[src]:
        if v not in visited:
            previous[v] = src
            dfs_r(g, v, visited, previous)

        
# Iterative depth first search
def dfs(g, src):
    visited = set([src])
    previous = defaultdict(set)
    previous[src] = None
    S = [src]

    while S:
        u = S.pop()
        for v in g[u]:
            if v not in visited:
                S.append(v)
                visited.add(v)
                previous[v] = u

    return previous      



def build_path(src, dest, previous):
    if dest not in previous:
        return []
    
    return build_path(src, previous[dest], previous) + [dest]


def are_connected(g, src, dest):
    previous = dfs(g, src)
    path = build_path(src, dest, previous)

    print(f'{src} to {dest} : {path}')

    return path and (path[0] == src and path[-1] == dest)


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


    g = Graph(6)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 6)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    # g.add_edge(5, 6)
    g.add_edge(6, 2)

    # g.print()
    t.run(are_connected(g, 0, 5) == True)      # to print: [0, 1, 3, 5] or [0, 2, 3, 5]
    are_connected(g, 1, 6)