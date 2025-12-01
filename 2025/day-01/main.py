example_data = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

def parse_text(text: str) -> list[str]:
    return text.strip().splitlines()

if __name__ == "__main__":
    # Read input
    input_file = "day-01/input.txt"
    with open(input_file, "r") as f:
        data = f.read()

    # Parse instructions
    instructions = parse_text(data)
    # instructions = parse_text(example_data)

    # Part 1
    counter_1: int = 0

    # Part 2
    counter_2: int = 0

    old_position: int = 50
    for line in instructions:
        direction, steps = line[0], int(line[1:])
        if direction == "L":
            new_position = old_position - steps
            turns, new_position = divmod(new_position, 100)
            counter_2 += abs(turns)
        elif direction == "R":
            new_position = old_position + steps
            turns, new_position = divmod(new_position, 100)
            counter_2 += abs(turns)
        if new_position == 0:
            counter_1 += 1
        old_position = new_position
    print(f"Part 1: {counter_1}") # 1066
    print(f"Part 2: {counter_2}") # 6216 # 6223