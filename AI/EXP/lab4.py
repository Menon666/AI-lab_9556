from collections import deque

MAX_DEPTH = 100

# Struct to represent a state
class State:
    def __init__(self, missionaries_left, cannibals_left, boat):
        self.missionaries_left = missionaries_left
        self.cannibals_left = cannibals_left
        self.boat = boat

# Struct for a node in the BFS search tree
class Node:
    def __init__(self, state, parent_index):
        self.state = state
        self.parent_index = parent_index

# Function to check if a state is valid
def is_valid(state):
    return (
        0 <= state.missionaries_left <= 3
        and 0 <= state.cannibals_left <= 3
        and (
            state.missionaries_left >= state.cannibals_left
            or state.missionaries_left == 0
            or state.missionaries_left == 3
        )
        and (3 - state.missionaries_left >= 3 - state.cannibals_left or state.missionaries_left == 0)
    )

# Function to check if the state is the goal state
def is_goal(state):
    return state.missionaries_left == 0 and state.cannibals_left == 0 and state.boat == 1

# Function to print the path
def print_path(nodes, index):
    if index == -1:
        return
    print_path(nodes, nodes[index].parent_index)
    node = nodes[index]
    print(
        f"Move: {node.state.missionaries_left} missionaries and {node.state.cannibals_left} cannibals "
        f"from the {'left' if node.state.boat == 0 else 'right'} side to the "
        f"{'right' if node.state.boat == 0 else 'left'} side."
    )

# Function for breadth-first search
def bfs(initial_state):
    queue = deque()
    initial_node = Node(initial_state, -1)
    queue.append(initial_node)

    while queue:
        current_node = queue.popleft()
        if is_goal(current_node.state):
            print("Solution Found:")
            print_path(queue, len(queue) - 1)
            return

        # Generate child nodes
        for m in range(3 + 1):
            for c in range(3 + 1):
                if m + c > 2 or m + c == 0:
                    continue

                if current_node.state.boat == 0:
                    next_state = State(
                        current_node.state.missionaries_left - m,
                        current_node.state.cannibals_left - c,
                        1
                    )
                else:
                    next_state = State(
                        current_node.state.missionaries_left + m,
                        current_node.state.cannibals_left + c,
                        0
                    )

                if is_valid(next_state):
                    next_node = Node(next_state, len(queue))
                    queue.append(next_node)

    print("No solution found.")

def main():
    initial_state = State(3, 3, 0)  # initial state
    bfs(initial_state)

if __name__ == "__main__":
    main()
