import numpy as np

example_data = [[7, 6, 4, 2, 1],
[1, 2, 7, 8, 9],
[9, 7, 6, 2, 1],
[1, 3, 2, 4, 5],
[8, 6, 4, 4, 1],
[1, 3, 6, 7, 9]]

def analyze_report(report: np.array) -> bool:
    report = report.flatten()
    diff = np.diff(report)
    # Check if report increases or decreases
    if not(np.all(diff < 0) or np.all(diff > 0)):
        return False

    # Check if the levels differ by at least 1 and less than 4
    diff = np.abs(diff)
    if not(np.all(diff <= 3) and np.all(diff >= 1)):
        return False
    
    return True
    

if __name__ == "__main__":
    # Load data
    with open("day-02/input.txt", "r") as f:
        data = f.readlines()
    
    # Part 1
    count = 0
    for row in data:
        row = np.array([int(i) for i in row.split()], dtype=int)
        if analyze_report(row):
            count += 1
    print(f"Part 1: {count}")

    # Part 2
    count = 0
    for row in data:
        row = np.array([int(i) for i in row.split()], dtype=int)
        if analyze_report(row):
            count += 1
            continue
        for idx in range(len(row)):
            new_row = np.delete(row, idx)
            if analyze_report(new_row):
                count += 1
                break
    print(f"Part 2: {count}")