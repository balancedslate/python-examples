from heapq import heappush, heappop

def dijkstra(graph, start, end):
    # Initialize distances and previous nodes
    distances = {node: float("inf") for node in graph}
    previous = {node: None for node in graph}
    distances[start] = 0

    # Create a priority queue of nodes
    queue = []
    heappush(queue, (0, start))

    # Loop until the queue is empty
    while queue:
        # Pop the node with the smallest distance
        distance, node = heappop(queue)

        # Ignore the node if it has already been processed
        if distance > distances[node]:
            continue

        # Update the distances and previous nodes of the neighbors
        for neighbor in graph[node]:
            new_distance = distances[node] + graph[node][neighbor]
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = node
                heappush(queue, (new_distance, neighbor))

    # Build the shortest path from the end to the start
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = previous[node]
    return path[::-1]

# Define the graph
graph = {
    "A": {"B": 1, "C": 4},
    "B": {"C": 2, "D": 5},
    "C": {"D": 1},
    "D": {},
}

# Find the shortest path from A to D
path = dijkstra(graph, "A", "D")

# Print the shortest path
print(f"Shortest path: {' -> '.join(path)}")
