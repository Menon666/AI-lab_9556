#9556-Krishnaa-Batch-B
def dfs_jug_problem(x, y, target_x, target_y, visited, path):
    # Base case: if the target state is reached
    if x == target_x or y == target_y:
        return path + [(x, y)]

    # Mark the current state as visited
    visited.add((x, y))

    # Perform each operation (emptying, filling, pouring) and recursively search for the target state
    operations = [
        (0, y),           # Empty jug 1
        (x, 0),           # Empty jug 2
        (x, min(x+y, target_y)),  # Pour water from jug 1 to jug 2
        (min(x+y, target_x), y),  # Pour water from jug 2 to jug 1
        (min(x+y, target_x), max(0, y - (target_x - x))),  # Pour all water from jug 2 to jug 1
        (max(0, x - (target_y - y)), min(x+y, target_y))   # Pour all water from jug 1 to jug 2
    ]

    for operation in operations:
        next_x, next_y = operation
        if (next_x, next_y) not in visited:
            result = dfs_jug_problem(next_x, next_y, target_x, target_y, visited, path + [(x, y)])
            if result:
                return result

    return None

def solve_jug_problem(jug1_capacity, jug2_capacity, target):
    initial_state = (0, 0)
    visited = set()
    path = dfs_jug_problem(0, 0, 0, target, visited, [])
    if path:
        return path
    else:
        return "No solution possible."

# Example usage:
jug1_capacity = 5
jug2_capacity = 3
target = 4
solution_path = solve_jug_problem(jug1_capacity, jug2_capacity, target)
print("Solution Path:", solution_path)
