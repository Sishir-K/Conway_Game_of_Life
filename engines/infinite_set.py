# This version of conway's game of life uses a 
# Python set to store only alive cells => infinite alive
import random
class InfiniteSetEngine:
    bounded = False
    directions = [
        (-1,1),(0,1),(1,1),
        (-1,0),      (1,0),
        (-1,-1),(0,-1),(1,-1)
    ]

    def __init__(self,rows:int=20,cols:int=40,initial_cells:set[tuple[int]]|None=None):
        if initial_cells is None:
            self.alive = {
                (r, c)
                for r in range(rows)
                for c in range(cols)
                if random.random() < 0.3
            }
        else:
            self.alive = set(initial_cells)
    def step(self):
        counts = {}
        # count the number of living neighbours
        for row,col in self.alive:
            for d_row,d_col in self.directions:
                pos = (row+d_row,col+d_col)
                counts[pos] = counts.get(pos,0)+1
        new_alive = set()
        for pos,count in counts.items():
            if count == 3 or (count == 2 and pos in self.alive):
                new_alive.add(pos)
        self.alive = new_alive
    def get_live_cells(self):
        return self.alive
