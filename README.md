Conway's Game of Life

This is a project by K.V. Sishir, a beginner Python developer, featuring a clean, modular implementation of the well-known cellular automaton Conway's Game of Life.

Rules

In a 2D grid, there are four ways to update the state of every cell simultaneously in each generation:
1. Underpopulation: If a cell is alive and has fewer than 2 live neighbours, it dies.
2. Overpopulation: If a cell is alive and has more than 3 live neighbours, it dies.
3. Reproduction: If a cell is dead and has exactly 3 live neighbours, it becomes alive.
4. Survival: If a cell is alive and has 2 or 3 live neighbours, it stays alive.
These simplistic yet powerfully constrained rules give rise to a huge variety of patterns and simulations. Changing just a single cell's position or state can completely alter the entire simulation.

Technologies Used

• Backend: Python (State is managed in memory using 2D Python lists, NumPy arrays, and Python sets)
• Frontend (Current): Command Prompt / Terminal Interface using ANSI escape codes and msvcrt for real-time keyboard controls
• Frontend (Planned): Pygame GUI and/or a JavaScript web frontend

Project Structure

text
Conway_game_of_life/
├── engines/
│   ├── pure_python.py    # 2D list engine with modulo (%) edge wrapping
│   ├── numpy_torus.py    # Vectorized NumPy engine using np.roll()
│   └── infinite_set.py   # Sparse set engine supporting an unbounded grid
├── renderer.py           # Terminal viewport renderer with camera controls
├── patterns.py           # Dictionary of classic starting patterns (Glider, Blinker, Pulsar, etc.)
└── main.py               # Interactive startup menu and simulation runner
Use code with caution.

Engines

I decided to build three separate simulation engines that all plug into the same renderer:
1. Pure Python (PurePythonEngine): Uses nested lists and wraps around grid boundaries using the % (modulo) operator.
2. NumPy Torus (NumpyEngine): Uses 2D NumPy arrays and shifts the entire grid in 8 directions simultaneously with np.roll() for fast vectorized neighbor counting.
3. Infinite Set (InfiniteSetEngine): Stores only (row, col) coordinates of live cells inside a Python set, allowing patterns to travel infinitely without hitting walls.

Version History & Changelog


Version 1.0.0 — Core Engines

• Wrote standalone prototypes for the Pure Python grid, the NumPy toroidal grid, and the Infinite Set grid.
• Implemented terminal rendering and tested random boards alongside classic patterns.

Version 1.0.1 — Modular Architecture & Interactive Viewport

• Refactored all three engines into wrapper classes (PurePythonEngine, NumpyEngine, InfiniteSetEngine) sharing a unified interface: .step() to advance one generation and .get_live_cells() to return a set of live (row, col) coordinates.
• Upgraded renderer.py from a basic grid printer into a full Renderer class with a movable camera viewport powered by msvcrt (WASD / Arrow keys to pan, R to reset view, C to center on live cells, and Q to quit).
• Built an interactive menu in main.py allowing the user to select any engine and choose between a random board or preset patterns from patterns.py.

Planned Roadmap

• Terminal playback controls (Space to pause/resume, N to step one generation, +/- to adjust speed)
• .rle (Run Length Encoded) pattern file parser for importing famous large patterns like the Gosper Glider Gun
• Graphical interface using Pygame or a JavaScript frontend
• Bonus 4th Engine: A Bitboard implementation using Python integers and bitwise operations (<<, >>, &, |, ^)

Development Credits & AI Collaboration

• Core Programming & Architecture (K.V. Sishir): Wrote the Pure Python engine, the NumPy neighbor-shifting implementation, the Infinite Set coordinate logic, the msvcrt camera movement system, the patterns.py library, and the interactive main.py menu.
• Guidance & Code Review (AI Assistant): Assisted with explaining np.roll() vectorization and ANSI terminal clearing (\033[H\033[J), suggesting the Separation of Concerns folder structure, debugging edge cases (operator precedence, optional initial_cells=None initialization, Windows two-byte arrow key handling, and centroid math), and formatting this README.

## Acknowledgments, Citations & License

### Historical Citation
* **Concept & Rules:** Invented by British mathematician **John Horton Conway** in 1970.
* **Popularization:** First introduced to the wider public by **Martin Gardner** in his October 1970 *"Mathematical Games"* column in *Scientific American*.

### Pattern Credits & Fair Use
* Classic cellular automaton patterns (such as the *Glider*, *Blinker*, *Toad*, *Pulsar*, and *Gosper Glider Gun*) are standard mathematical configurations documented by the global cellular automata community on [LifeWiki](https://conwaylife.com "LifeWiki").
* Pure mathematical patterns and basic RLE coordinates are treated as public-domain mathematical constructs and are included strictly for educational and non-commercial exploration.

### License
* The source code for this project is licensed under the **MIT License** — you are free to use, modify, and distribute it with proper attribution.
