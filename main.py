# MODULES
import time
from renderer import Renderer
from patterns import PATTERNS
from engines.pure_python import PurePythonEngine
from engines.numpy_torus import NumpyEngine
from engines.infinite_set import InfiniteSetEngine

# CONSTANTS
ROWS = 20
COLS = 40
ENGINES = {
    "1":("Pure Python (2D list)", PurePythonEngine),
    "2":("NumPy (Torus Wrapping)", NumpyEngine),
    "3":("Infinite Set (Sparse Grid)", InfiniteSetEngine),
}

def choose_engine():
    """Prompt the user to select an engine"""
    print("Choose an engine")
    for key, (label, _) in ENGINES.items():
        print(f"{key}. {label}")
    choice = input("Enter choice:").strip()
    if choice not in ENGINES:
        print("Invalid Engine Choice")
        return None
    return ENGINES[choice][1]

def choose_pattern()->tuple[bool, set[tuple[int, int]]]:
    """Prompt for a starting pattern. Returns (is_valid, pattern_cells)."""
    print("\nChoose starting state:")
    print("0. Random board")
    
    pattern_names = list(PATTERNS.keys())
    for idx, name in enumerate(pattern_names, start=1):
        print(f"{idx}. {name.capitalize()}")

    p_choice = input("Enter choice: ").strip()
    if p_choice == "0":
        return True,None
    elif p_choice.isdigit() and 1 <= int(p_choice) <= len(pattern_names):
        return True,PATTERNS[pattern_names[int(p_choice) - 1]]
    else:
        print("Invalid pattern choice")
        return False,None
    
def run_simulation(engine, renderer:Renderer):
    """Run the main render-step loop until user stops/interrupts"""
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
        print("\n Simulation stopped")

def main():
    # Pick the engine
    engine_cls = choose_engine()
    if not engine_cls:
        print("Invalid Engine")
        return
    # Pick the starting Pattern
    is_valid, pattern = choose_pattern()
    if not is_valid:
        print("Invalid Pattern")
        return
    # Initialize the Engine
    engine = engine_cls(ROWS,COLS,pattern)
    # Run the Simulation
    renderer = Renderer(ROWS,COLS,ROWS//2,COLS//2,bounded=engine.bounded)
    run_simulation(engine,renderer)
    
if __name__== "__main__":
    main()


    

