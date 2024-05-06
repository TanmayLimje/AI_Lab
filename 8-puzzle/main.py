
from queue import PriorityQueue

class PuzzleNode:
    def __init__(self, state, parent=None, move=""):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = 0  # Total cost
        self.heuristic = 0  # Heuristic cost

    def __lt__(self, other):
        return self.cost + self.heuristic < other.cost + other.heuristic

class EightPuzzleSolver:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def h1(self, state):
        # Heuristic 1: Number of misplaced tiles
        count = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != self.goal_state[i][j]:
                    count += 1
        return count

    def h2(self, state):
        # Heuristic 2: Manhattan distance
        distance = 0
        for i in range(3):
            for j in range(3):
                value = state[i][j]
                if value != 0:
                    goal_pos = divmod(value - 1, 3)
                    distance += abs(goal_pos[0] - i) + abs(goal_pos[1] - j)
        return distance

    def get_neighbors(self, node):
        neighbors = []
        zero_i, zero_j = None, None
        
        for i in range(3):
            for j in range(3):
                if node.state[i][j] == 0:
                    zero_i, zero_j = i, j
                    break
        
        moves = [(-1, 0, "Up"), (1, 0, "Down"), (0, -1, "Left"), (0, 1, "Right")]
        for di, dj, move in moves:
            new_i, new_j = zero_i + di, zero_j + dj
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_state = [row[:] for row in node.state]
                new_state[zero_i][zero_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[zero_i][zero_j]
                neighbors.append(PuzzleNode(new_state, node, move))
        return neighbors

    def solve(self, heuristic="h1"):
        start_node = PuzzleNode(self.initial_state)
        start_node.heuristic = getattr(self, heuristic)(start_node.state)
        
        frontier = PriorityQueue()
        frontier.put(start_node)
        
        explored = set()
        
        while not frontier.empty():
            current_node = frontier.get()
            
            if current_node.state == self.goal_state:
                path = []
                while current_node.parent:
                    path.append(current_node.move)
                    current_node = current_node.parent
                path.reverse()
                return path
            
            explored.add(tuple(map(tuple, current_node.state)))
            
            for neighbor in self.get_neighbors(current_node):
                if tuple(map(tuple, neighbor.state)) not in explored:
                    neighbor.cost = current_node.cost + 1
                    neighbor.heuristic = getattr(self, heuristic)(neighbor.state)
                    frontier.put(neighbor)
        
        return None

# Example usage
if __name__ == "__main__":
    initial_state = [[8, 7, 1],
                     [5, 6, 2],
                     [4, 3, 0]]

    goal_state = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 0]]

    solver = EightPuzzleSolver(initial_state, goal_state)
    solution = solver.solve(heuristic="h2")  # Use Manhattan distance heuristic
    if solution:
        print("Solution found:", solution)
    else:
        print("No solution found.")
