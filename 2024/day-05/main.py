def file_to_list(path: str) -> list[str]:
    with open(path, "r") as f:
        data = [text[:-1] for text in f.readlines()]
        return data

# Read data
path_1 = "day-05/example1.txt"
path_2 = "day-05/example2.txt"
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
correct_order = True
for update in updates:
    for idx, i in enumerate(update[1:]):
        if i in rules.keys():
            pages_before = rules[i]
            for page in pages_before:
                if page in update[:idx + 1]:
                    correct_order = False
    if correct_order:
        correct_middles.append(update[int((len(update) - 1) / 2)])

print(f"Part 1: {sum(correct_middles)}")
