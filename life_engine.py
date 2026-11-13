# Modules required
import time
import os
import subprocess
import numpy as np

# Function to create default_grid (Task 3)
def create_grid(rows:int,cols:int):
    return np.zeros((rows,cols),dtype=int) # Creates plain grid of 0s

# Function to create initial grid randomly
def create_grid_random(rows:int,cols:int):
    grid = np.random.choice([0,1] ,size=(rows,cols),p=[0.8,0.2])
    return grid

# Function to check neighbours and return new_generation
def new_generation(grid):
    neighbours = ( # By just adding the entire array shifted in all 
                   # eight direcions we can automatically count all the sums simultaneously 
        np.roll(grid,-1,axis=0)+ # bottom
        np.roll(grid,1,axis=0)+ # top
        np.roll(grid,-1,axis=1)+ # left
        np.roll(grid,1,axis=1)+ # right
        np.roll(np.roll(grid,1,axis=0),1,axis=1)+ # top right
        np.roll(np.roll(grid,-1,axis=0),1,axis=1)+ # bottom left
        np.roll(np.roll(grid,1,axis=0),-1,axis=1)+ # top left
        np.roll(np.roll(grid,-1,axis=0),-1,axis=1) # bottom right
    )
    return ((neighbours==3) | ((grid==1) & (neighbours == 2))).astype(int)

# Function to print/render the grid
def render_grid(grid):
    if os.name == "nt":
        subprocess.run(['cls'],shell=True)
    else:
        subprocess.run(['clear'],shell=True)
    for row in grid:
        print(" ".join("■" if cell == 1 else " " for cell in row))
    print()

def main():
    grid = create_grid(10,10)
    generation = 0
    try:
        while True:
            render_grid(grid)
            print(f"Generation: {generation} | Live cells: {np.sum(grid)}")
            grid = new_generation(grid)
            generation += 1
            time.sleep(0.3)
    except KeyboardInterrupt:
        print("\nSimulation stopped")
if __name__=="__main__":
    main()