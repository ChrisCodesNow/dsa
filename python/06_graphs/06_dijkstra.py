# Dijkstra's shortest path algorithm on a weighted graph
from weighted_graph import Graph
import heapq

def shortest_path(graph, src):
    distance = {u:float('inf') for u in range(graph.vertices())}
    distance[src] = 0

    visited = set()
    Q = [(weight, u) for u,weight in distance.items()]
    heapq.heapify(Q)
    while Q:
        print(Q)
        weight, u = heapq.heappop(Q)
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                update_distance = distance[u] + graph.edge_weight(u, v)
                distance[v] = min(update_distance, distance[v])

    return distance


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

    g = Graph(5)
    g.add_edge(0, 1, 3)
    g.add_edge(0, 2, 1)
    g.add_edge(1, 2, 7)
    g.add_edge(1, 3, 5)
    g.add_edge(1, 4, 1)
    g.add_edge(2, 3, 2)
    g.add_edge(3, 4, 7)

    distance = shortest_path(g, 2)
    print(distance)
    t.run(distance[2] == 0)
    t.run(distance[0] == 1)
    t.run(distance[1] == 4)
    t.run(distance[3] == 2)
    t.run(distance[4] == 5)