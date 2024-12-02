def open_file(sort=False):
    left_side = []
    right_side = []

    with open("day01/input.txt") as f:
        for line in f:
            numbers = line.strip().split("   ")
            left_side.append(int(numbers[0]))
            right_side.append(int(numbers[1]))

    if sort:
        left_side.sort()
        right_side.sort()
    return left_side, right_side


def part1():
    left_side, right_side = open_file(sort=True)
    total_diff = 0
    for i in range(len(left_side)):
        diff = left_side[i] - right_side[i]
        total_diff += abs(diff)
    return total_diff

def part2():
    left_side, right_side = open_file(sort=False)
    
    similarity_score = 0
    items_dict = {}
    
    for i in range(len(right_side)):
        if right_side[i] in items_dict: items_dict[right_side[i]] += 1
        else: items_dict[right_side[i]] = 1

    for i in range(len(left_side)):
        if left_side[i] in items_dict:
            similarity_score += left_side[i] * items_dict[left_side[i]]

    return similarity_score
