'''
Approach 1:
    Build adjacency list graph from tickets
    Build flight itinerary using DFS

    DFS(src, visited, itinerary, g, tickers):
        Base 1:
            Itinerary size = num of tickets + 1:
                => Get itinerary
        
        Mark src as visited
        Iterate all neighbors v of src:
            V is unvisited:
                DFS with (src = v, itinerary = itinerary + src)
                Remove v from visited

        No valid itinerary => Get nothing
        

Runtime: O()
Space Complexity: O()
'''
def flight_itinerary(tickets, src):
    g = adj_list(tickets)
    visited = set()
    itinerary = [src]
    return build_itinerary(g, src, visited, itinerary, tickets)


from collections import defaultdict
def adj_list(tickets):
    g = defaultdict(set)
    for u,v in tickets:
        g[u].add(v)
    
    return g


def build_itinerary(g, src, visited, itinerary, tickets):
    if len(itinerary) == len(tickets) + 1:
        return itinerary
    
    visited.add(src)
    for v in g[src]:
        if v not in visited:
            current_itinerary = build_itinerary(g, v,visited, \
                            itinerary + [v], tickets)
            if current_itinerary:
                return current_itinerary
            visited.remove(v)

    return None

    

# Test
class Test:
    count = 0
    def run(self, result):
        self.count += 1
        if result:
            print(f"Passed test {self.count}")
        else:
            print(f"Failed test {self.count}")

        
if __name__ == '__main__':
    test = Test()

    tickets = [
        ["HNL", "AKL"],
        ["YUL", "ORD"],
        ["ORD", "SFO"],
        ["SFO", "HNL"]
    ]
    src = "YUL"
    result = ["YUL", "ORD", "SFO", "HNL", "AKL"]
    my_result = flight_itinerary(tickets, src)
    test.run(result == my_result)



    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    src = "JFK"
    result = ["JFK", "MUC", "LHR", "SFO", "SJC"]
    my_result = flight_itinerary(tickets, src)
    test.run(result == my_result)

    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    src = "JFK"
    result = ["JFK","ATL","JFK","SFO","ATL","SFO"]
    my_result = flight_itinerary(tickets, src)
    print(my_result)
    test.run(result == my_result)