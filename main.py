# MODULES
import time
from renderer import Renderer
from patterns import PATTERNS
from engines.pure_python import PurePythonEngine
from engines.numpy_torus import NumpyEngine
from engines.infinite_set import InfiniteSetEngine

def main():
    print("Choose an engine:")
    print("1. Pure Python (2D List)")
    print("2. NumPy (Torus Wrapping)")
    print("3. Infinite Set (Sparse Grid)")
    choice = input("Enter 1, 2, or 3: ").strip()
    # Default Grid
    rows,cols = 20,30
    # CHeck for invalid Engine Choice
    if choice not in ("1","2","3"):
        print("Invalid Choice")
        return
    
    # To choose Starting Pattern
    print("\nChoose starting state:")
    print("0. Random board")
    pattern_names = list(PATTERNS.keys())
    for idx, name in enumerate(pattern_names, start=1):
        print(f"{idx}. {name.capitalize()}")
    p_choice = input("Enter choice: ").strip()
    if p_choice == "0":
        starting_pattern = None
    elif p_choice.isdigit() and 1 <= int(p_choice) <= len(pattern_names):
        starting_pattern = PATTERNS[pattern_names[int(p_choice) - 1]]
    else:
        print("Invalid pattern choice")
        return
    
    # Engine initialization is confirmed afterwards as starting patterns should be chosen first
    if choice == "1":
        engine = PurePythonEngine(rows,cols,starting_pattern)
    elif choice == "2":
        engine = NumpyEngine(rows,cols,starting_pattern)
    elif choice == "3":
        engine = InfiniteSetEngine(rows,cols,starting_pattern)
    # Initializing object of class Renderer
    renderer = Renderer(rows, cols, center_row=rows // 2, center_col=cols // 2)
    generation = 0
    try:
        while True:
            live_cells = engine.get_live_cells()
            if not renderer.handle_input(live_cells):
                break
            renderer.render(live_cells,generation)
            engine.step()
            generation += 1
            time.sleep(0.2)
    except KeyboardInterrupt:
        print("\nSimulation stopped")

if __name__=="__main__":
    main()


    

