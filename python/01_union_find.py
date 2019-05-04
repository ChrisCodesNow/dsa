class UnionFind:
    def __init__(self, num_elements):
        self.parent = [-1 for _ in range(num_elements)]
        print(f"Created Union Find of size {num_elements}")


    # Find the root node of the subset
    def find(self, x):
        if self.parent[x] == -1:
            return x
        else:
            return self.find(parent[x])

    # Join subset rooted at x to subset rooted at y
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        self.parent[root_x] = root_y
