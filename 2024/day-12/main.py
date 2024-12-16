example = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

example = """AAAA
BBCD
BBCC
EEEC"""

steps = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def read_grid(text: str) -> dict[tuple[int]: str]:
    res = {}
    for i, line in enumerate(text.split("\n")):
        for j, char in enumerate(line):
            res[(i, j)] = char
    return res

def search(grid, pos, region=None):
    if region is None:
        region = []
    region.append(pos)
    for step in steps:
        new_pos = (pos[0] + step[0], pos[1] + step[1])
        if new_pos in grid and grid[new_pos] == grid[pos] and new_pos not in region:
            search(grid, new_pos, region)
        else:
            continue
    return region

def find_regions(grid) -> dict:
    positions = list(grid.keys())
    regions = []
    for pos in positions:
        region = search(grid.copy(), pos)
        for loc in region[1:]:
            positions.remove(loc)
        regions.append(region)
    return [(grid[region[0]], region) for region in regions]

def calc_value_perimeter(region: list[tuple[int]]) -> int:
    area = len(region)
    sides = 0
    for point in region:
        for step in steps:
            if (point[0] + step[0], point[1] + step[1]) not in region:
                sides += 1
    
    return area * sides

def calc_value_sides(region: list[tuple[int]]) -> int:
    area = len(region)
    corners = []
    offsets = [(0, 0), (0, 1), (1, 0), (1, 1)]
    for point in region:
        for off in offsets:
            corners.append((point[0] + off[0], point[1] + off[1]))
    expanded_grid = list(set(corners))

    corners = []    
    for point in expanded_grid:
        up    = (point[0] - 1, point[1]) in expanded_grid
        down  = (point[0] + 1, point[1]) in expanded_grid
        left  = (point[0], point[1] - 1) in expanded_grid
        right = (point[0], point[1] + 1) in expanded_grid
        if (up and left) ^ (up and right) ^ (down and left) ^ (down and right):
            corners.append(point)

        # Missing condition for concave corners
    
    return (area, len(corners))


if __name__ == "__main__":
    # Read input
    grid = read_grid(open("day-12/input.txt").read().strip())
    # grid = read_grid(example)

    # Part 1
    regions = find_regions(grid)
    total_value = 0
    for (_, v) in regions:
        total_value += calc_value_perimeter(v)
    print(f"Part 1: {total_value}") # 1402544

    # Part 2
    # for (k, v) in regions:
    #     print(f"{k}: {calc_value_sides(v)}")