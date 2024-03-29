import itertools

def calculate_distance(coords1, coords2):
    """
    Calculates the Euclidean distance between two points in 2D space.
    """
    x1, y1 = coords1
    x2, y2 = coords2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def tsp_brute_force(coords):
    """
    Solves the Travelling Salesman Problem using brute force approach.
    Returns the shortest path and its distance.
    """
    num_cities = len(coords)
    all_distances = [[calculate_distance(coords[i], coords[j]) for j in range(num_cities)] for i in range(num_cities)]
    shortest_path = None
    shortest_distance = float('inf')
    for path in itertools.permutations(range(num_cities)):
        distance = sum(all_distances[path[i]][path[i+1]] for i in range(num_cities - 1))
        distance += all_distances[path[-1]][path[0]]
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_path = path
    return shortest_path, shortest_distance

# Example usage:
cities_coordinates = [(0, 0), (1, 2), (3, 1), (5, 2)]
shortest_path, shortest_distance = tsp_brute_force(cities_coordinates)

print("Shortest Path:")
for city_index in shortest_path:
    x, y = cities_coordinates[city_index]
    print(f"({int(x)}, {int(y)})")
print("Shortest Distance:", int(shortest_distance))  # Converted to int for removing decimal points
