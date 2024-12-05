import re

example_memory_1 = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
example_memory_2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

if __name__ == "__main__":
    with open("day-03/input.txt", "r") as f:
        memory = f.read()

    # Part 1
    pattern = re.compile(r"mul\((\d+),(\d+)\)")
    matches = pattern.findall(memory)
    result = 0
    for match in matches:
        result += int(match[0]) * int(match[1])
    print(f"Part 1: {result}") # 182619815


    # Part 2
    result = 0
    multiply = True
    pattern = re.compile(r"do\(\)|don't\(\)|mul\((\d+),(\d+)\)")
    for match in re.finditer(pattern, memory):
        if match.group(0) == "do()":
            multiply = True
        elif match.group(0) == "don't()":
            multiply = False
        elif multiply:
            result += int(match.group(1)) * int(match.group(2))
    print(f"Part 2: {result}") # 80747545
