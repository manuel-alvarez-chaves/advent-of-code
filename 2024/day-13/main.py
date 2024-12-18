import re

import numpy as np

cost_A = 3
cost_B = 1

example = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""

pattern = re.compile(r"(\d+)")

def cost(chunk, error=False):
    a, b, c, d, e, f = chunk
    buttons = np.array([[a, c], [b, d]])
    prize = np.array([e, f])
    if error:
        prize += 10000000000000
    
    presses = np.linalg.solve(buttons, prize).round().astype(int)
    if (presses @ buttons.T == prize).all():
        return presses @ (cost_A, cost_B)
    else:
        return 0
        
def read_input(text: str) -> list[int]:
    data = pattern.findall(text)
    data = list(map(int, data))
    chunks = []
    for i in range(0, len(data), 6):
        chunks.append(data[i:i+6])
    return chunks

if __name__ == "__main__":
    # Read input
    text = open("day-13/input.txt").read()
    data = read_input(text)

    # Part 1
    total = 0
    for entry in data:
        total += cost(entry)
    print(f"Part 1: {total}") # 27105

    # Part 2
    total = 0
    for entry in data:
        total += cost(entry, True)
    print(f"Part 2: {total}") # 101726882250942