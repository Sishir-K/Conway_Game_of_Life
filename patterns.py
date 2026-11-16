# patterns.py
import re
from pathlib import Path

PATTERNS = {
    "glider": {(1, 2), (2, 3), (3, 1), (3, 2), (3, 3)},
    "blinker": {(5, 4), (5, 5), (5, 6)},
    "toad": {(5, 5), (5, 6), (5, 7), (6, 4), (6, 5), (6, 6)},
    "pulsar": {
        (2, 4), (2, 5), (2, 6), (2, 10), (2, 11), (2, 12),
        (4, 2), (4, 7), (4, 9), (4, 14),
        (5, 2), (5, 7), (5, 9), (5, 14),
        (6, 2), (6, 7), (6, 9), (6, 14),
        (7, 4), (7, 5), (7, 6), (7, 10), (7, 11), (7, 12),
        (9, 4), (9, 5), (9, 6), (9, 10), (9, 11), (9, 12),
        (10, 2), (10, 7), (10, 9), (10, 14),
        (11, 2), (11, 7), (11, 9), (11, 14),
        (12, 2), (12, 7), (12, 9), (12, 14),
        (14, 4), (14, 5), (14, 6), (14, 10), (14, 11), (14, 12),
    }
}

def load_rle(file_path:str | Path, offset_row:int = 2,offset_col:int=2)->set[tuple[int,int]]:
    """Parse an RLE file and return a set of (row,col) live cell coordinates"""
    try:
        with open(file_path,"r",encoding = "utf-8") as file:
            lines = [
                clean for line in file
                if (clean:= line.strip()) and not clean.lower().startswith(("#","x"))
            ]
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return set()

    body = "".join(lines).split("!")
    live_cells = set()
    row,col = offset_row,offset_col

    for count_str,tag in re.findall(r"(\d*)([bo\$])",body):
        count = int(count_str) if count_str else 1
        if tag == "b":
            col += count
        elif tag == "o":
            for _ in range(count):
                live_cells.add(row,col)
                col -= 1
        elif tag == "$":
            row += count
            col = offset_col
    return live_cells


