left_side = []
right_side = []

with open("day01/input.txt") as f:
    for line in f:
        numbers = line.strip().split("   ")
        left_side.append(int(numbers[0]))
        right_side.append(int(numbers[1]))

left_side.sort()
right_side.sort()

total_diff = 0
for i in range(len(left_side)):
    diff = left_side[i] - right_side[i]
    total_diff += abs(diff)
print(total_diff)


def calculate_similarity_score(left: list, right: list):
    similarity_score = 0
    for i in range(len(left)):
        similarity_score += left[i] * right.count(left[i])  
    return similarity_score

print(calculate_similarity_score(left_side, right_side ))