import numpy as np
example = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

def parse_input(text: str) -> np.ndarray:
    text = text.strip().split("\n")
    text = [list(line) for line in text]
    return np.array(text)

def find_antinodes(grid: np.ndarray, harmonics: bool = False) -> np.ndarray:
    nrows, ncols = grid.shape
    filled_grid = grid.copy()
    for antenna in np.unique(grid):
        if antenna == ("."):
            continue
        locs = np.argwhere(grid == antenna)
        locs = [(locs[idx], locs) for idx in range(len(locs))]
        for pair in locs:
            loc1 = pair[0]
            for loc2 in pair[1]:
                res = loc1 - loc2
                if (res == np.array([0, 0])).all():
                    continue
                repeats = 100 if harmonics else 1
                if harmonics:
                    filled_grid[loc1[0], loc1[1]] = "#"
                for i in range(repeats):
                    loc_antinode = loc1 + (i + 1) * res
                    if loc_antinode[0] >= 0 and loc_antinode[1] >= 0 and loc_antinode[0] < nrows and loc_antinode[1] < ncols:
                        filled_grid[loc_antinode[0], loc_antinode[1]] = "#"
                    else:
                        break
    return filled_grid

if __name__ == "__main__":
    # Read input
    with open("day-08/input.txt", "r") as f:
        inp = f.read()
    inp = parse_input(inp)

    # Part 1
    filled_grid = find_antinodes(inp)
    num_antinodes = len(np.argwhere(filled_grid == "#"))
    print(f"Part 1: {num_antinodes}") # 327

    # Part 2
    filled_grid = find_antinodes(inp, True)
    num_antinodes = len(np.argwhere(filled_grid == "#"))
    print(f"Part 2: {num_antinodes}") # 1233