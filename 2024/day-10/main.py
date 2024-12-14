example = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def generate_grid(text: str) -> dict:
    return {(row, col): int(i) for row, line in enumerate(text.split('\n')) for col, i in enumerate(line)}

def search(pos, grid, height=0, end=None) -> int:
    if end is None:
        end = []
    if height == 9:
        end.append(pos)
    for step in steps:
        new_pos = (pos[0] + step[0], pos[1] + step[1])
        if new_pos in grid and grid[new_pos] == height + 1:
            search(new_pos, grid, height + 1, end)
        else:
            continue
    return len(set(end))

# Read data
data = open("day-10/input.txt").read().strip()
grid = generate_grid(data)

# Part 1
score = 0
for pos in grid:
    if grid[pos] == 0:
        score += search(pos, grid)

print(f"Part 1: {score}") # 624
            
