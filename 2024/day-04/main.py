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
    arr = string_to_array(example)
    
    # print(f"Part 1: {count}") # 2599