from graph import Graph

'''
Modified version of dfs.
Keep track of ancestors of current vertex
'''
def is_cyclic(g):
    visited = set()
    ancestors = set()
    return is_cyclic_r(g, 0, visited, ancestors)


def is_cyclic_r(g, u, visited, ancestors):
    visited.add(u)
    curr_ancestors = set([u]) | ancestors
    for v in g[u]:
        if v in ancestors:
            return True

        elif v not in visited:
            if is_cyclic_r(g, v, visited, curr_ancestors):
                return True
            
    return False


if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 6)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    g.add_edge(5, 6)
    g.add_edge(6, 2)

    g.print()
    if is_cyclic(g):
        print('G is cyclic')
    else:
        print('G is not cyclic')