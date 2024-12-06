from pathlib import Path

import numpy as np
from tqdm import tqdm

example = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

def parse_input(text: str) -> np.ndarray:
    return np.array([list(row) for row in text.strip().split('\n')])

with Path.open(Path("day-06/input.txt"), "r") as f:
    grid = parse_input(f.read())

# grid = parse_input(example)

class Guard:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.direction = 0

    def rotate(self):
        #  0
        # 3 1
        #  2
        self.direction = (self.direction + 1) % 4

    def move(self):
        if self.direction == 0:
            self.y -= 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y += 1
        elif self.direction == 3:
            self.x += -1

    def next_move(self):
        if self.direction == 0:
            return self.x, self.y - 1
        elif self.direction == 1:
            return self.x + 1, self.y
        elif self.direction == 2:
            return self.x, self.y + 1
        elif self.direction == 3:
            return self.x - 1, self.y


def traverse_maze(grid: np.ndarray, iter_limit: int = 10_000) -> np.ndarray:
    grid = grid.copy()
    nrows, ncols = grid.shape

    # Guard
    loc_guard = np.where(grid == "^")
    guard = Guard(loc_guard[1][0], loc_guard[0][0])
    grid[guard.y, guard.x] = "X"
    for idx in range(iter_limit):
        nx, ny = guard.next_move()
        # print(f"Direction: {guard.direction} - Current: ({guard.x}, {guard.y}) | Next: ({nx}, {ny})")
        if (nx >= 0 and ny >= 0) and (nx < ncols and ny < nrows):
            if grid[ny, nx] == "#":
                guard.rotate()
            else:
                guard.move()
                grid[guard.y, guard.x] = "X"
        else:
            # print("Out of bounds")
            break
        if idx == iter_limit - 1:
            return False
    return grid

solved_grid = traverse_maze(grid)
print(f"Part 1: {np.sum(solved_grid == 'X')}") # 5145

# Part 2
count = 0
for pos in tqdm(np.argwhere(solved_grid == "X"), ascii=True):
    if np.array_equal(pos, np.argwhere(grid == "^")[0]):
        continue

    new_grid = grid.copy()
    new_grid[pos[0], pos[1]] = "#"

    solved_grid = traverse_maze(new_grid)
    if solved_grid is False:
        count += 1

print(f"Part 2: {count}") # 1523