import heapq


def dijkstra(graph, start, end):
    """Constructs the shortest path from the start node to the end node using Dijkstra's algorithm.

    Args:
        graph (Dict[str, Tuple[str, float]]): A dictionary representing the graph, where the keys are the nodes and the values are a list of
                                              tuples representing the neighbors of each node and their costs.
        start (str): The start node of the path.
        end (str): The end node of the path.

    Returns:
        List[str]: A list of airports in the shortest path from the start airport to the end airport.
        float: The cost of the shortest path.
    """

    if start not in graph:
        return None, None

    if start == end:
        return [start], 0

    # Create a priority queue
    queue = []

    # Add the start node to the queue with a cost of 0
    queue.append((start, 0))

    # A dictionary to store the predecessor and cost from start of each node
    predecessors = {start: (start, 0)}

    while queue:
        # Get the node with the lowest cost from the queue
        current_node, current_cost = heapq.heappop(queue)

        # If the current node is the end node, return the shortest path
        if current_node == end:
            nodes_in_shortest_path = getPreviousNodes(
                predecessors, start, end)
            return nodes_in_shortest_path, predecessors[current_node][1]

        if current_node not in graph:
            continue

        # For each neighbor of the current node in the graph
        for neighbor, cost in graph[current_node]:
            if neighbor not in predecessors:
                heapq.heappush(queue, (neighbor, current_cost + cost))
                predecessors[neighbor] = (current_node, current_cost + cost)

            # If the neighbor is already in the shortest path, update its cost
            elif current_cost + cost < predecessors[neighbor][1]:
                predecessors[neighbor] = (current_node, current_cost + cost)

    return None, None


def getPreviousNodes(shortest_path, start, end):
    """Constructs the nodes in the shortest path from the start node to the end node.

    Args:
        shortest_path (Dict[str, Tuple[str, float]]): A dictionary representing the shortest path.
        start (str): The start node of the path.
        end (str): The end node of the path.

    Returns:
        List[str]: A list of nodes in the shortest path from the start node to the end node.
    """

    path = []
    current_node = end

    while current_node != start:
        path.append(current_node)
        current_node = shortest_path[current_node][0]

    path.append(start)
    path.reverse()

    return path
