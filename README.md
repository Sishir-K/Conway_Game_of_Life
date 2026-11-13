# Conway's Game of Life

This is a project by **K.V. Sishir**, a 3rd Semester CSE undergraduate student, featuring a clean, modular Python implementation of **John Conway's Game of Life**.

---

## Rules

In a 2D grid, there are four ways to update the state of every cell simultaneously in each generation:

1. **Underpopulation:** If a cell is alive and has fewer than 2 live neighbours, it dies.
2. **Overpopulation:** If a cell is alive and has more than 3 live neighbours, it dies.
3. **Reproduction:** If a cell is dead and has exactly 3 live neighbours, it becomes alive.
4. **Survival:** If a cell is alive and has 2 or 3 live neighbours, it stays alive.

These simplistic yet powerfully constrained rules give rise to a huge variety of complex patterns and simulations. Changing just a single cell's position or state can completely alter the outcome.

---

## Technologies Used

* **Backend:** Python (State is managed in memory using 2D Python lists, vectorized NumPy arrays, and Python sets)
* **Frontend (Current):** Command Prompt / Terminal Interface using ANSI escape codes (`\033[H\033[2J\033[3J`) and `msvcrt` for real-time keyboard controls
* **Frontend (Planned):** Pygame GUI and/or a JavaScript web frontend

---

## Project Structure

```text
Conway_game_of_life/
├── engines/
│   ├── pure_python.py    # 2D list engine with modulo (%) edge wrapping
│   ├── numpy_torus.py    # Vectorized NumPy engine using np.roll()
│   └── infinite_set.py   # Sparse set engine supporting an unbounded grid
├── renderer.py           # Terminal viewport renderer with camera controls & clamping
├── patterns.py           # Dictionary of classic starting patterns (Glider, Blinker, Toad, Pulsar)
└── main.py               # Modular startup menu and simulation runner
```

---

## Engines

I built three separate simulation engines that share a unified interface (`.step()`, `.get_live_cells()`, and `.bounded`) so they all plug into the exact same renderer:

1. **Pure Python (`PurePythonEngine`):** Uses nested 2D lists and wraps around grid boundaries using the `%` (modulo) operator.
2. **NumPy Torus (`NumpyEngine`):** Uses 2D NumPy arrays and shifts the entire grid in 8 directions simultaneously with `np.roll()` for fast vectorized neighbor counting.
3. **Infinite Set (`InfiniteSetEngine`):** Stores only `(row, col)` coordinates of live cells inside a Python `set`, allowing patterns to expand infinitely without hitting walls.

---

## Version History & Changelog

### Version 1.0.0 — Core Engines
* Built standalone prototypes for the Pure Python grid, the NumPy toroidal grid, and the Infinite Set grid.
* Tested random boards alongside classic patterns in the terminal.

### Version 1.0.1 — Modular Architecture & Interactive Viewport
* Refactored all three engines into wrapper classes (`PurePythonEngine`, `NumpyEngine`, `InfiniteSetEngine`) sharing a unified interface.
* Built a `Renderer` class in `renderer.py` with a movable camera viewport powered by `msvcrt` (`WASD` / Arrow keys to pan, `R` to reset view, `C` to center on the centroid of live cells, and `Q` to quit).
* Added an interactive startup menu in `main.py` to choose between engines and starting patterns.

### Version 1.1.0 — Viewport Clamping, Readability Refactor & Live Stats
* Added `bounded` viewport clamping so fixed-size grids (`PurePythonEngine` and `NumpyEngine`) prevent the camera from panning out of bounds, while `InfiniteSetEngine` retains unrestricted exploration.
* Updated the status bar to display both **Visible Alive** (cells inside the current viewport) and **Total Alive** (cells across the entire simulation).
* Refactored `renderer.py` to use movement lookup dictionaries (`MOVE_DELTAS`) and flicker-free frame buffering (`\033[3J\033[H`).
* Refactored `main.py` into single-purpose helper functions (`choose_engine`, `choose_pattern`, `run_simulation`) and dictionary-based engine dispatch.

---

## Planned Roadmap
* [ ] `.rle` (Run-Length Encoded) pattern file parser for importing large famous patterns (such as the Gosper Glider Gun)
* [ ] Terminal playback controls (`Space` to pause/resume, `N` to step one generation, `+`/`-` to adjust simulation speed)
* [ ] Graphical interface using Pygame or a JavaScript web frontend
* [ ] Bonus 4th Engine: A **Bitboard** implementation using Python integers and bitwise logic gates (`<<`, `>>`, `&`, `|`, `^`)

---

## Acknowledgments, Citations & License

### Historical Citation
* **Concept & Rules:** Invented by British mathematician **John Horton Conway** in 1970.
* **Popularization:** First introduced to the wider public by **Martin Gardner** in his October 1970 *"Mathematical Games"* column in *Scientific American*.

### Pattern Credits & Fair Use
* Classic cellular automaton patterns (such as the *Glider*, *Blinker*, *Toad*, and *Pulsar*) are standard mathematical configurations documented by the global cellular automata community on [LifeWiki](https://conwaylife.com "LifeWiki").
* Pure mathematical patterns and basic RLE coordinates are treated as public-domain mathematical constructs and are included strictly for educational and non-commercial exploration.

### License
* The source code for this project is licensed under the **MIT License** — you are free to use, modify, and distribute it with proper attribution.

---

## Development Credits & AI Collaboration

* **Core Programming & Architecture (K.V. Sishir):** Designed and coded the Pure Python engine, the NumPy neighbor-shifting implementation, the Infinite Set coordinate engine, the `msvcrt` camera movement system, the `patterns.py` library, and the modular `main.py` menu.
* **Guidance & Code Review (AI Assistant):** Assisted with explaining `np.roll()` vectorization and ANSI terminal clearing, suggesting the Separation of Concerns architecture, debugging edge cases (tuple unpacking, bounded viewport clamping, Windows two-byte arrow keys, and centroid math), and formatting documentation.
