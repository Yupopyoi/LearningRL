class Maze:
    def __init__(self):
        # 0: way, 1: wall, 2: goal
        self.grid = [
            [0, 0, 0, 1, 0, 0, 0, 1],
            [1, 1, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1],
            [1, 1, 1, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 1],
            [0, 1, 0, 1, 1, 1, 0, 1],
            [0, 1, 1, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1, 1, 0, 2]
        ]
        self.start = (0, 0)  # start position

    def is_valid_move(self, position : int):
        x, y = position
        if 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0]):
            return self.grid[x][y] != 1  
        return False

    def is_goal(self, position):
        x, y = position
        return self.grid[x][y] == 2

    def get_start_position(self):
        return self.start
    
    def mase_size(self):
        return len(self.grid)
    