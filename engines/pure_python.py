#Creating a rapper class for the PurePythonEngine
import random

class PurePythonEngine:
    bounded = True
    def __init__(self,rows:int,cols:int,initial_cells:set[tuple[int]]):
        self.rows = rows
        self.cols = cols
        if initial_cells is None:
            # Generate a random board if no starting cells were given
            self.grid = [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]
        else:
            # Build an empty board and place the given starting cells
            self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
            for r, c in initial_cells:
                if 0 <= r < rows and 0 <= c < cols:
                    self.grid[r][c] = 1

    #Function to generate next_generation = step()
    def step(self):
        new_grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for r in range(self.rows):
                for c in range(self.cols):
                    
                    live_neighbours = 0
                    for d_row in [-1,0,1]:
                        for d_col in [-1,0,1]:
                            if d_row == 0 and d_col == 0:
                                continue
                            n_row,n_col = (r+d_row)%self.rows, (c+d_col)%self.cols
                            live_neighbours += self.grid[n_row][n_col]
        
                    cell = self.grid[r][c]
                    if cell == 1 and live_neighbours in (2,3):
                        new_grid[r][c] = 1
                    elif cell == 0 and live_neighbours == 3:
                        new_grid[r][c] = 1

        self.grid = new_grid

    # Function to get live cells
    def get_live_cells(self)->set[tuple[int]]:
        """Converting the 2D list in a set of tuples for the renderer"""
        live = set()
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == 1:
                    live.add((row,col))
        return live




