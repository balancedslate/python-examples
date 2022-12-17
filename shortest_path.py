from itertools import permutations

def find_shortest_path(cities, distances):
    # Generate all possible permutations of the cities
    permutations_ = permutations(cities)

    # Find the permutation with the shortest total distance
    min_distance = float("inf")
    min_path = None
    for permutation in permutations_:
        total_distance = 0
        for i in range(len(permutation) - 1):
            city1 = permutation[i]
            city2 = permutation[i + 1]
            distance = distances[(city1, city2)]
            total_distance += distance
        if total_distance < min_distance:
            min_distance = total_distance
            min_path = permutation

    return min_path

# Define the cities and their locations
cities = {
    "A": (0, 0),
    "B": (1, 0),
    "C": (1, 1),
    "D": (0, 1),
}

# Calculate the distance between each pair of cities
distances = {}
for city1, (x1, y1) in cities.items():
    for city2, (x2, y2) in cities.items():
        if city1 != city2:
            distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            distances[(city1, city2)] = distance

# Find the shortest path that visits all cities
shortest_path = find_shortest_path(cities.keys(), distances)

# Print the shortest path
print(f"Shortest path: {' -> '.join(shortest_path)}")
