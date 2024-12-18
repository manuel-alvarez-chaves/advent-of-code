import re

example = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""

pattern = re.compile(r"-?\d+")

class Robot():
    def __init__(self, position, velocity):
        self.initial_position = position
        self.x = position[0]
        self.y = position[1]
        self.vx = velocity[0]
        self.vy = velocity[1]

    def move(self, width, height):
        # X
        new_x = self.x + self.vx
        if new_x > width:
            new_x = new_x - width - 1
        if new_x < 0:
            new_x = width + new_x + 1
        self.x = new_x
        # Y
        new_y = self.y + self.vy
        if new_y > height:
            new_y = new_y - height - 1
        if new_y < 0:
            new_y = height + new_y + 1
        self.y = new_y

    def __repr__(self):
        return f"Robot - [pos: ({self.x}, {self.y}) | vel: ({self.vx}, {self.vy})]"

def parse_input(text: str):
    data = []
    for line in text.split("\n"):
        if line == "":
            continue
        x, y, vx, vy = map(int, pattern.findall(line))
        data.append([(x, y), (vx, vy)])
    return data

def draw_grid(robots: list[Robot], width: int, height: int) -> None:
    grid = {(x, y): "." for x in range(width) for y in range(height)}
    
    for robot in robots:
        val = grid[(robot.x, robot.y)]
        if val == ".":
            grid[(robot.x, robot.y)] = 1
        else:
            grid[(robot.x, robot.y)] += 1

    text = ""
    for y in range(height):
        for x in range(width):
            text += str(grid[(x, y)])
        text += "\n"
    
    print(text)
    return None

def calc_safety_factor(robots: list[Robot], width: int, height: int) -> int:
    quadrants = [0, 0, 0, 0]
    for robot in robots:
        if robot.x < width // 2 and robot.y < height // 2:
            quadrants[0] += 1
        elif robot.x < width // 2 and robot.y > height // 2:
            quadrants[1] += 1
        elif robot.x > width // 2 and robot.y < height // 2:
            quadrants[2] += 1
        elif robot.x > width // 2 and robot.y > height // 2:
            quadrants[3] += 1
    
    safety_factor = 1
    for i in quadrants:
        safety_factor *= i
    return safety_factor

if __name__ == "__main__":
    # Read inpuit
    data = parse_input(example)
    data = parse_input(open("day-14/input.txt").read().strip())
    robots = [Robot(*entry) for entry in data]
    
    # Part 1
    width, height = 101, 103
    for _ in range(100):
        for robot in robots:
            robot.move(width - 1, height - 1)
    safety_factor = calc_safety_factor(robots, width - 1, height - 1)
    print(f"Part 1: {safety_factor}") # 214400550

    # Part 2
    # Simulate for a while and find the time at which the robots have
    # the smallest safety factor. This means that the robots are clustered
    # together in one of the quadrants forming the christmas tree.
    robots = [Robot(*entry) for entry in data]
    scores = []
    for idx in range(10000):
        for robot in robots:
            robot.move(width - 1, height - 1)
        if idx == 8148:
            draw_grid(robots, width, height)
        safety_factor = calc_safety_factor(robots, width - 1, height - 1)
        scores.append(safety_factor)
    idx = scores.index(min(scores))
    print(f"Part 2: {idx + 1}") # 8149