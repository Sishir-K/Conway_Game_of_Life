import msvcrt
import os
# Constants
ARROW_PREFIXES = (b'\x00', b'\xe0')
KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT = b'H', b'P', b'K', b'M'
MOVE_DELTAS = {
    b'w': (-1, 0),
    b's': (1, 0),
    b'a': (0, -1),
    b'd': (0, 1),
    KEY_UP: (-1, 0),
    KEY_DOWN: (1, 0),
    KEY_LEFT: (0, -1),
    KEY_RIGHT: (0, 1),
}
# Terminal Visual Renderer
class Renderer:
    def __init__(self,rows:int=20,cols:int=30,center_row:int=10,center_col:int=15,bounded:bool=False):
        self.rows = rows
        self.cols = cols
        self.center_row = center_row
        self.center_col = center_col
        self.default_row = center_row
        self.default_col = center_col
        self.bounded = bounded

    def handle_input(self,live_cells: set[tuple[int, int]] | None = None)->bool:
        """Pans camera with the WASD and arrow keys."""
        while msvcrt.kbhit(): # WHile a key is pressed
            key = msvcrt.getch()
            if key in ARROW_PREFIXES:
                key = msvcrt.getch()
            else:
                key = key.lower()
            
            if key in MOVE_DELTAS:
                # FOR WASD directions and arrow keys
                d_row,d_col = MOVE_DELTAS[key]
                self.center_row += d_row
                self.center_col += d_col
            elif key == b'r': # Reset camera back to original center
                self.center_row = self.default_row
                self.center_col = self.default_col

            # Center/Track camera to centroid of all live_cells
            elif key == b"c" and live_cells: 
                self.center_row = round(sum(r for r, _ in live_cells) / len(live_cells))
                self.center_col = round(sum(c for _, c in live_cells) / len(live_cells))
            elif key == b"q": # Quit
                print("\nSimulation Stopped")
                return False 
        if self.bounded:
            self.center_row = max(self.rows // 2, min(self.rows - self.rows // 2, self.center_row))
            self.center_col = max(self.cols // 2, min(self.cols - self.cols // 2, self.center_col))
                        
        return True

    def render(self,live_cells:set[tuple[int,int]],generation:int = 0):
        """Render any engine's live cell inside the terminal viewport"""
        top = self.center_row - self.rows//2
        left = self.center_col - self.cols//2
        visible_alive = sum(
            1 for r,c in live_cells
            if top <= r < top + self.rows and left <= c < left + self.cols
        )
        # Move cursor to top-left (home) and clear screen
        lines = [
            " ".join("■" if (r,c) in live_cells else "." for c in range(left,left+self.cols))
            for r in range(top,top+self.rows)
        ]
        lines.append(f"\nGeneration:{generation}| Visible Alive: {visible_alive} |Total Alive:{len(live_cells)}")
        lines.append(f"Viewport centre: ({self.center_row}, {self.center_col})")
        print("\033[3J\033[H"+"\n".join(lines),flush = True)