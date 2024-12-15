from functools import cache

example = [125, 17]

@cache
def count_stones(stone: int, num_blinks: int):
    if num_blinks == 0: 
        return 1
    if stone == 0: 
        return count_stones(1, num_blinks - 1)
    if len(str(stone)) % 2 is True:
        return count_stones(2024 * stone, num_blinks - 1)
    stone = str(stone)
    middle = len(stone) // 2
    first, second = (stone[:middle], stone[middle:])
    return (count_stones(first, num_blinks - 1) + count_stones(second, num_blinks - 1))


def read_input(path: str) -> list[int]:
    text = open(path).read().strip()
    return [int(i) for i in text.split(" ")]

if __name__ == "__main__":
    data = read_input("day-11/input.txt")

    # Part 1
    num_blinks = 25
    res = 0
    for i in data.copy():
        res += count_stones(i, num_blinks)
    print(f"Part 1: {res}") # 251658240

    # Part 2
    num_blinks = 75
    res = 0
    for i in data.copy():
        res += count_stones(i, num_blinks)
    print(f"Part 2: {res}") # 283341988972178712821760
    