from heapq import heappop, heappush

example = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""

def parse_input(text: str) -> dict:
    grid = {}
    start, end = None, None
    for row, line in enumerate(text.splitlines()):
        for col, char in enumerate(line):
            grid[(row, col)] = char
            if char == "S":
                start = (row, col)
            if char == "E":
                end = (row, col)
    return grid, start, end

steps = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def dijkstra(grid, start, end):
    pq = [(0, start, (0, 0), [start])]
    visited = set()

    while pq:
        cost, node, direction, path = heappop(pq)
        if node == end:
            return cost, path
        if node in visited:
            continue
        visited.add(node)

        for step in steps:
            new_node = (node[0] + step[0], node[1] + step[1])
            new_path = path + [new_node]
            is_corner = step != direction
            new_cost = cost + 1 + (1000 if is_corner else 0)
            if new_node in grid and grid[new_node] != "#":
                heappush(pq, (new_cost, new_node, step, new_path))
    return -1, []    

if __name__ == "__main__":
    # Read data
    data = open("day-16/input.txt").read().strip()
    grid, start, end = parse_input(data)

    # Part 1
    res, path = dijkstra(grid, start, end)
    print("Part 1:", res)