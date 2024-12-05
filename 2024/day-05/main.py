from pathlib import Path


def file_to_list(path: str) -> list[str]:
    with Path.open(path, "r") as f:
        data = [text[:-1] for text in f.readlines()]
        return data

# Read data
# path_1 = Path("day-05/example1.txt")
# path_2 = Path("day-05/example2.txt")
path_1 = Path("day-05/data1.txt")
path_2 = Path("day-05/data2.txt")
rules = file_to_list(path_1)
rules = [rule.split("|") for rule in rules]
order = {}
for rule in rules:
    x, y = int(rule[0]), int(rule[1])
    if x not in order.keys():
        order[x] = [y]
    else:
        order[x].append(y)
rules = order
del order

updates = [[int(i) for i in item.split(",")] for item in file_to_list(path_2)]

# Part 1
correct_middles = []
incorrect_updates = []
for update in updates:
    correct_order = True
    for idx, i in enumerate(update[1:]):
        if i in rules.keys():
            pages_before = rules[i]
            for page in pages_before:
                if page in update[:idx + 1]:
                    correct_order = False
                    break
                    
    if correct_order:
        correct_middles.append(update[int((len(update) - 1) / 2)])
    else:
        incorrect_updates.append(update)

print(f"Part 1: {sum(correct_middles)}") # 5391

# Part 2
correct_middles = []
for update in incorrect_updates:
    new_update = [update[0]]
    for i in update[1:]:
        new_pos = len(new_update)
        if i in rules.keys():
            pages_before = rules[i]
            for page in pages_before:
                if page in new_update:
                    pos = new_update.index(page)
                    if pos < new_pos:
                        new_pos = pos
        new_update.insert(new_pos, i)
    correct_middles.append(new_update[int((len(new_update) - 1) / 2)])
print(f"Part 2: {sum(correct_middles)}") # 6142

