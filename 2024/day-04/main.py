import numpy as np

example = r"""MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

def available_movements(arr: np.array, pos: tuple[np.array], offset: int) -> tuple[bool]:
    n, m = arr.shape
    x, y = pos
    up, down, left, right = False, False, False, False
    if x - offset >= 0:
        up = True 
    if x + offset <= n - 1:
        down = True
    if y - offset >= 0:
        left = True
    if y + offset <= m - 1:
        right = True
    return (up, down, left, right)

def string_to_array(text: str) -> np.array:
    arr, inner = [], []
    for char in text:
        if char == "\n":
            arr.append(inner)
            inner = []
        else:
            inner.append(char)
    arr.append(inner)
    return np.array(arr)

if __name__ == "__main__":
    # Read data
    with open("day-04/input.txt", "r") as f:
        data = f.read()
    arr = string_to_array(data)
    
    # Part 1
    pattern = "XMAS"
    count = 0
    for pos, val in np.ndenumerate(arr):
        x, y = pos
        up, down, left, right = available_movements(arr, pos, 3)
        # 6 7 8
        # 5   1
        # 4 3 2
        if right: # 1
            text = val + arr[x, y + 1] + arr[x, y + 2] + arr[x, y + 3]
            if text == pattern:
                count += 1
        if right and down: # 2
            text = val + arr[x + 1, y + 1] + arr[x + 2, y + 2] + arr[x + 3, y + 3]
            if text == pattern:
                count += 1
        if down: # 3
            text = val + arr[x + 1, y] + arr[x + 2, y] + arr[x + 3, y]
            if text == pattern:
                count += 1
        if down and left: # 4
            text = val + arr[x + 1, y - 1] + arr[x + 2, y - 2] + arr[x + 3, y - 3]
            if text == pattern:
                count += 1
        if left: # 5
            text = val + arr[x, y - 1] + arr[x, y - 2] + arr[x, y - 3]
            if text == pattern:
                count += 1
        if left and up: # 6
            text = val + arr[x - 1, y - 1] + arr[x - 2, y - 2] + arr[x - 3, y - 3]
            if text == pattern:
                count += 1
        if up: # 7
            text = val + arr[x - 1, y] + arr[x - 2, y] + arr[x - 3, y]
            if text == pattern:
                count += 1
        if up and right: # 8
            text = val + arr[x - 1, y + 1] + arr[x - 2, y + 2] + arr[x - 3, y + 3]
            if text == pattern:
                count += 1
    print(f"Part 1: {count}") # 2599

    # Part 2
    patterns = ["MASMAS", "MASSAM", "SAMMAS", "SAMSAM"]
    count = 0
    for pos, val in np.ndenumerate(arr):
        if val != "A":
            continue
        x, y = pos
        up, down, left, right = available_movements(arr, pos, 1)
        if up and down and left and right:
            # Plus
            # plus = arr[x - 1, y] + arr[x, y] + arr[x + 1, y] + arr[x, y - 1] + arr[x, y] + arr[x, y + 1]
            # if plus in patterns:
            #     count += 1

            # Cross
            cross = arr[x - 1, y - 1] + arr[x, y] + arr[x + 1, y + 1] + arr[x + 1, y - 1] + arr[x, y] + arr[x - 1, y + 1]
            if cross in patterns:
                count += 1
    print(f"Part 2: {count}") # 1978 | 1948