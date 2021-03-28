def dijkstra(graph, costs, parents):
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node 
        processed.append(node)
        node = find_lowest_cost_node(costs)
    return costs, parents

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost 
            lowest_cost_node = node 
    return lowest_cost_node

if __name__ == "__main__":
    # graph
    graph = {}
    graph["start"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2
    graph["a"] = {}
    graph["a"]["finish"] = 1
    graph["b"] = {}
    graph["b"]["a"] = 3
    graph["b"]["finish"] = 5
    graph["finish"] = {}

    # costs
    costs = {}
    costs["a"] = 6
    costs["b"] = 2
    costs["finish"] = float("inf")

    # parents
    parents = {}
    parents["a"] = "start"
    parents["finish"] = None

    processed = []

    print("Costs before running dijkstra's algorithm")
    print(costs)
    lowest_costs, path = dijkstra(graph, costs, parents)
    print("Costs after running dijkstra's algorithm")
    print(lowest_costs)
    print("Shortest path:")
    print(" -> ".join(["start", path["a"], path["finish"], "finish"]))




