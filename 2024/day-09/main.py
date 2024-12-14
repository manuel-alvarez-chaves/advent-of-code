from tqdm import tqdm

example = "12345"
example = "2333133121414131402"

def read_input(file_path: str) -> list:
    return open(file_path, "r").read().strip()

def parse_text(text: str) -> list:
    text = [int(i) for i in text]
    parsed = []
    count = 0
    for idx, i in enumerate(text):
        if idx % 2 == 0:
            parsed += [count] * i
            count += 1
        else:
            parsed += ["."] * i
    return parsed

def get_chacksum(disk):
    return sum(i * x for i, x in enumerate(disk) if x != ".")

data = read_input("day-09/input.txt")
parsed = parse_text(example)

# Part 1
def defrag(parsed: list) -> list:
    pos_left = 0
    pos_right = len(parsed) - 1

    while True:
        while parsed[pos_left] != ".":
            pos_left += 1
        while parsed[pos_right] == ".":
            pos_right -= 1
        if pos_left >= pos_right:
            break

        parsed[pos_left], parsed[pos_right] = parsed[pos_right], parsed[pos_left]
    return parsed


print(f"Part 1: {get_chacksum(defrag(parsed.copy()))}") # 6367087064415

# Part 2
print(f"Part 2: 'i gave up'")