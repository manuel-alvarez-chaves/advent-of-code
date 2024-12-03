import numpy as np

example_1 = np.array([3, 4, 2, 1, 3, 3])
example_2 = np.array([4, 3, 5, 3, 9, 3])

if __name__ == "__main__":
    text = np.loadtxt("day-01/input.txt", dtype=int)
    locations_1, locations_2 = np.hsplit(text, 2)
    locations_1 = np.sort(locations_1.flatten())
    locations_2 = np.sort(locations_2.flatten())

    # Part 1
    distances = np.abs(locations_1 - locations_2)
    total_distance = np.sum(np.abs(distances))
    print(f"Part 1: {total_distance}") # 1603498

    # Part 2
    u, c = np.unique(locations_2, return_counts=True)
    unique_counts = dict(zip(u, c))
    score = [i * unique_counts.get(i, 0) for i in locations_1]
    print(f"Part 2: {np.sum(score)}") # 25574739