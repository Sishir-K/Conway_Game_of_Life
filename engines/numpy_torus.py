# This version of conway's game of life uses a 
# Numpy array but, uses topological wrapping meaning the
# bottom right can interact with bottom left and top right etc
import numpy as np

# Making a warpper class for this entire engine called as NumpyEngine
class NumpyEngine:
    def __init__(self,rows:int,cols:int,initial_cells:set[tuple[int]]):
        self.grid = np.zeros((rows,cols),dtype=int)
        for r,c in initial_cells:
            self.grid[r,c]=1
    
    # Function to check neighbours and return new_generation
    def step(self):
        neighbours = ( # By just adding the entire array shifted in all 
                    # eight direcions we can automatically count all the sums simultaneously 
            np.roll(self.grid,-1,axis=0)+ # bottom
            np.roll(self.grid,1,axis=0)+ # top
            np.roll(self.grid,-1,axis=1)+ # left
            np.roll(self.grid,1,axis=1)+ # right
            np.roll(np.roll(self.grid,1,axis=0),1,axis=1)+ # top right
            np.roll(np.roll(self.grid,-1,axis=0),1,axis=1)+ # bottom left
            np.roll(np.roll(self.grid,1,axis=0),-1,axis=1)+ # top left
            np.roll(np.roll(self.grid,-1,axis=0),-1,axis=1) # bottom right
        )
        return ((neighbours==3) | ((self.grid==1) & (neighbours == 2))).astype(int)

    # Function to get new set of live cells
    def get_live_cells(self)->set[tuple[int]]:
        rows,cols = np.where(self.grid==1)
        return set(zip(rows.tolist(),cols.tolist()))
