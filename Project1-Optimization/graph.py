def euclidean(p, q):
    """Find the euclidean distance between two cities

    Args:
        p (tuple): A tuple containing values x and y, ie. (x, y)
        q (tuple): A tuple containing values x and y, ie. (x, y)

    Returns:
        float: Returns the euclidean distance of p and q
    """
    if p is None or not isinstance(p, tuple):
        raise('The argument p must be a valid tuple.')

    if q is None or not isinstance(q, tuple):
        raise('The argument q must be a valid tuple.')

    return ((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2) ** 0.5


def create_graph(cities):
    """Creates a graph based on a list of cities

    Args:
        cities (list): A list of tuples representing cities as [(x, y), ...]

    Returns:
        dict: Returns a weighted graph (weights are the euclidean distance)
            represented as {src: {dst: weight}, ...}
    """
    graph = {}
    for src, xsrc, ysrc in cities:
        for dst, xdst, ydst in cities:
            if src >= dst:
                continue
            if src not in graph:
                graph[src] = {}
            if dst not in graph:
                graph[dst] = {}
            weight = euclidean((xsrc, ysrc), (xdst, ydst))
            graph[src][dst] = weight
            graph[dst][src] = weight

    return graph


def graph_to_edges(graph):
    """Converts a graph to a list of edges

    Args:
        graph (dict): A non-empty graph as {src: {dst: weight}, ...}

    Returns:
        list: Returns a list of edges of the given graph
    """
    if graph is None or not isinstance(graph, dict):
        raise ValueError("A graph must be a valid dict.")

    return [(src, dst, graph[src][dst]) for src in graph for dst in graph[src]]


def edges_to_graph(edges):
    """Converts a list of edges to a graph

    Args:
        edges (list): A list of edges

    Returns:
        dict: Returns a graph of the given edges
    """
    if edges is None or not isinstance(edges, list):
        raise ValueError("The argument edges must be a valid list.")

    graph = {}
    for src, dst, weight in edges:
        if src not in graph:
            graph[src] = {}
        if dst not in graph:
            graph[dst] = {}
        graph[src][dst] = weight
        graph[dst][src] = weight

    return graph