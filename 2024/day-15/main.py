example = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

def read_input(text: str):
    werehouse, moves = text.split("\n\n")
    grid = {}
    for idx, line in enumerate(werehouse.splitlines()):
        for idy, i in enumerate(line):
            grid[(idx, idy)] = i
    moves = moves.splitlines()
    moves = "".join(moves)
    return grid, moves

def draw_grid(grid: dict) -> None:
    width, height = tuple(max(x) for x in zip(*grid.keys()))
    for x in range(width + 1):
        for y in range(height + 1):
            print(grid[(x, y)], end="")
        print()
    return None

def move_robot(grid, move):
    pos = next(k for k, v in grid.items() if v == "@")
    moves = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}
    move = moves[move]

    next_pos = (pos[0] + move[0], pos[1] + move[1])
    
    # .
    if grid[next_pos] == ".":
        grid[next_pos] = "@"
        grid[pos] = "."
    
    # O
    elif grid[next_pos] == "O":
        next_points = [pos, next_pos]
        offset = 2
        while True:
            behind = (pos[0] + move[0] * offset, pos[1] + move[1] * offset)
            if grid[behind] == "O":
                next_points.append(behind)
                offset += 1
            if grid[behind] == ".":
                next_points.append(behind)
                break
            if grid[behind] == "#":
                next_points.append(behind)
                break
        if grid[next_points[-1]] != "#":
            for idx, behind in enumerate(next_points):
                match idx:
                    case 0:
                        grid[behind] = "."
                    case 1:
                        grid[behind] = "@"
                    case _:
                        grid[behind] = "O"
    return grid

def augment_grid(grid) -> dict:
    width, height = tuple(max(x) for x in zip(*grid.keys()))
    new_grid = {}
    for x in range(width + 1):
        count = 0
        for y in range(height + 1):
            match grid[(x, y)]:
                case "#":
                    new_grid[(x, count + y)] = "#"
                    new_grid[(x, count + y + 1)] = "#"
                    count += 1
                case "O":
                    new_grid[(x, count + y)] = "["
                    new_grid[(x, count + y + 1)] = "]"
                    count += 1
                case ".":
                    new_grid[(x, count + y)] = "."
                    new_grid[(x, count + y + 1)] = "."
                    count += 1
                case "@":
                    new_grid[(x, count + y)] = "@"
                    new_grid[(x, count + y + 1)] = "."
                    count += 1
    return new_grid
    
def calc_coordinate(grid):
    res = 0
    for k, v in grid.items():
        if v == "O":
            res += k[0] * 100 + k[1]
    return res
if __name__ == "__main__":
    # Read input
    data = open("day-15/input.txt").read().strip()
    grid, moves = read_input(example)

    # Part 1
    for move in moves:
        grid = move_robot(grid, move)
    res = calc_coordinate(grid)
    # print(f"Part 1: {res}")

    # Part 2
    grid, moves = read_input(example)
    new_grid = augment_grid(grid)
    draw_grid(new_grid)