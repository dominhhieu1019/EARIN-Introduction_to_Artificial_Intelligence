from heapq import heappop, heappush
from graph import (edges_to_graph, graph_to_edges)

def find_path(graph, no_cities, w1, w2):
    """Algorithm implementation to find the highway

    Args:
        graph (dict): A non-empty graph.
        no_cities (int): number of cities in the network
        w1 (float): parameter w1
        w2 (float): parameter w2

    Returns:
        list: Returns a list of tuples representing the edges of the path
    """
    if not graph or not isinstance(graph, dict):
        raise ValueError("graph must be a dict.")

    min_path = []
    start = next(iter(graph))
    explored = []
    unexplored = [(0, start, None)]
    unused = []
    while unexplored:
        w, u, v = heappop(unexplored)
        if u in explored:
            continue
        if not v is None:
            min_path.append((v, u, w))
        explored.append(u)

        for n in graph[u]:
            if n not in explored:
                heappush(unexplored, (graph[u][n], n, u))
            else:
                heappush(unused, (graph[u][n], n, u))

    minf, distance_between_cities = objective_function(min_path, no_cities, w1, w2)
    while unused:
        path = min_path.copy()
        w, u, v = heappop(unused)
        if (v, u, w) in min_path or (u, v, w) in min_path or w == distance_between_cities[u][v]:
            continue
        path.append((v, u, graph[v][u]))
        f, dis = objective_function(path, no_cities, w1, w2)
        if f > minf:
            continue
        min_path = path
        minf = f
        distance_between_cities = dis

    return min_path


def cities_distance(path, no_cities):
    """Algorithm implementation to find the highway

    Args:
        path (list): A list of edges
        no_cities (int): number of cities in the network

    Returns:
        dict: Returns a weighted graph (weights are length of path between two cities)
            represented as {src: {dst: weight}, ...}
    """
    distance_between_cities = edges_to_graph(path)
    for src in range(no_cities):
        for dst in range(no_cities):
            if dst == src:
                continue
            if dst not in distance_between_cities[src]:
                distance_between_cities[src][dst] = distance_between_cities[dst][src] = float('inf')

    for k in range(no_cities):
        for src in range(no_cities):
            if k == src:
                continue
            for dst in range(no_cities):
                if dst == src or dst == k or distance_between_cities[src][k] == float('inf') or distance_between_cities[k][dst] == float('inf'):
                    continue
                distance_between_cities[src][dst] = distance_between_cities[dst][src] = min(
                    distance_between_cities[src][dst], distance_between_cities[src][k] + distance_between_cities[k][dst])

    return distance_between_cities


def objective_function(path, no_cities, w1, w2):
    """Algorithm implementation to find the highway.

    Args:
        path (list): A list of edges
        no_cities (int): number of cities in the network
        w1 (float): parameter w1
        w2 (float): parameter w2

    Returns:
        tuple: Returns result of objective function f and 
            a weighted graph (weights are length of path between two cities)
            represented as {src: {dst: weight}, ...}
    """
    distance_between_cities = cities_distance(path, no_cities)
    t = d = 0
    for _, _, w in path:
        t = t + w
    for i in distance_between_cities:
        d = d + sum(distance_between_cities[i].values())

    return w1 * t / 2 + w2 * d / (no_cities * (no_cities - 1)), distance_between_cities
