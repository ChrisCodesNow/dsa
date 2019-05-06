class UnionFind:
    def __init__(self, num_elements):
        self.parent = [i for i in range(num_elements)]
        self.rank = [0 for _ in range(num_elements)]
        print(f"Created Union Find of size {num_elements}")


    # # Find the root node of the subset
    # def find_non_compress(self, x):
    #     if self.parent[x] == x:
    #         return x
    #     else:
    #         return self.find(parent[x])


    # Compressess tree on recursive call
    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]


    # Connect subset rooted at x to subset rooted at y
    # def union(self, x, y):
    def connect(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        self.parent[root_x] = root_y


    # Performs union by rank, keeping tree height minimal
    def join(self, x, y):
        # Only union if in distinct subsets
        if self.find(x) != self.find(y):
            if self.rank[x] < self.rank[y]:
                self.connect(x, y)
            elif self.rank[y] < self.rank[x]:
                self.connect(y, x)
            else:
                self.connect(x, y)
                root_y = self.find(y)
                self.rank[root_y] += 1


    # Connect each susbset parent to all its direct children
    # O(n)
    def compress(self):
        for i in range(len(self.parent)):
            self.parent[i] = self.find(i)

        # Check what happens to rank


    def get_parent(self):
        return self.parent[:]


# Tests
if __name__ == '__main__':
    ds = UnionFind(8)
    print(ds.get_parent())
    print()
    
    ds.join(1, 0)
    ds.join(3, 2)
    ds.join(5, 4)
    print(ds.get_parent())
    print()

    ds.join(1, 3)
    print(ds.get_parent())
    ds.compress()
    print()
    print(ds.get_parent())