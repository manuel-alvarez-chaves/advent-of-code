import itertools
from tqdm import tqdm

example = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

def parse_input(text: str):
    text = [line.split(":") for line in text.strip().split("\n")]
    data = [(int(res), nums.strip().split(" ")) for [res, nums] in text]
    clean_data = []
    for (k, v) in data:
        nums = [int(i) for i in v]
        clean_data.append((k, nums))
    return clean_data

if __name__ == "__main__":
    # Read input
    with open("day-07/input.txt", "r") as f:
        data = f.read()
    data = parse_input(data)

    # Part 1
    true_test_values = []
    for (k, v) in tqdm(data, ascii=True):
        num_ops = len(v) - 1
        combs = list(itertools.product(['+', '*'], repeat=num_ops))
        for comb in combs:
            res = v[0]
            for idx in range(len(v) - 1):
                if comb[idx] == '+':
                    res += v[idx + 1]
                elif comb[idx] == '*':
                    res *= v[idx + 1]
            if res == k:
                true_test_values.append(k)
                break

    print(f"Part 1: {sum(true_test_values)}") # 4122618559853

    # Part 2
    true_test_values = []
    for (k, v) in tqdm(data, ascii=True):
        num_ops = len(v) - 1
        combs = list(itertools.product(['+', '*', "||"], repeat=num_ops))
        for comb in combs:
            res = v[0]
            for idx in range(len(v) - 1):
                if comb[idx] == '+':
                    res += v[idx + 1]
                elif comb[idx] == '*':
                    res *= v[idx + 1]
                elif comb[idx] == '||':
                    res = int(str(res) + str(v[idx + 1]))
            if res == k:
                true_test_values.append(k)
                break

    print(f"Part 2: {sum(true_test_values)}") # 227615740238334