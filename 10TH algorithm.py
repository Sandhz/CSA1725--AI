import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start node to current node
        self.h = 0  # Heuristic estimation from current node to goal node
        self.f = 0  # Total cost (g + h)

    def __lt__(self, other):
        return self.f < other.f

def astar_search(grid, start, end):
    open_set = []
    closed_set = set()

    start_node = Node(start)
    end_node = Node(end)

    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.position == end_node.position:
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        closed_set.add(current_node.position)

        for next_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Adjacent positions (assuming 4-connected grid)
            node_position = (current_node.position[0] + next_position[0], current_node.position[1] + next_position[1])

            if node_position[0] < 0 or node_position[0] >= len(grid) or \
               node_position[1] < 0 or node_position[1] >= len(grid[0]):
                continue

            if grid[node_position[0]][node_position[1]] == 1:
                continue

            if node_position in closed_set:
                continue

            new_node = Node(node_position, current_node)
            new_node.g = current_node.g + 1
            new_node.h = ((node_position[0] - end_node.position[0]) ** 2 +
                          (node_position[1] - end_node.position[1]) ** 2) ** 0.5
            new_node.f = new_node.g + new_node.h

            heapq.heappush(open_set, new_node)

    return None  # No path found

# Example usage:
grid = [[0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]]

start = (0, 0)
end = (4, 4)

path = astar_search(grid, start, end)
if path:
    print("Path found:", path)
else:
    print("No path found")
